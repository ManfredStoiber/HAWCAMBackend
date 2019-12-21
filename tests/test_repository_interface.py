import unittest
from unittest.mock import MagicMock
from repository_interface import RepositoryInterface
from view_model_create_category import ViewModelCreateCategory


class RepositoryInterfaceTest(unittest.TestCase):

    def test_repository_interface(self):
        interface = RepositoryInterface("test", "createCategory")
        self.assertEqual(interface.model, "test")
        self.assertEqual(interface.uc, "createCategory")
        self.assertNotEqual(interface.model, "hallo")
        self.assertNotEqual(interface.uc, "test")
