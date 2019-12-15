import unittest, json
from uc_create_category import create_category

class UcCreateCategoryTest(unittest.TestCase):

    data_true = {
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

    data_false = {
        "name":"Raum",
        "bezeichnung": False
    }

    def test_create_category(self):
        self.assertEqual(create_category(self.data_true), True)
        self.assertEqual(create_category(self.data_false), False)