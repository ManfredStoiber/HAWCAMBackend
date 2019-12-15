import unittest
from repository import Repository


class RepositoryTest(unittest.TestCase):

    def test_repository(self):
        r = Repository("test", "createCategory")
        check = r.transmit_model_to_repository()
        self.assertEqual(check, False)