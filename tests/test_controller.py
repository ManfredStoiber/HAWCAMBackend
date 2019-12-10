import sys, unittest, json
#sys.path.append("..\HAWCAMBackend")
from flask import Flask, jsonify, request

app = Flask(__name__)

class ControllerTest(unittest.TestCase):

    def test_uc_create_category_call(self):
        with app.app_context():
            yield
        data={
            "name": "Raum",
            "details": {
                "detail1": {
                    "name": "Bestuhlungstyp",
                    "typ": "Einfaches Textfeld",
                    "mandatory": "1",
                    "deleted": "0"
                },
                "detail2": {
                    "name": "Garantie bis",
                    "typ": "Datum",
                    "mandatory": "1",
                    "deleted": "1"
                }
            },
            "deleted": "0"
        }
        app.testing = True
        client = app.test_client()
        response = client.post("/api/v1.0/createCategory", json=data)
        json_data = response.get_json()
        self.assertEqual(json_data, jsonify(data))

    def test_uc_list_categories_call(self):
        with app.app_context():
            yield
        data = {
            "categories": {
                "category1": {
                    "name": "Raum",
                    "count": 3
                },
                "category2": {
                    "name": "Buch",
                    "count": 14
                },
                "category3": {
                    "name": "Rechner",
                    "count": 10
                }
            }
        }
        client = app.test_client()
        response = client.get("/api/v1.0/listCategories")
        json_data = response.get_json()
        self.assertEqual(json_data, jsonify(data))

    if __name__ == "__main__":
        unittest.main()