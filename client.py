import requests
import json


data = {
    "name": "Raum",
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
print(responseCreateCategory.text)

# Call global Services
# responseCreateCategory = requests.put('http://192.168.0.14:5000/api/v1.0/createCategory', json.dumps(data).encode())
# responseListCategories = requests.get('http://95.90.220.121:5000/api/v1.0/listCategories')
# print(responseListCategories)

