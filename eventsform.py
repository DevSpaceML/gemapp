from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField,SelectField, validators
from wtforms.widgets import TextArea

class EventsForm(FlaskForm):
    evntname = StringField('Event Name', validators=[validators.length(max=200)])
    evnt_type = StringField('Type of event', validators=[validators.length(max=200)])
    venue = StringField('Venue Name', validators=[validators.length(max=200)])
    artist = StringField('Artist Name', validators=[validators.length(max=200)])
    evntdate = StringField('Event Date', validators=[validators.length(max=200)])
    evnt_charge = StringField('Ticket Price', validators=[validators.length(max=200)])
    descrip  = StringField('Brief description', widget=TextArea())
    start_date = StringField('Start of date range', validators=[validators.length(max=200)])
    end_date = StringField('End of date range', validators=[validators.length(max=200)])
    city = StringField('City', validators=[validators.length(max=200)])
    country = StringField('Country', validators=[validators.length(max=200)])
    address = StringField('Address', validators=[validators.length(max=200)])
    gps_point = StringField('GPS Coordinates', validators=[validators.length(max=200)])
    country = StringField('Country', validators=[validators.length(max=200)])
    rel_evnt = StringField('Related Event', validators=[validators.length(max=200)])
    submit = SubmitField('Create Event')
    def __init__(self, arg):
        super(EventsForm, self).__init__()
        self.arg = arg