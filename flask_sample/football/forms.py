from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators, SubmitField
from wtforms.validators import URL

class TeamSearchForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=20)])
    submit = SubmitField("Find")

class TeamForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=1, max=20)])
    code = StringField('Code', [validators.Length(min=3, max=5)])
    founded = DecimalField('Founded', [validators.NumberRange(min=0)])
    country = StringField('Country', [validators.Length(min=1, max=20)])
    national = StringField('National', [validators.Length(min=1, max=20)])
    logo_url = StringField('Logo URL')
   # venue_id = DecimalField('Venue ID', [validators.NumberRange(min=0)])
    submit = SubmitField("Save")