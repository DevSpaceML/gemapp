from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField,SelectField, validators
from wtforms.widgets import TextArea


class eventsform(FlaskForm):
    evntname = StringField('Event Name', validators=[validators.length(max=200)])
    venue = StringField('Venue Name', validators=[validators.length(max=200)])
    artist = StringField('Artist Name', validators=[validators.length(max=200)])
    evntdate = StringField('event date', validators=[validators.length(max=200)])
    descrip  = TextArea('Describe the event',rows=15, cols=50)
    startdate = StringField('Start of date range', validators=[validators.length(max=200)])
    end_date = StringField('End of date range', validators=[validators.length(max=200)])
    city = StringField('city', validators=[validators.length(max=200)])
    address = StringField('address', validators=[validators.length(max=200)])
    country = StringField('country', validators=[validators.length(max=200)])
    submit = SubmitField('Create Event')
    def __init__(self, arg):
        super(eventsform, self).__init__()
        self.arg = arg