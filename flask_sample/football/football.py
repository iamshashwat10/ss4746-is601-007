import datetime
from flask import Blueprint, flash, get_flashed_messages, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from utils.api import API  # Import your API class for football API
from football.forms import TeamForm, TeamSearchForm  # Import your TeamForm class
from roles.permissions import admin_permission

football = Blueprint('football', __name__, url_prefix='/football', template_folder='templates')

@football.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = TeamSearchForm()  # Assuming you have a TeamSearchForm for football teams
    if form.validate_on_submit():
        try:
            # Use your football API class (e.g., FootballAPI) to get team information
            result = API.get("/v3/teams", params={"name": form.name.data})
            
            if result.get('results', 0) > 0:
                team_data = result['response'][0]['team']

                # Assuming your database table for football teams is named IS601_Team
                result = DB.insertOne(
                    """INSERT INTO IS601_Team (id, name, code, country, founded, national, logo_url, source)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        code = VALUES(code),
                        country = VALUES(country),
                        founded = VALUES(founded),
                        national = VALUES(national),
                        logo_url = VALUES(logo_url),
                        source = VALUES(source)""",
                    team_data['id'], team_data['name'], team_data['code'], team_data['country'], team_data['founded'],
                    team_data['national'], team_data.get('logo', ''), 'API'
                )

                if result.status:
                    flash(f"Loaded team record for {form.name.data} from API", "success")
                else:
                    flash(f"Error loading team record from API: {result.error}", "danger")
            else:
                flash(f"No team found for {form.name.data}", "warning")

        except Exception as e:
            flash(f"Error loading team record: {e}", "danger")

    return render_template("team_search.html", form=form)

#ss4746
#Date: 12/05/2023
@football.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = TeamForm()

    if form.validate_on_submit():
        try:
            # Check if the team already exists in the database
            existing_team = DB.selectOne(
                "SELECT id FROM IS601_Team WHERE name = %s",
                form.name.data
            )

            if existing_team.status and existing_team.row:
                # Team already exists, inform the user
                flash(f"Team with the name '{form.name.data}' already exists. "
                      f"If you want to modify it, you can do so on the team edit page.", "warning")
            else:
                # Team doesn't exist, create a new record

                # Additional form data validation
                if not 3 <= len(form.code.data) <= 5:
                    flash("Code must be between 3 and 5 characters.", "danger")
                    return render_template("team_form.html", form=form, type="Create")

                try:
                    founded_year = int(form.founded.data)
                    if not 0 <= founded_year <= datetime.datetime.now().year:
                        raise ValueError("Invalid year")
                except ValueError:
                    flash("Founded must be a valid year.", "danger")
                    return render_template("team_form.html", form=form, type="Create")

                result = DB.insertOne(
                    """INSERT INTO IS601_Team (name, code, country, founded, national, logo_url)
                        VALUES (%s, %s, %s, %s, %s, %s)""",
                    form.name.data, form.code.data, form.country.data, founded_year,
                    form.national.data, form.logo_url.data
                )

                # Print the result of the database insertion for debugging
                if result.status:
                    flash(f"Created team record for {form.name.data}", "success")
                else:
                    flash(f"Error creating team record: {result.error}", "danger")
        except Exception as e:
            flash(f"Error creating team record: {e}", "danger")
    else:
        # Form is not valid, display validation errors
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"{field.title()} {error}", "danger")

    return render_template("team_form.html", form=form, type="Create")




@football.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    id = request.args.get("id")

    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("football.list"))

    try:
        result = DB.selectOne(
            "SELECT name, code, country, founded, national, logo_url FROM IS601_Team WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = TeamForm(data=result.row)
    except Exception as e:
        flash("Error fetching team record", "danger")
        return redirect(url_for("football.list"))

    if request.method == "POST":
        try:
            # Additional form data validation
            if not 3 <= len(request.form["code"]) <= 5:
                flash("Code must be between 3 and 5 characters.", "danger")
                return render_template("team_form.html", form=form, type="Edit")

            try:
                founded_year = int(request.form["founded"])
                if not 0 <= founded_year <= datetime.datetime.now().year:
                    raise ValueError("Invalid year")
            except ValueError:
                flash("Founded must be a valid year.", "danger")
                return render_template("team_form.html", form=form, type="Edit")

            if request.form["national"] not in ['0', '1']:
                flash("National must be 0 or 1.", "danger")
                return render_template("team_form.html", form=form, type="Edit")

            # Update the existing team record in the database
            result = DB.insertOne(
                "UPDATE IS601_Team SET name = %s, code = %s, country = %s, founded = %s, national = %s, logo_url = %s WHERE id = %s",
                request.form["name"], request.form["code"], request.form["country"], founded_year,
                request.form["national"], request.form["logo_url"], id
            )

            if result.status:
                flash(f"Updated team record for {request.form['name']}", "success")
                return redirect(url_for("football.list"))
            else:
                flash(f"Error updating team record: {result.error}", "danger")

        except Exception as e:
            flash(f"Error updating team record: {e}", "danger")

    return render_template("team_form.html", form=form, type="Edit")




@football.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        # Set default limit
        limit = min(int(request.args.get("limit", 100)), 100)

        # Get sorting parameters from query string
        sort_field = request.args.get("sort_field", "id")
        sort_order = request.args.get("sort_order", "asc").upper()

        # Validate sort order
        if sort_order not in ["ASC", "DESC"]:
            sort_order = "ASC"

        result = DB.selectAll(
            f"SELECT id, name, code, country, founded, national, logo_url, source FROM IS601_Team "
            f"ORDER BY {sort_field} {sort_order} LIMIT %s",
            limit
        )
        if result.status and result.rows:
            rows = result.rows
        else:
            flash("No team records available.", "info")
    except Exception as e:
        print(e)
        flash("Error getting team records", "danger")
    
    return render_template("team_list.html", rows=rows)




@football.route("/delete", methods=["GET"])
@admin_permission.require(http_exception=403)
def delete():
    id = request.args.get("id")
    args = {**request.args}
    if id:
        try:
            # Delete the team record from the database
            result = DB.delete("DELETE FROM IS601_Team WHERE id = %s", id)
            if result.status:
                flash("Deleted team record", "success")
        except Exception as e:
            flash(f"Error deleting team record: {e}", "danger")
        del args["id"]
    else:
        flash("No ID present", "warning")
    return redirect(url_for("football.list", **args))

@football.route("/view", methods=["GET"])
def view():
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("football.list"))
    try:
        result = DB.selectOne(
            "SELECT name, code, country, founded, national, logo_url FROM IS601_Team WHERE id = %s",
            id
        )
        if result.status and result.row:
            return render_template("team_view.html", team=result.row)
        else:
            flash("Team record not found", "danger")
    except Exception as e:
        print(f"Team error {e}")
        flash("Error fetching team record", "danger")
    return redirect(url_for("football.list"))