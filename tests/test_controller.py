import sys, unittest, json
# sys.path.append("..\HAWCAMBackend")
from flask import Flask, jsonify, request
from controller import app
import urllib.request
import controller


class ControllerTest(unittest.TestCase):

    def test_uc_create_category_call(self):
        with app.app_context() as ctx:
            with app.test_client() as client:
                data = {
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
                response = client.put("http://localhost:5000/api/v1.0/createCategory", json=json.dumps(data))
                json_data = response.get_json()
                # Fehlersuche, warum Flask-Api nicht erreichbar
                print("response = " + str(response))
                print("json_data = " + str(json_data))
                print("jsonify(data) = " + str(jsonify(data)))
                self.assertEqual(json_data, jsonify(data))

    def create_app(self):
        self.app = controller.app.test_client()
        app.config['TESTING'] = True

    def test_server_is_up_and_running(self):
        self.create_app()
        response = urllib.request.urlopen("http://localhost:5000/api/v1.0/listCategories")
        self.assertEqual(response.code, 200)

    if __name__ == "__main__":
        unittest.main()
