import unittest, json
from view_model_list_categories import ViewModelListCategories


class VmListCategoriesTest(unittest.TestCase):

    def test_create_json(self):
        test_set = {("Raum", 5), ("Beamer", 3)}
        vm = ViewModelListCategories(test_set)
        self.assertEqual(vm.create_json(), json.dumps({"categories": [{"name": "Beamer", "count": 3}, {"name": "Raum", "count": 5}]}))
