import requests
import json
#from urllib.request import urlopen

data={
	"name":"Raum", 
	"details":{
		"detail1":{
			"name":"Bestuhlungstyp",
			"typ":"Einfaches Textfeld",
			"mandatory":"1",
			"deleted":"0"
		},
		"detail2":{
			"name":"Garantie bis",
			"typ":"Datum",
			"mandatory":"1",
			"deleted":"1"
		}
	},
	"deleted":"0"
}

headers = {"Content-Type": "application/json"}

#responseCreateCategory = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode())
responseListCategories = requests.get('http://localhost:5000/api/v1.0/listCategories')

#print(responseCreateCategory.read().decode())
