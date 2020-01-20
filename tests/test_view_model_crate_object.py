import unittest, json
from view_model_create_object import ViewModelCreateObject


class VmCreateObjectTest(unittest.TestCase):



    def test_view_model_create_object(self):
        data3 = {
            "catName": "Raum",
            "objObjName": "2_213",
            "details": {
                "Detail1": "Nordseite",
                "Detail2": 80,
                "Detail3": "Jürgen Terpin"
            }
        }

        string = json.dumps(data3)
        string_as_dict = json.loads(string)
        vm = ViewModelCreateObject(string_as_dict)
        self.assertIsNotNone(vm.to_model())
        #with self.assertRaises(Exception): vm.to_model()
        
    def test_view_model_create_object_false(self):
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
        vm = ViewModelCreateObject(string_as_dict)
        with self.assertRaises(Exception): vm.to_model()
        #self.assertIsNotNone(vm.to_model())
