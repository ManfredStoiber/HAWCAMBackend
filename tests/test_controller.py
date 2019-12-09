import unittest, json
from client import call_uc_create_category
from client import app
from flask import jsonify

class ControllerTest(unittest.TestCase):

    data=[{
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
    }]

    def test_uc_call(self):
        app.testing = True
        client = app.test_client()
        response = client.post("/api/v1.0/createCategory", json=data)
        json_data = response.get_json()
        self.assertEqual(json_data, jsonify(data))


    if __name__ == "__main__":
        unittest.main()