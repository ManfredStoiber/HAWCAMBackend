import json
import unittest
from model_category import DetailArgument, CategoryDetail, Category


class ModelCategoryTest(unittest.TestCase):
    dataLong = {
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

    dataMiddle = {
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
    }

    dataShort = {
        "name": "Bestuhlungstyp",
        "typ": "Einfaches Textfeld",
        "optionalOrMandatory": 1,
        "deleted": 0
    }

    dataShort2 = {
        "name": "Format",
        "typ": "Einfaches Textfeld",
        "optionalOrMandatory": 1,
        "deleted": 0
    }

    def test_detail_argument(self):
        da = DetailArgument(self.dataShort)
        self.assertEqual(da.getTupel(), ("Bestuhlungstyp", "Einfaches Textfeld", 1, 0))

    def test_detail(self):
        d = CategoryDetail(**self.dataMiddle)
        self.assertIn(DetailArgument(self.dataShort), d.detail_list)
        self.assertNotIn(DetailArgument(self.dataShort2), d.detail_list)

    def test_category(self):
        string_as_dict = json.loads(json.dumps(self.dataLong))
        c = Category(string_as_dict["name"], string_as_dict["contentDescriptions"], string_as_dict["deleted"])
        self.assertEqual(c.getTupel(), ("Raum", 0))

