import requests
import json

data = {
    "name": "Raum",
    "contentDescriptions": {
        "1": {
            "name": "Bestuhlungstyp",
            "typ": "Einfaches Textfeld",
            "optionalOrMandatory": 0,
            "deleted": 0
        },
        "2": {
            "name": "Garantie bis",
            "typ": "Datum",
            "optionalOrMandatory": 0,
            "deleted": 1
        },
        "3": {
            "name": "Stuhlform",
            "typ": "Einfaches Textfeld",
            "optionalOrMandatory": 0,
            "deleted": 1
        }
    },
    "deleted": 0
}

data2 = {"catName": "'Raum'"}

data3 = {
        "catName": "Raum",
        "objObjName": "2_213",
        "details": {
            "Detail1": "Nordseite",
            "Detail2": 80,
            "Detail3": "Jürgen Terpin"
        }
}

data4 = {"search": "'2_213'"}

# Call local Service
#responseCreateCategory = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode())
#print(responseCreateCategory.text)
#responseListCategories = requests.get('http://localhost:5000/api/v1.0/listCategories')
#print(responseListCategories.text)
#responseListAttributes = requests.put('http://localhost:5000/api/v1.0/listAttributesForCategory', json.dumps(data2).encode())
#print(responseListAttributes.text)
#responseCreateObject = requests.put('http://localhost:5000/api/v1.0/createObject', json.dumps(data3).encode())
#print(responseCreateObject.text)
responseSearch = requests.put('http://localhost:5000/api/v1.0/search', json.dumps(data4).encode())
print(responseSearch.text)

# Call global Services
#responseCreateCategory = requests.put('http://snirps.ddns.net:5001/api/v1.0/createCategory', json.dumps(data).encode())
#print(responseCreateCategory.content)
# responseListCategories = requests.get('http://snirps.ddns.net:5001/api/v1.0/listCategories')
# print(responseListCategories.text)
#responseListAttributes = requests.put('http://snirps.ddns.net:5001/api/v1.0/listAttributesForCategory', json.dumps(data2).encode())
#print(responseListAttributes.text)


