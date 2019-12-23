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

    def test_detail_argument(self):
        da = DetailArgument(self.dataShort)
        self.assertEqual(da.getTupel(), ("Bestuhlungstyp", "Einfaches Textfeld", 1, 0))

    def test_detail(self):
        d = CategoryDetail(**self.dataMiddle)
        self.assertEqual(d.detail_list[0].name, DetailArgument(self.dataShort).name)
        self.assertEqual(d.detail_list[0].typ, DetailArgument(self.dataShort).typ)
        self.assertNotEqual(d.detail_list[1].name, DetailArgument(self.dataShort).name)

    def test_category(self):
        string_as_dict = json.loads(json.dumps(self.dataLong))
        c = Category(string_as_dict["name"], string_as_dict["contentDescriptions"], string_as_dict["deleted"])
        self.assertEqual(c.getTupel(), ("Raum", 0))

