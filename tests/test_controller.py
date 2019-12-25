import sys, unittest, json
# sys.path.append("..\HAWCAMBackend")
from flask import Flask, jsonify, request
from controller import app
import urllib.request
import controller


class ControllerTest(unittest.TestCase):

    def test_uc_create_category_call(self):
        data = {
            "name": "ManfredStinkt",
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
        response = urllib.request.urlopen("http://snirps.ddns.net:5001/api/v1.0/createCategory")
        json_data = response.get_json()
        self.assertEqual(json_data, jsonify(data))

    def create_app(self):
        self.app = controller.app.test_client()
        app.config['TESTING'] = True

    def test_server_is_up_and_running(self):
        self.create_app()
        response = urllib.request.urlopen("http://snirps.ddns.net:5001/api/v1.0/listCategories")
        self.assertEqual(response.code, 200)

    if __name__ == "__main__":
        unittest.main()
