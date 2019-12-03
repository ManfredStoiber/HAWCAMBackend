import requests
import json
from urllib.request import urlopen

data={
	"name":"Raum", 
	"details":{
		"detail":{
			"name":"Bestuhlungstyp",
			"typ":"Einfaches Textfeld",
			"mandatory":"1",
			"deleted":"0"
		},
		"detail":{
			"name":"Garantie bis",
			"typ":"Datum",
			"mandatory":"1",
			"deleted":"1"
		}
	},
	"deleted":"0"
}

headers = {"Content-Type": "application/json"}
		
response = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode()) 
	

#print(response.read().decode())
