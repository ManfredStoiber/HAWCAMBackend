import mysql.connector
from repository_interface import RepositoryInterface

class Repository(RepositoryInterface):

	def __init__(self, model, uc):
		super().__init__(model, uc)
			
	
	def fire_sql(self, connection, query, tupel):
		try:
			cursor = connection.cursor(prepared=True)
			cursor.execute(query, tupel)
			connection.commit()
			result = cursor.fetchall()		
			for x in result:
 				print(x)
		except mysql.connector.Error as error:
   			print("parameterized query failed {}".format(error))
		finally:
  			if (connection.is_connected()):
        			cursor.close()
        			connection.close()


	def create_category(self, model, connection):
		print("Category created")
		sql_insert_query = "INSERT INTO Category (category_name, deleted) VALUES (%s, %s)"
		sql_insert_tupel = model.getTupel()
		self.fire_sql(connection, sql_insert_query, sql_insert_tupel)
		sql_insert_query = "INSERT INTO Attributes (name, deleted, datatype) VALUES (%s, %s, %s)"
		for detail in model.details.detail_list:
			sql_insert_tupel = detail.getTupel()
			self.fire_sql(connection, sql_insert_query, sql_insert_tupel)


	def transmit_model_to_repository(self):
		connection = mysql.connector.connect(host = "snirps.ddns.net", user = "sepdbuser", passwd = "!milchbubis19", db = "sepdb")
		if self.uc == "createCategory":
			self.create_category(self.model, connection)
		elif self.uc == "...":
			print("lala")
			#...(interface.model)
		else:
			print("Nichts weiter")
		connection.close()

	
	
