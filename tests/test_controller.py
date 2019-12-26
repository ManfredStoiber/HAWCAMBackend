import sys, unittest, json
# sys.path.append("..\HAWCAMBackend")
from flask import Flask, jsonify
from controller import app
import urllib.request
import controller
import requests


class ControllerTest(unittest.TestCase):

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

    def create_app(self):
        self.app = controller.app.test_client()
        app.config['TESTING'] = True

    def test_server_is_up_and_running(self):
        self.create_app()
        response = requests.put("http://snirps.ddns.net:5001/api/v1.0/createCategory", json.dumps(self.data).encode())
        self.assertEqual(response.status_code, 200)
        response = urllib.request.urlopen("http://snirps.ddns.net:5001/api/v1.0/listCategories")
        self.assertEqual(response.code, 200)

    if __name__ == "__main__":
        unittest.main()
