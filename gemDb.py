#gem db class
import mysql.connector

class GemDB:
	#initialise db access with auth and name of database

	dbCursor

	def __init__(self,host,user,password,database):
		self.host = "localhost"
		self.user = "root"
		self.password = "M0y0nd!zv0!"
		self.database = "allsocialdata"

		self.conn = mysql.connector(self.host,self.user,self.password,self.database)
		dbCursor = self.conn.cursor(dictionary = true)
		
		return dbCursor 




	
	#prep values for sqlstmt
	#function stmtPrep(formvals)
	

	'''
	function dbinsert(cols,vals)
		*create sql stmt string using supplied columns and values
		try
			*insert statement
			#INSERT INTO tableName (col1,col2...colN) VALUES (var1,var2...varN)
			*return success message to log
		except
			*errormsg = error
			*return errormsg		
	'''


	#update


	#delete


			