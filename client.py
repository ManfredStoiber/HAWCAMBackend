import requests
import json


data = {
    "name": "hallo13",
    "contentDescriptions": {
        "1": {
            "name": "Bestuhlungstyp",
            "typ": "Einfaches Textfeld",
            "optionalOrMandatory": "1",
            "deleted": "0"
        },
        "2": {
            "name": "Garantie bis",
            "typ": "Datum",
            "optionalOrMandatory": "1",
            "deleted": "1"
        }
    },
    "deleted": "0"
}

# Call local Service
responseCreateCategory = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode())
#print(responseCreateCategory.text)

# Call global Services
#responseCreateCategory = requests.put('http://snirps.ddns.net:5000/api/v1.0/createCategory', json.dumps(data).encode())
#responseListCategories = requests.get('http://snirps.ddns.net:5000/api/v1.0/listCategories')
#print(responseListCategories.text)

