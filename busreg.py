
from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField,SelectField, validators
from wtforms.widgets import TextArea

class BusRegForm(FlaskForm):
    name = StringField('Business Name', validators=[validators.length(max=100)])   
    BusType = SelectField('Business Type', choices=[('lodging', 'lodging'), ('Restaurant', 'Restaurant'), ('Activity', 'Activity'),('Other', 'Other')])
    OtherBusType = StringField('Alternative Business type', validators=[validators.length(max=100)])
    StreetName = StringField('Street Name and number',validators=[validators.length(max=100)])
    location = SelectField('City or town', choices=[('maputo', 'maputo'), ('tofo', 'tofo'), ('Vilankulos', 'Vilanikulos'),('Pomene', 'Pomene'),
    ('Cabo Delgado','CaboDelgado'),('Inhassoro', 'Inhassoro'),('Other', 'Other')])
    PostCode = StringField('PostCode', validators=[validators.length(max=100)])
    Profile = StringField('Brief description', widget=TextArea())
    email = StringField('Email Address', validators=[validators.length(max=100)])
    OpHoursStart = StringField('Opens', validators=[validators.length(max=10)])
    OpHoursEnd = StringField('Closes', validators=[validators.length(max=10)])
    submit = SubmitField('Submit')
    def __init__(self, arg):
        super(BusRegForm, self).__init__()
        self.arg = arg