import unittest
import uc_search
import json
import mysql.connector
from repository import Repository


class UcSearchTest(unittest.TestCase):

    def connect(self):
        connection = mysql.connector.connect(host="remotemysql.com", user="xbKMa0eIqY", passwd="wqGNkrfAkK",
                                             db="xbKMa0eIqY", connect_timeout=1000)
        return connection

    def create_test_data_in_db(self, repository):
        connection = self.connect()
        query = "Insert into category (Category_name, deleted) values (%s, %s)"
        tupel = ("UnittestVmSearchCategory", 0)
        repository.fire_sql(connection, query, True, tupel)
        query = "INSERT INTO object (object_name, object_deleted) VALUES (%s, %s)"
        tupel = ("UnittestVmSearchObject", 0)
        obj_key = repository.fire_sql(connection, query, True, tupel)
        query = "INSERT INTO object_to_category (id_object, categorie_name) VALUES (%s, %s) "
        tupel = (obj_key, "UnittestVmSearchCategory")
        repository.fire_sql(connection, query, True, tupel)
        connection.close()

    def clean(self, repository):
        repository.delete("object_to_category", "categorie_name = 'UnittestVmSearchCategory'")
        repository.delete("category", "Category_name = 'UnittestVmSearchCategory'")
        repository.delete("object", "object_name = 'UnittestVmSearchObject'")

    def test_uc_search(self):
        repository = Repository(model=None, uc="search")
        self.create_test_data_in_db(repository)
        content = {"search": "'UnittestVmSearch'"}
        result = uc_search.search(content)
        self.clean(repository)
        self.assertEqual(result, json.dumps({"categories": [{"name": "UnittestVmSearchCategory"}],
                                             "objects": [{"name": "UnittestVmSearchObject", "cat": "UnittestVmSearchCategory"}]}))
