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

    data2 = {"catName": "'Raum'"}

    def create_app(self):
        self.app = controller.app.test_client()
        app.config['TESTING'] = True

    def test_server_is_up_and_running_create_category(self):
        self.create_app()
        response = requests.put("http://snirps.ddns.net:5001/api/v1.0/createCategory", json.dumps(self.data).encode())
        self.assertEqual(response.status_code, 200)
    
    def test_server_is_up_and_running_list_category(self):
        response = urllib.request.urlopen("http://snirps.ddns.net:5001/api/v1.0/listCategories")
        self.assertEqual(response.code, 200)

    def test_server_is_up_and_running_list_attributes(self):
        self.create_app()
        response = requests.put('http://snirps.ddns.net:5001/api/v1.0/listAttributesForCategory', json.dumps(self.data2).encode())
        self.assertEqual(response.status_code, 200)

    def test_server_is_up_and_running_search(self):
        self.create_app()
        response = requests.put('http://snirps.ddns.net:5001/api/v1.0/search', json.dumps({"search": "'Raum'"}).encode())
        self.assertEqual(response.status_code, 200)

    def test_server_is_up_and_running_list_object_details(self):
        self.create_app()
        response = requests.put('http://snirps.ddns.net:5001/api/v1.0/listObjectDetails', json.dumps({"objName": "'R123'"}).encode())
        self.assertEqual(response.status_code, 200)

    def test_server_is_up_and_running_edit_object(self):
        self.create_app()
        response = requests.put('http://snirps.ddns.net:5001/api/v1.0/editObject', json.dumps({"bla": "bla"}).encode())
        self.assertEqual(response.status_code, 200)

    def test_server_is_up_and_running_edit_category(self):
        self.create_app()
        response = requests.put('http://snirps.ddns.net:5001/api/v1.0/editCategory', json.dumps({"bla": "bla"}).encode())
        self.assertEqual(response.status_code, 200)

    def test_server_is_up_and_running_invalid(self):
        self.create_app()
        response = requests.put('http://snirps.ddns.net:5001/api/v1.0/invalidURL', json.dumps(self.data2).encode())
        self.assertEqual(response.status_code, 405)
        
    if __name__ == "__main__":
        unittest.main()
