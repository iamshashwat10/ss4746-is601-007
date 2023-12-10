from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, DecimalField, TextAreaField, validators, SubmitField
from wtforms.validators import URL

class TeamFetchForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=20)])
    submit = SubmitField("Find")

class TeamForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=20)])
    code = StringField('Code', [validators.Length(min=3, max=5, message="Code must be between 3 and 5 characters")])
    founded = DecimalField('Founded', [validators.NumberRange(min=1800, max=2023, message="Invalid year")])
    country = StringField('Country', [validators.Length(min=1, max=20, message="Invalid country name")])
    national = StringField('National', [validators.AnyOf(['0', '1'], message="National must be 0 or 1")])
    logo_url = StringField('Logo URL')
    submit = SubmitField("Save")

class TeamSearchForm(FlaskForm):
    class Meta:
        # This overrides the value from the base form.
        csrf = False
    name = StringField("Name")
    country = StringField("Country")
    founded_year = IntegerField("Founded Year") 
    limit = IntegerField("Limit", default=10)
    sort = SelectField("Sort")
    order = SelectField("Order", choices=[("asc","+"), ("desc","-")])
    submit = SubmitField("Filter")

class AdminTeamSearchForm(TeamSearchForm):
    username = StringField("Username")

class AssocForm(FlaskForm):
    class Meta:
        # This overrides the value from the base form.
        csrf = False
    username = StringField("Username")
    team = StringField("Team Name")
    submit = SubmitField("Filter")