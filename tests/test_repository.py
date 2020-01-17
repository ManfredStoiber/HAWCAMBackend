import unittest, json
from random import *
from repository import Repository
from view_model_create_category import ViewModelCreateCategory
from view_model_list_attributes import VmListAttributes


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

    data2 = {"catName": "'Raum'"}
    test_set = [('det3', 'date', 1), ('det2', 'number', 1), ('det1', 'textfield', 0), ('det4', 'dateAndTime', 0)]

    def test_repository(self):
        string = json.dumps(self.data)
        string_as_dict = json.loads(string)
        view = ViewModelCreateCategory(string_as_dict)
        r0 = Repository(view.to_model(), "createCategory")
        self.assertIsNone(r0.connect_with_db())
        self.assertIsNone(r0.delete("category_to_attribute", "category_name='Category" + str(self.counter) + "'"))
        self.assertIsNone(r0.delete("category", "Category_name='Category" + str(self.counter) + "'"))
        r1 = Repository("test", "createCategory")
        with self.assertRaises(AttributeError): r1.connect_with_db()
        r2 = Repository(model=None, uc="listCategories")
        self.assertNotEqual(r2.connect_with_db(), None)
        # restliche Code-Zeilen von repository.py nicht sinnvoll testbar, da dafür z.B. Datenbank unerreichbar sein müsste

    def test_repository_search(self):
        repository = Repository(model=None, uc="search")
        result = repository.connect_with_db("'DieseSucheIstNichtErfolgreich'")
        self.assertEqual(result, [])

    def test_repository_list_attributes(self):
        vm = VmListAttributes('Raum')
        repo = Repository(self.data2, "listAttributes")
        self.assertEqual(repo.connect_with_db("'Raum'"),
                         [('det3', 'date', 1), ('det2', 'number', 1), ('det1', 'textfield', 0),
                          ('det4', 'dateAndTime', 0)])

    def test_repository_list_attributes(self):
        vm = VmListAttributes('')
        repo = Repository(self.data2, "listAttributes")
        self.assertEqual(repo.connect_with_db("''"), [])  # st das wirklich sinnvoll?
