import unittest, json
from view_model_create_category import ViewModelCreateCategory

class VmCreateCategoryTest(unittest.TestCase):

    def test_view_model_create_category(self):
        string = json.dumps({'name':'raum', 'detail':'Zwölf'})
        string_as_dict = json.loads(string)
        vm = ViewModelCreateCategory(string_as_dict)
        self.assertIsNone(vm.to_model())
        string_as_dict = json.loads(json.dumps({
	        "name":"Raum",
	        "details":{
		        "detail1":{
			        "name":"Bestuhlungstyp",
			        "typ":"Einfaches Textfeld",
			        "mandatory":"1",
			        "deleted":"0"
		        },
		        "detail2":{
			        "name":"Garantie bis",
			        "typ":"Datum",
			        "mandatory":"1",
			        "deleted":"1"
		        }
	        },
	        "deleted":"0"
        }))
        vm = ViewModelCreateCategory(string_as_dict)
        self.assertIsNotNone(vm.to_model())
