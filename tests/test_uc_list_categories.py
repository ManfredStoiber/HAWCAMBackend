import unittest
from uc_list_categories import list_categories


class UcListCategoriesTest(unittest.TestCase):

    def test_list_categories(self):
        self.assertIsNotNone(list_categories())
