import unittest, json
from random import *
from repository import Repository
from view_model_create_category import ViewModelCreateCategory


class RepositoryTest(unittest.TestCase):

    counter = randrange(10000)

    data = {
        "name": "Category" + str(counter),
        "contentDescriptions": {
            "1": {
                "name": "Bestuhlungstyp",
                "typ": "Einfaches Textfeld",
                "optionalOrMandatory": 0,
                "deleted": 0
            },
            "2": {
                "name": "Garantie bis",
                "typ": "Datum",
                "optionalOrMandatory": 0,
                "deleted": 1
            }
        },
        "deleted": 0
    }

    def test_repository(self):
        string = json.dumps(self.data)
        string_as_dict = json.loads(string)
        view = ViewModelCreateCategory(string_as_dict)
        r0 = Repository(view.to_model(), "createCategory")
        self.assertIsNone(r0.connect_with_db())
        self.assertIsNone(r0.delete("category_to_attribute", "category_name='Category"+str(self.counter)+"'"))
        self.assertIsNone(r0.delete("category", "Category_name='Category"+str(self.counter)+"'"))
        r1 = Repository("test", "createCategory")
        with self.assertRaises(AttributeError): r1.connect_with_db()
        r2 = Repository(model=None, uc="listCategories")
        self.assertNotEqual(r2.connect_with_db(), None)
        #restliche Code-Zeilen von repository.py nicht sinnvoll testbar, da dafür z.B. Datenbank unerreichbar sein müsste
