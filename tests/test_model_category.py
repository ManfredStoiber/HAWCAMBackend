import json
import unittest
from model_category import DetailArgument, CategoryDetail, Category


class ModelCategoryTest(unittest.TestCase):
    dataLong = {
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

    dataMiddle = {
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
    }

    dataShort = {
        "name": "Bestuhlungstyp",
        "typ": "Einfaches Textfeld",
        "mandatory": "1",
        "deleted": "0"
    }

    def test_detail_argument(self):
        da = DetailArgument(self.dataShort)
        self.assertEqual(da.getTupel(), ("Bestuhlungstyp", "Einfaches Textfeld", "1", "0"))
        #self.assertEqual(str(da), "Name = Bestuhlungstyp, Typ = Einfaches Textfeld, Pflichtfeld = 1, geloescht = 0")

    #def test_detail(self):
    #    d = CategoryDetail(json.loads(json.dumps(self.dataMiddle)))
    #    self.assertEqual(str(d), "Name = Bestuhlungstyp, Typ = Einfaches Textfeld, Pflichtfeld = 1, geloescht = "
    #                             "0\nName = Garantie bis, Typ = Datum, Pflichtfeld = 1, geloescht = 1\n")

    def test_category(self):
        string_as_dict = json.loads(json.dumps(self.dataLong))
        c = Category(string_as_dict["name"], string_as_dict["details"], string_as_dict["deleted"])
        self.assertEqual(c.getTupel(), ("Raum", "0"))
        #self.assertEqual(str(c), "Kategoriename: Raum, "
        #                         "Kategoriedetails: Name = Bestuhlungstyp, Typ = Einfaches Textfeld, Pflichtfeld = 1, "
        #                         "geloescht = 0\nName = Garantie bis, Typ = Datum, Pflichtfeld = 1, geloescht = 1\n, "
        #                         "Kategorie geloescht: 0")
