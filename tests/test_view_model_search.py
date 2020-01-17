import unittest, json, mysql.connector
from view_model_search import ViewModelSearch
from repository import Repository


class VmSearch(unittest.TestCase):

    def connect(self):
        connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                             db="xbKMa0eIqY", connect_timeout=1000)
        return connection

    def create_test_data_in_db(self, repository):
        connection = self.connect()
        query = "Insert into category (Category_name, deleted) values (%s)"
        tupel = ("'UnittestVmSearchCategory'", 0)
        repository.fire_sql(connection, query, True, tupel)
        query = "INSERT INTO object (object_name, object_deleted) VALUES (%s)"
        tupel = ("'UnittestVmSearchObject'", 0)
        repository.fire_sql(connection, query, True, tupel)
        connection.close()

    def clean(self, repository):
        repository.delete("category", "Category_name = 'UnittestVmSearchCategory'")
        repository.delete("object", "object_name = 'UnittestVmSearchObject'")

    def get_test_set(self):
        repository = Repository(model=None, uc="search")
        self.create_test_data_in_db(repository)
        search_pattern = "UnittestVmSearch"
        result = repository.connect_with_db(search_pattern)
        self.clean(repository)
        return result

    def test_view_model_search_empty_set(self):
        test_set = {}
        vm = ViewModelSearch(test_set)
        result = vm.create_json()
        self.assertEqual(result, json.dumps({"categories": [], "objects": []}))

    def test_view_model_search_filled_set(self):
        test_set = self.get_test_set()
        vm = ViewModelSearch(test_set)
        result = vm.create_json()
        self.assertEqual(result, json.dumps({"categories": [{"name": "UnittestVmSearchCategory"}],
                                             "objects": [{"name": "UnittestVmSearchObject"}]}))
