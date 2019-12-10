import json
from model_category import *

class ViewModelCreateCategory:

	def __init__(self, string_as_dict):
		self.dict = string_as_dict
	
	def to_model(self):
		try:
			category = Category(self.dict["name"], self.dict["details"], self.dict["deleted"])
			return category
		except:
			return None

	
	
