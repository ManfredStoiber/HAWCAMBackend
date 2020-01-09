import unittest, json, requests
from uc_list_attributes import get_attributes



class UcListAttributesTest(unittest.TestCase):
    #sollte hier nicht ein fehler zurückkommen
    def test_list_attributes_NotInDB(self):
        self.assertIsNotNone(get_attributes({'catName': "'NotInDatabase'"}))
   
    #sollte hier nicht ein fehler zurückkommen
    def test_list_attributes_Empty(self):
        self.assertEqual(get_attributes({'catName': "''"}),json.dumps({"name": "", "attributes": []}))
   
    #sollte hier nicht ein fehler zurückkommen
    def test_list_attributes_Empty(self):
        self.assertEqual(get_attributes({'catName': "''"}),json.dumps({"name": "", "attributes": []}))
   
    #setzt vorraus dass create funktioniert und delete eigentlich auch
    # def test_list_attributes_inDB(self): 
    #     data = {
    #         "name": "TestobjektFurUnittest",
    #         "contentDescriptions": {
    #             "1": {
    #                 "name": "Bestuhlungstyp",
    #                 "typ": "Einfaches Textfeld",
    #                 "optionalOrMandatory": 0,
    #                 "deleted": 0
    #             },
    #             "2": {
    #                 "name": "Garantie bis",
    #                 "typ": "Datum",
    #                 "optionalOrMandatory": 0,
    #                 "deleted": 1
    #             },
    #             "3": {
    #                 "name": "Stuhlform",
    #                 "typ": "Einfaches Textfeld",
    #                 "optionalOrMandatory": 0,
    #                 "deleted": 1
    #             }
    #         },
    #         "deleted": 0
    #     }   
    #     responseCreateCategory = requests.put('http://localhost:5000/api/v1.0/createCategory', json.dumps(data).encode())
    #     self.assertEqual(get_attributes({'catName': "'TestobjektFurUnittest'"}),json.dumps({"name": "TestobjektFurUnittest", "attributes": [{"name": "Bestuhlungstyp", "typ": "Einfaches Textfeld", "mandatory": 0}, {"name": "Garantie bis", "typ": "Datum", "mandatory": 0}, {"name": "Stuhlform", "typ": "Einfaches Textfeld", "mandatory": 0}]}))
    #     #delete category zur zeit nicht möglich!