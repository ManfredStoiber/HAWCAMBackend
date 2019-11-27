class DetailArgument:
	def __init__(self, y):	
		self.d_name = y["d_name"]
		self.d_typ = y["d_typ"]
	def __str__(self):
		return "Name = " + str(self.d_name) + ", Typ = " + str(self.d_typ)


class CategoryDetail:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		self.detail_list = [None] * len(self.__dict__)
		i = 0
		for x, y in self.__dict__.items():
			if i < (len(self.__dict__)-1):
				#print(x)
				self.detail_list[i] = DetailArgument(y)
				#print(self.detail_list[i])
				i = i + 1
	def __str__(self):
		temp = "\n"
		for x in self.detail_list:
			temp += str(x) + "\n"
		return temp


class Category:	
	def __init__(self, name, details):
		self.name = name
		self.details = CategoryDetail(**details)
	def __str__(self):
		return "Kategoriename = " + str(self.name) + ", Kategoriedetails: " + str(self.details)