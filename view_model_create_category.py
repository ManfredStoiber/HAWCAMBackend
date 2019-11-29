import json
from model_category import *

class ViewModelCreateCategory:

	def __init__(self, string_as_dict):
		self.dict = string_as_dict
	
	def to_model(self, data):
		return Category(data["name"], data["details"], data["deleted"])
	


	
	
