#gem db class
import mysql.connector

class GemDB:
	#initialise db access with auth and name of database

	def __init__(self,host,user,password,database):
		self.host = "localhost"
		self.user = "root"
		self.password = ""
		self.database = "tiyeni"

		self.conn = mysql.connector(self.host,self.user,self.password,self.database)
		dbCursor = self.conn.cursor(dictionary = True)
		
		return dbCursor 
	
	# prep values for sqlstmt
	# function stmtPrep(formvals)
	
	'''
	def dbinsert(cols,vals):
		# create sql stmt string using supplied columns and values
		try:
			INSERT INTO tableName (col1,col2...colN) VALUES (var1,var2...varN)
			*return sqlmessage
		except:
			*errormsg = error
			*print(f"The following error occured : errormsg") 		
	'''

	#update


	#delete

	# Tofo Data
	tofo_beach = {
		"Kumba Lodge": {
			"name": "Kumba Lodge",
			"location": "Tofo Beach, Mozambique",
			"email": "stay@kumbalodge.com",
			"tel": "+258 85 677 8433",
			"style": "Eco‑friendly beachfront retreat – minimalist sea‑view bungalows, wellness/yoga focus",
			"descrip": "Infinity pool, health‑food restaurant, yoga studio; activities include diving, snorkeling, surfing, horseback‑riding, ocean safaris.",
			"stars": "4.9 (Booking.com 9.1/10)",
			"gpspoint": "-23.84129, 35.53817",
			"source": "https://www.kumbalodge.com/"
		},
		"Casa na Praia Tofo": {
			"name": "Casa na Praia Tofo",
			"location": "Tofo Beach, Mozambique",
			"email": None,
			"tel": "+258 84 927 8517",
			"style": "Beachfront lodge – sea‑view suites & bungalows with African‑inspired decor",
			"descrip": "Ocean‑front accommodation, restaurant, private beach, spa/massage, free Wi‑Fi; activities include snorkeling, diving, whale watching, fishing, canoeing & horseback riding.",
			"stars": "7.8–8.1 Good (Booking.com)",
			"gpspoint": "-23.85456, 35.5485",
			"source": "https://www.casanapraiatofo.com/"
		},
		"Mango Beach Resort": {
			"name": "Mango Beach Resort",
			"location": "Tofo Beach, Mozambique",
			"email": None,
			"tel": None,
			"style": "Family‑friendly beachfront resort with pool & bar",
			"descrip": "Beachfront property with pool, fitness center, private tidal pool; restaurant serving Indian/Italian/Mediterranean/local cuisine; activities include hiking, snorkeling, boating.",
			"stars": "9.0+ (Booking.com 9/10; Tripadvisor 4.9/5)",
			"gpspoint": None,
			"source": "https://www.booking.com/hotel/mz/mango-beach-lodge.html"
		},
		"Lehani Beach Hostel": {
			"name": "Lehani Beach Hostel",
			"location": "Tofo Beach, Mozambique",
			"email": None,
			"tel": None,
			"style": "Laid‑back beachfront hostel – social vibe",
			"descrip": "Hostel with pool, bar, terrace, beachfront access; highly praised for atmosphere and staff.",
			"stars": "9.1 Excellent (Booking.com)",
			"gpspoint": None,
			"source": "https://www.booking.com/city/mz/praia-do-tofo.html"
		},
		"Baia Sonambula": {
			"name": "Baia Sonambula Beach Hotel",
			"location": "Tofo Beach, Mozambique",
			"email": None,
			"tel": None,
			"style": "Boutique beachfront guesthouse",
			"descrip": "Beachfront guesthouse with pool, private terrace; complimentary breakfast and coffee.",
			"stars": "9.3 Wonderful (Booking.com)",
			"gpspoint": None,
			"source": "https://www.booking.com/beach/city/mz/praia-do-tofo.html"
		}
	}


	# instagram_data function to gather data from Insta profiles and add to tiyeni db

	def accom_data(dataobj):
		#check for db conn

		#instadata dict object
		for k in dataobj:
		    print(k)
	        cols = dataobj.keys()
		    vals = dataobj.values()

		#self.dbinsert(cols,vals)


			