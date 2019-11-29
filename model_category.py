class DetailArgument:
	def __init__(self, y):	
		self.name = y["name"]
		self.typ = y["typ"]
		self.mandatory = y["mandatory"]
		self.deleted = y["deleted"]

	def __str__(self):
		return "Name = " + str(self.name) + ", Typ = " + str(self.typ) + ", Pflichtfeld = " + str(self.mandatory) + ", geloescht = " + str(self.deleted)

	def getTupel(self):
		return (self.name, self.typ, self.mandatory, self.deleted)


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
	def __init__(self, name, details, deleted):
		self.name = name
		self.details = CategoryDetail(**details)
		self.deleted = deleted

	def __str__(self):
		return "Kategoriename = " + str(self.name) + ", Kategoriedetails: " + str(self.details)

	def getTupel(self):
		return (self.name, self.deleted)