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
        self.assertEqual(da.get_tuple(), ("Bestuhlungstyp", "Einfaches Textfeld", 1, 0))

    def test_detail(self):
        d = CategoryDetail(**self.dataMiddle)
        if self.compareDetailArgument(DetailArgument(self.dataShort), d.detail_list[0]) is False and \
                self.compareDetailArgument(DetailArgument(self.dataShort), d.detail_list[1]) is False:
            raise AssertionError
        if self.compareDetailArgument(DetailArgument(self.dataShort2), d.detail_list[0]) is True or \
                self.compareDetailArgument(DetailArgument(self.dataShort2), d.detail_list[1]) is True:
            raise AssertionError

    def test_category(self):
        string_as_dict = json.loads(json.dumps(self.dataLong))
        c = Category(string_as_dict["name"], string_as_dict["contentDescriptions"], string_as_dict["deleted"])
        self.assertEqual(c.get_tuple(), ("Raum", 0))

    def compareDetailArgument(self, obj1, obj2):
        if obj1.name != obj2.name or obj1.typ != obj2.typ or obj1.mandatory != obj2.mandatory or \
                obj1.deleted != obj2.deleted:
            return False
        return True
