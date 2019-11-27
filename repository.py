import mysql.connector
from repository_interface import RepositoryInterface

class Repository(RepositoryInterface):

	def __init__(self, model, uc):
		super().__init__(model, uc)
				

	def transmit_model_to_repository(self):
		connection = mysql.connector.connect(host = "snirps.ddns.net", user = "sepdbuser", passwd = "!milchbubis19", db = "sepdb")
		if self.uc == "createCategory":
			create_category(self.model)
		elif self.uc == "...":
			print("lala")
			#...(interface.model)
		else:
			print("Nichts weiter")
		connection.close()

	def create_category(model):
		print("Category created")
		sql = "Select * FROM Categories"
	
