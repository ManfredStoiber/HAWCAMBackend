import requests
import json
from urllib.request import urlopen

data={
	"name":"Raum", 
	"details":{
		"detail":{
			"name":"Bestuhlungstyp",
			"typ":"Einfaches Textfeld",
			"mandatory":"ja",
			"deleted":"nein"
		},
		"detail":{
			"name":"Garantie bis",
			"typ":"Datum",
			"mandatory":"ja",
			"deleted":"ja"
		}
	},
	"deleted":"nein"
}

headers = {"Content-Type": "application/json"}
		
response = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode()) 
	

#print(response.read().decode())
