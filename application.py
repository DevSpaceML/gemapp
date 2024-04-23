from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import Form, StringField, SubmitField,SelectField, validators
from wtforms.widgets import TextArea
from flask_bootstrap import Bootstrap5
import mysql.connector
from  busreg import BusRegForm

application = app = Flask(__name__, template_folder='templates',static_folder='static')
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'
csrf = CSRFProtect(app)

@app.route("/")
def main():
	return render_template('hometpl.html')
@app.route("/activities")
def activities():
	return render_template('activities.html')
@app.route("/gemdata")
def gemdata():
	data = mysql.connector.connect(
		host = "localhost",
		user = "root",
		password = "M0y0nd!zv0!",
		database = "allsocialdata" 
		)
	searchterm = "ambience"
	elements = 0
	results = []
	DbCursor = data.cursor(dictionary=True)
	gemsql =  "select user_ScreenName,user_FollowersCount,hashtagquery,tweet_Text from twitter where tweet_Text LIKE '%"+searchterm+"%'"
	DbCursor.execute(gemsql)

	for i in DbCursor:
		results.append(i)
		elements = elements + 1 
	return render_template('gemdata.html', elements = elements, dataset = results)	
@app.route("/accomodation")
def stays():
	return render_template('accomodation.html')
@app.route("/register", methods=['GET','POST'])
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
			if cols[x] is none:
				pass
			else:
				columns.slice(cols[x]+',')

		print(columns)		


		#for key in formdata:
		print('columns are ',cols);
		print('values  are ',vals);

		''' lindoDb = mysql.connector.connect(
		host = "localhost",
		user = "gemadmin",
		password = "g3m@dmin!",
		database = "mozdata" 
		)'''

		dbCursor = lindoDb.cursor()
		sqlStmt = "INSERT INTO venues (name,email,streetname,location,postcode,type,profile,OpStart,OpEnd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		formVals = (name,email,streetname,location,postcode,bustype,profile,OpHoursStart,OpHoursEnd)

		dbCursor.execute(sqlStmt,formVals)
		lindoDb.commit()

	else:
		print(form.errors) 
		print(message)	
		
	return render_template('regbiz.html', form=form, message=message)

	


		