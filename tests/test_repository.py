import unittest
from repository import Repository


class RepositoryTest(unittest.TestCase):

    def test_repository(self):
        r = Repository("test", "createCategory")
        check = r.connect_with_db()
        self.assertEqual(check, False)