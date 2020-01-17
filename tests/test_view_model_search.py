import unittest, json, mysql.connector
from view_model_search import ViewModelSearch
from repository import Repository


class VmSearchTest(unittest.TestCase):

    def test_view_model_search_empty_set(self):
        test_set = {}
        vm = ViewModelSearch(test_set)
        result = vm.create_json()
        self.assertEqual(result, json.dumps({"categories": [], "objects": []}))

    def test_view_model_search_filled_set(self):
        test_set = {("UnittestVmSearchCategory",), ("UnittestVmSearchObject", "UnittestVmSearchCategory")}
        vm = ViewModelSearch(test_set)
        result = vm.create_json()
        self.assertEqual(result, json.dumps({"categories": [{"name": "UnittestVmSearchCategory"}],
                                             "objects": [{"name": "UnittestVmSearchObject", "cat": "UnittestVmSearchCategory"}]}))
