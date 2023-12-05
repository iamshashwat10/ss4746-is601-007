from flask import Blueprint, flash, render_template, request, redirect, url_for
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
                    """INSERT INTO IS601_Team (name, code, country, founded, national, logo_url)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        ON DUPLICATE KEY UPDATE
                        code = VALUES(code),
                        country = VALUES(country),
                        founded = VALUES(founded),
                        national = VALUES(national),
                        logo_url = VALUES(logo_url)""",
                    team_data['name'], team_data['code'], team_data['country'], team_data['founded'],
                    team_data['national'], team_data.get('logo_url', '')
                )

                if result.status:
                    flash(f"Loaded team record for {form.name.data}", "success")
                else:
                    flash(f"Error loading team record: {result.error}", "danger")
            else:
                flash(f"No team found for {form.name.data}", "warning")

        except Exception as e:
            flash(f"Error loading team record: {e}", "danger")

    return render_template("team_search.html", form=form)

@football.route("/add", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def add():
    form = TeamForm()
    if form.validate_on_submit():
        try:
            # Create a new team record in the database
            team_data = {
                'name': form.name.data,
                'code': form.code.data,
                'country': form.country.data,
                'founded': form.founded.data,
                'national': form.national.data,
                'logo_url': form.logo_url.data
            }
            print("Form Data:", form.data)
            # Assuming your database table for football teams is named IS601_Team
            result = DB.insertOne(
                """INSERT INTO IS601_Team (name, code, country, founded, national, logo_url)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    code = VALUES(code),
                    country = VALUES(country),
                    founded = VALUES(founded),
                    national = VALUES(national),
                    logo_url = VALUES(logo_url)""",
                team_data['name'], team_data['code'], team_data['country'], team_data['founded'],
                team_data['national'], team_data.get('logo_url', '')
            )
            # Print the result of the database insertion for debugging
            if result.status:
                flash(f"Created team record for {form.name.data}", "success")
            else:
                flash(f"Error creating team record: {result.error}", "danger")
        except Exception as e:
            flash(f"Error creating team record: {e}", "danger")
    else:
        # Print form errors for debugging
        print("Form Errors:", form.errors)
    
    return render_template("team_form.html", form=form, type="Create")

@football.route("/edit", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def edit():
    form = TeamForm()
    id = request.args.get("id")
    if id is None:
        flash("Missing ID", "danger")
        return redirect(url_for("football.list"))
    if form.validate_on_submit() and id:
        try:
            # Update the existing team record in the database
            result = DB.insertOne(
                "UPDATE IS601_Team SET name = %s, code = %s, country = %s, founded = %s, national = %s, logo_url = %s WHERE id = %s",
                form.name.data, form.code.data, form.country.data, form.founded.data,
                form.national.data, form.logo_url.data, id
            )
            if result.status:
                flash(f"Updated team record for {form.name.data}", "success")
        except Exception as e:
            flash(f"Error updating team record: {e}", "danger")
    try:
        result = DB.selectOne(
            "SELECT name, code, country, founded, national, logo_url FROM IS601_Team WHERE id = %s",
            id
        )
        if result.status and result.row:
            form = TeamForm(data=result.row)
    except Exception as e:
        flash("Error fetching team record", "danger")
    return render_template("team_form.html", form=form, type="Edit")

@football.route("/list", methods=["GET"])
@admin_permission.require(http_exception=403)
def list():
    rows = []
    try:
        result = DB.selectAll("SELECT id, name, code, country, founded, national, logo_url FROM IS601_Team LIMIT 100")
        if result.status and result.rows:
            rows = result.rows
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