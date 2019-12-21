import unittest, json
from view_model_create_category import ViewModelCreateCategory


class VmCreateCategoryTest(unittest.TestCase):

    def test_view_model_create_category(self):
        string = json.dumps({'name': 'raum', 'detail': 'Zwölf'})
        string_as_dict = json.loads(string)
        vm = ViewModelCreateCategory(string_as_dict)
        with self.assertRaises(Exception): vm.to_model()
        string_as_dict = json.loads(json.dumps({
            "name": "Raum",
            "contentDescriptions": {
                "1": {
                    "name": "Bestuhlungstyp",
                    "typ": "Einfaches Textfeld",
                    "optionalOrMandatory": "1",
                    "deleted": "0"
                },
                "2": {
                    "name": "Garantie bis",
                    "typ": "Datum",
                    "optionalOrMandatory": "1",
                    "deleted": "1"
                }
            },
            "deleted": "0"
        }))
        vm = ViewModelCreateCategory(string_as_dict)
        self.assertIsNotNone(vm.to_model())
