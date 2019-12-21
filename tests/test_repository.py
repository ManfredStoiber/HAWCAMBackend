import unittest
from repository import Repository


class RepositoryTest(unittest.TestCase):

    def test_repository(self):
        r1 = Repository("test", "createCategory")
        with self.assertRaises(AttributeError): r1.connect_with_db()

        r2 = Repository(model=None, uc="listCategories")
        self.assertNotEqual(r2.connect_with_db(), None)
