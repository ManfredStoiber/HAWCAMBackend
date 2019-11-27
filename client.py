import json
from urllib.request import urlopen

data={
	"Name":"Raum", 
	"Details":{
		"Detail1":{
			"d_name":"Bestuhlungstyp",
			"d_typ":"Einfaches Textfeld"
		},
		"Detail2":{
			"d_name":"Garantie bis",
			"d_typ":"Datum"
		}
	}
}
		
	
response=urlopen('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode())

#print(response.read().decode())
