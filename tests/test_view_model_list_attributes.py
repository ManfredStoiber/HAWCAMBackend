import unittest, json
from view_model_list_attributes import VmListAttributes


class VmListAttributesTest(unittest.TestCase):

    def test_view_model_list_attributes(self):
        test_set = [('det3', 'date', 1), ('det2', 'number', 1), ('det1', 'textfield', 0), ('det4', 'dateAndTime', 0)]
        vm = VmListAttributes(test_set)
        self.assertEqual(vm.create_json("'Raum'"), json.dumps({"name": "Raum", "attributes": [
            {"name": "det1", "typ": "textfield", "mandatory": 0}, {"name": "det2", "typ": "number", "mandatory": 1},
            {"name": "det3", "typ": "date", "mandatory": 1}, {"name": "det4", "typ": "dateAndTime", "mandatory": 0}]}))
        # warumm "'Raum'"
