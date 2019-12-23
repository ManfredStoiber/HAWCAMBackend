import requests
import json


data = {
    "name": "hallo14",
    "contentDescriptions": {
        "1": {
            "name": "Bestuhlungstypalösjdfljas",
            "typ": "Einfaches Textfeldaölsdjfölasjd",
            "optionalOrMandatory": 0,
            "deleted": 0
        },
        "2": {
            "name": "Garantie bisalsdjfölas",
            "typ": "Datumaölsdjfljasd",
            "optionalOrMandatory": 0,
            "deleted": 1
        }
    },
    "deleted": 0
}

# Call local Service
responseCreateCategory = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode())
print(responseCreateCategory.text)
#responseListCategories = requests.get('http://localhost:5000/api/v1.0/listCategories')
#print(responseListCategories.text)

# Call global Services
#responseCreateCategory = requests.put('http://snirps.ddns.net:5000/api/v1.0/createCategory', json.dumps(data).encode())
#print(responseCreateCategory.text)
#responseListCategories = requests.get('http://snirps.ddns.net:5001/api/v1.0/listCategories')
#print(responseListCategories.text)

