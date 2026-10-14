from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import Form, StringField, SubmitField,SelectField, validators
from wtforms.widgets import TextArea
from flask_bootstrap import Bootstrap5
import pietest as dbtest
from  busreg import BusRegForm
from eventsform import EventsForm

application = app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
csrf = CSRFProtect(app)

@app.route("/")
def main():
	return render_template('hometpl.html')

@app.route("/activities")
def activities():
	
	return render_template('activities.html')

@app.route("/accomodation")
def accomodation():
	
	results = dbtest.accommodation_data('mozambique', 'tofo', 'style','beach')
	data = results['data']

	return render_template('accomodation.html', dataset = data)

@app.route("/admin/newevent",  methods=['GET','POST'])
def newevent():
    message = " "
    columns = ''
    placeholders = ''
    values = []
    form = EventsForm(FlaskForm)

    if form.validate_on_submit():
        formdata = request.form
        
        valid_data = {k:v for k,v in formdata.items()
					  if v and k not in ['csrf_token', 'submit']}
		
        if valid_data:
            columns = ','.join(valid_data.keys())
            placeholders = ','.join(['%s'] * len(valid_data.keys())) 
            values = list(valid_data.values())
            
            print(values)
            ins_event = f"INSERT INTO EVENTS ({columns}) VALUES({placeholders})"

            print(ins_event)
               
            with database.get_db_conn() as db_conn:
                db_cursor = db_conn.cursor()
                db_cursor.execute(ins_event, values)		
			
    else:
         print(values)
         print(columns)				
                
    return render_template('admin_events.html', form=form, message=message)

@app.route("/admin/register", methods=['GET','POST'])
def register():
	message = " "
	columns = None
	form = BusRegForm(FlaskForm)

	if form.validate_on_submit():
		formdata = request.form
		cols = list(formdata.keys())
		vals = list(formdata.values())

		#Loop through and check if key is null and add to columns string if not
		for x in cols:
			if cols[x] is None:
				pass
			else:
				columns.slice(cols[x]+',')

		print(columns)		

		#for key in formdata:
		print('columns are ',cols);
		print('values  are ',vals);


		dbCursor = lindoDb.cursor()
		sqlStmt = "INSERT INTO venues (name,email,streetname,location,postcode,type,profile,OpStart,OpEnd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		formVals = (name,email,streetname,location,postcode,bustype,profile,OpHoursStart,OpHoursEnd)

		dbCursor.execute(sqlStmt,formVals)
		lindoDb.commit()

	else:
		print(form.errors) 
		print(message)	
		
	return render_template('regbiz.html', form=form, message=message)
	
if __name__ == "__main__":
	app.run()