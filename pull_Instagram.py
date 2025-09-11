import instaloader
import mysql.connector
import logging

#logging.basicConfig(level=logging.DEBUG)

# Set all logging messages to output to console
#L = instaloader.Instaloader()

#username = "shamisobeach"
#password = "F@lc0nC0ll3g3!"

# Maintain stack of instagram accounts to circumvent rate limits. track time of call and create variable, 
# nextAvailableCall
'''
try:
    L.load_session_from_file(username)
except FileNotFoundError:
    L.login(username, password)
    L.save_session_to_file()

if not L.context.is_logged_in:
    raise Exception("Login Failed")

profile = instaloader.Profile.from_username(L.context, "fatimas.nest_tofo")

for post in profile.get_posts(): 
    print(post)
    print('-----------------------------')

'''

def dbConnect():
    #connect to local mysql
    dbconn = mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password =  "",
        database = "tiyeni"
    )

    return dbconn


    #insert into mysql

	# Tofo Data
inhambane = {
    "Various Inhambane Accommodations": {
        "name": "Inhambane Region Beach Lodges",
        "location": "Inhambane Province, Mozambique",
        "email": "-",
        "tel": "-",
        "style": "Traditional coastal accommodations",
        "descrip": "Historic coastal region with various accommodation options, gateway to southern Mozambique beaches, rich cultural heritage",
        "stars": "Regional accommodations",
        "gpspoint": "-",
        "image": "https://www.mozambiqueislands.com/wp-content/uploads/2020/05/inhambane-region-beach.jpg",
        "source": "https://www.mozambiqueislands.com/resorts/"
    },
    "Bibo Sands": {
        "name": "Bibo Sands",
        "location": "Inhambane Province, Mozambique",
        "email": "-",
        "tel": "-",
        "style": "Affordable beachfront accommodation",
        "descrip": "Reasonable and affordable priced place with excellent value, great hosts William and his wife, highly recommended by guests who return frequently",
        "stars": "Highly rated Airbnb",
        "gpspoint": "-",
        "image": "https://a0.muscache.com/im/pictures/miso/Hosting-28456731/original/c4b7d8e9-2f3a-4b5c-9d6e-7f8a9b0c1d2e.jpeg",
        "source": "https://www.airbnb.com/mozambique/stays/vacation-homes"
    },
    "Barra Beach Cottage": {
        "name": "Barra Beach Cottage",
        "location": "Barra Beach area, Inhambane Province, Mozambique",
        "email": "-",
        "tel": "-",
        "style": "Rustic cottage with heavenly views",
        "descrip": "Airy cottage with rustic charm accessible by 4x4 with heavenly view, spacious and well-kitted for couple on palm tree-lined dune, best view of Barra Beach, ironwood chairs and breakfast table to gaze on the reef",
        "stars": "Airbnb unique stay",
        "gpspoint": "-",
        "image": "https://a0.muscache.com/im/pictures/miso/Hosting-46523891/original/e7f8a9b0-3c4d-5e6f-9a8b-1c2d3e4f5a6b.jpeg",
        "source": "https://www.airbnb.com/inhambane-province-mozambique/stays"
    },
    "Mozambique Beach Resort House": {
        "name": "Mozambique Beach Resort House",
        "location": "Inhambane Province, Mozambique",
        "email": "-",
        "tel": "-",
        "style": "Self catering 3 bedroom house in scenic resort",
        "descrip": "Self catering 3 bedroom house, sleep 6 guests, uncapped WiFi available, scenic area with spectacular 180 degree views of pristine beaches, reef running parallel to beach for fishing, snorkeling and tubing available",
        "stars": "Airbnb beach house",
        "gpspoint": "-",
        "image": "https://a0.muscache.com/im/pictures/miso/Hosting-39547821/original/d8e9f0a1-4b5c-6d7e-9f8a-2b3c4d5e6f7a.jpeg",
        "source": "https://www.airbnb.com/mozambique/stays"
    }
}

# instagram_data function to gather data from Insta profiles and add to tiyeni db

def accom_data(dataobj):
	#check for db conn, do insert, close db conn
    dbConn = dbConnect()
    dbcursor = dbConn.cursor()

	#instadata dict object
    for prop in dataobj:    
      cols = ','.join(list(dataobj[prop].keys()))
      vals = list(dataobj[prop].values())
      placeholders = ','.join(['%s'] * len(vals))
 
      print(cols)
      print(vals)  
      print("----- * ----- * -----")

      sql_ins_stmt = f"insert into accomz ({cols}) VALUES({placeholders})"
      print(sql_ins_stmt)
      dbcursor.execute(sql_ins_stmt, vals)
      dbConn.commit()

accom_data()
    


