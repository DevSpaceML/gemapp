import mysql.connector

#name,location,type,address,contactNum,email,hours,descrip,imgUrl,bkngUrl

lindoDb = mysql.connector.connect(
		host = "localhost",
		user = "gemadmin",
		password = "g3m@dmin!",
		database = "mozdata"
	)

dbCursor = lindoDb.cursor()

sqlStmt = "INSERT INTO entity (name,email,location,bustype,otherbustype,address,OpHoursStart,OpHoursEnd) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

formVals = ('form.name','form.email','form.location','form.BusType','form.OtherBusType','form.address','form.OpHoursStart','form.OpHoursEnd')

dbCursor.execute(sqlStmt,formVals)
lindoDb.commit()



	