import datetime
from flask import Blueprint, flash, get_flashed_messages, render_template, request, redirect, url_for
from sql.db import DB  # Import your DB class
from utils.api import API  # Import your API class for football API
from football.forms import TeamForm, TeamSearchForm, TeamFetchForm, AdminTeamSearchForm, AssocForm
from roles.permissions import admin_permission
from flask_login import current_user, login_required

football = Blueprint('football', __name__, url_prefix='/football', template_folder='templates')

def get_total(partial_query, args={}):
    total = 0
    try:
        result = DB.selectOne("SELECT count(1) as total FROM "+partial_query, args)
        if result.status and result.row:
            total = int(result.row["total"])
    except Exception as e:
        print(f"Error getting total {e}")
        total = 0
    return total

@football.route("/fetch", methods=["GET", "POST"])
@admin_permission.require(http_exception=403)
def fetch():
    form = TeamFetchForm()  # Assuming you have a TeamSearchForm for football teams
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
def list():
    form = TeamSearchForm(request.args)
    allowed_columns = ["name", "country", "founded_year"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT id, name, code, country, founded, national, logo_url, source, 
    IFNULL((SELECT count(1) FROM IS601_WatchList WHERE user_id = %(user_id)s and team_id = IS601_Team.id), 0) as 'is_assoc' 
    FROM IS601_Team WHERE 1=1
    """
    args = {"user_id": current_user.id}
    where = ""

    if form.name.data:
        args["name"] = f"%{form.name.data}%"
        where += " AND name LIKE %(name)s"
    if form.country.data:
        args["country"] = f"%{form.country.data}%"
        where += " AND country LIKE %(country)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"

    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"

    result = DB.selectAll(query + where, args)
    rows = []

    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Team""")
    return render_template("team_list.html", rows=rows, form=form, total_records=total_records)



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
    if not id:
        flash("Missing id", "danger")
    else:
        try:
            result = DB.selectOne("""SELECT name, code, country, founded, national, logo_url, source, 
    IFNULL((SELECT count(1) FROM IS601_WatchList WHERE user_id = %(user_id)s and team_id = IS601_Team.id), 0) as 'is_assoc' 
    FROM IS601_Team WHERE id = %(team_id)s""", {"team_id": id, "user_id": current_user.id})
            if result.status and result.row:
                return render_template("team_view.html", data=result.row)
        except Exception as e:
            print(f"Error fetching record {e}")
            flash("Error finding item","danger")
    return redirect(url_for("football.list"))

#ss4746 #12-09-2023
@football.route("/track", methods=["GET"])
@login_required
def track():
    id = request.args.get("id")
    args = {**request.args}
    del args["id"]
    if not id:
        flash("Missing id parameter", "danger")
    else:
        params = {"user_id": current_user.id, "team_id": id}
        try : 
            try:
                result = DB.insertOne("INSERT INTO IS601_WatchList (team_id, user_id) VALUES (%(team_id)s, %(user_id)s)", params)
                if result.status:
                    flash("Added team to your watch list", "success")
            except Exception as e:
                print(f"Should just be a duplicate exception and can be ignored {e}")
                result = DB.delete("DELETE FROM IS601_WatchList WHERE team_id = %(team_id)s AND user_id = %(user_id)s", params)
                if result.status:
                    flash("Removed team from your watch list", "success")
        except Exception as e:
            print(f"Error doing something with track/untrack {e}")
            flash("An unhandled error occurred please try again" ,"danger")

    url = request.referrer
    if url:
        from urllib.parse import urlparse
        url_stuff = urlparse(url)
        watchlist_url = url_for("football.watchlist")
        print(f"Parsed url {url_stuff} {watchlist_url}")
        if url_stuff.path == url_for("football.watchlist"):
            return redirect(url_for("football.watchlist", **args))
        elif url_stuff.path == url_for("football.view"):
            args["id"] = id
            return redirect(url_for("football.view", **args))
    return redirect(url_for("football.list", **args))

@football.route("/watchlist", methods=["GET"])
def watchlist():
    
    id = request.args.get("id", current_user.id)
    form = TeamSearchForm(request.args)
    allowed_columns = ["name", "country", "founded_year"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT t.id, name, code, country, founded, national, logo_url, source, 
    IFNULL((SELECT count(1) FROM IS601_WatchList WHERE user_id = %(user_id)s and team_id = t.id), 0) as 'is_assoc' 
    FROM IS601_Team t JOIN IS601_WatchList w ON t.id = w.team_id
    WHERE w.user_id = %(user_id)s
    """
    args = {"user_id":id}
    where = ""

    if form.name.data:
        args["name"] = f"%{form.name.data}%"
        where += " AND name LIKE %(name)s"
    if form.country.data:
        args["country"] = f"%{form.country.data}%"
        where += " AND country LIKE %(country)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"

    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"

    result = DB.selectAll(query + where, args)
    rows = []

    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Team t JOIN IS601_WatchList w ON t.id = w.team_id
     WHERE w.user_id = %(user_id)s""", {"user_id": id})
    return render_template("team_list.html", rows=rows, form=form, title="Watchlist", total_records=total_records)

@football.route("/clear", methods=["GET"])
def clear():
    id = request.args.get("id")
    args = {**request.args}
    if "id" in args:
        del args["id"]
    if not id:
        flash("Missing id", "danger")
    else:
        if id == current_user.id or current_user.has_role("Admin"):
            try:
                result = DB.delete("DELETE FROM IS601_WatchList WHERE user_id = %(user_id)s", {"user_id":id})
                if result.status:
                    flash("Cleared watchlist", "success")
            except Exception as e:
                print(f"Error clearing watchlist {e}")
                flash("Error clearing watchlist","danger")
        

    return redirect(url_for("football.watchlist", **args))


@football.route("/associations", methods=["GET"])
@admin_permission.require(http_exception=403)
def associations():
    
    form = AdminTeamSearchForm(request.args)
    allowed_columns = ["name", "country", "founded_year"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT u.id as user_id, username, c.id, name, code, country, founded, national, logo_url, source
    FROM IS601_Team c JOIN IS601_WatchList w ON c.id = w.team_id LEFT JOIN IS601_Users u on u.id = w.user_id
    WHERE 1=1
    """
    args = {}
    where = ""

    if form.name.data:
        args["name"] = f"%{form.name.data}%"
        where += " AND name LIKE %(name)s"
    if form.country.data:
        args["country"] = f"%{form.country.data}%"
        where += " AND country LIKE %(country)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"

    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"

    result = DB.selectAll(query + where, args)
    rows = []

    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Team t JOIN IS601_WatchList w ON t.id = w.team_id
     WHERE w.user_id = %(user_id)s""", {"user_id": id})
    return render_template("team_list.html", rows=rows, form=form, title="Associations", total_records=total_records)

@football.route("/unwatched", methods=["GET"])
@login_required
def unwatched():
    form = TeamSearchForm(request.args)
    allowed_columns = ["name", "country", "founded_year"]
    form.sort.choices = [(k, k) for k in allowed_columns]
    query = """
    SELECT c.id, name, code, country, founded, national, logo_url,
    IFNULL((SElECT count(1) FROM IS601_WatchList WHERE user_id = %(user_id)s and team_id = c.id), 0) as 'is_assoc' 
    FROM IS601_Team c 
    
     WHERE c.id not in (SELECT DISTINCT team_id FROM IS601_WatchList)
    """
    args = {"user_id": current_user.id}
    where = ""

    if form.name.data:
        args["name"] = f"%{form.name.data}%"
        where += " AND name LIKE %(name)s"
    if form.country.data:
        args["country"] = f"%{form.country.data}%"
        where += " AND country LIKE %(country)s"

    if form.sort.data in allowed_columns and form.order.data in ["asc", "desc"]:
        where += f" ORDER BY {form.sort.data} {form.order.data}"
    
    
    limit = 10
    if form.limit.data:
        limit = form.limit.data
        if limit < 1:
            limit = 1
        if limit > 100:
            limit = 100
        args["limit"] = limit
        where += " LIMIT %(limit)s"

    result = DB.selectAll(query+where, args)
    rows = []
    if result.status and result.rows:
        rows = result.rows

    total_records = get_total(""" IS601_Team c 
     WHERE c.id not in (SELECT DISTINCT team_id FROM IS601_WatchList)""")
    return render_template("team_list.html", rows=rows, form=form, title="Unwatched Items", total_records=total_records)

@football.route("/manage", methods=["GET"])
def manage():
    form = AssocForm(request.args)
    users = []
    teams = []
    username = form.username.data
    team_name = form.team.data
    if username and team_name:
        result = DB.selectAll("SELECT id, username FROM IS601_Users WHERE username like %(username)s LIMIT 25",{"username":f"%{username}%"})
        if result.status and result.rows:
            users = result.rows
        result = DB.selectAll("SELECT id, name FROM IS601_Team WHERE name like %(team)s LIMIT 25", {"team":f"%{team_name}%"})
        if result.status and result.rows:
            teams = result.rows
    print(f"Users {users}")
    print(f"Teams {teams}")
    return render_template("team_association.html", users=users, teams=teams, form=form)

@football.route("/manage_assoc", methods=["POST"])
def manage_assoc():
    users = request.form.getlist("users[]")
    teams = request.form.getlist("teams[]")
    print(users, teams)
    args = {**request.args}
    if users and teams: # we need both for this to work
        mappings = []
        for user in users:
            for team in teams:
                mappings.append({"user_id":user, "team_id":team})
        if len(mappings) > 0:
            for mapping in mappings:
                print(f"mapping {mapping}")
                try:
                    result = DB.insertOne("INSERT INTO IS601_WatchList (user_id, team_id) VALUES(%(user_id)s, %(team_id)s)", mapping)
                    if result.status:
                        pass
                        #flash(f"Successfully enabled/disabled roles for the user/role {len(mappings)} mappings", "success")
                except Exception as e:
                    print(f"Insert error {e}")
                    result = DB.delete("DELETE FROM IS601_WatchList WHERE user_id = %(user_id)s and team_id = %(team_id)s",mapping)
            flash("Successfully applied mappings", "success")
        else:
            flash("No user/team mappings", "danger")

    if "users" in args:
        del args["users"]
    if "teams" in args:
        del args["teams"]
    return redirect(url_for("football.manage", **args))