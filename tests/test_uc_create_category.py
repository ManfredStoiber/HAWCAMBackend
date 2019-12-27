import unittest, json, mysql
from uc_create_category import create_category


class UcCreateCategoryTest(unittest.TestCase):
    data_true = {
        "name": "Raum",
        "contentDescriptions": {
            "1": {
                "name": "Bestuhlungstyp",
                "typ": "Einfaches Textfeld",
                "optionalOrMandatory": 1,
                "deleted": 0
            },
            "2": {
                "name": "Garantie bis",
                "typ": "Datum",
                "optionalOrMandatory": 1,
                "deleted": 1
            }
        },
        "deleted": 0
    }

    data_false = {
        "name": "HalloHallo",
        "bezeichnung": False
    }

    def test_create_category(self):
        with self.assertRaises(mysql.connector.errors.IntegrityError): create_category(self.data_true) # Raum schon vorhanden
        with self.assertRaises(KeyError): create_category(self.data_false)
