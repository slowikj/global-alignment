import unittest

from src.utils import to_string


class UtilsTests(unittest.TestCase):

    def test_conversion_list_to_string(self):
        self.assertEqual(to_string(["a", "l", "a"]), "ala")

    def test_conversion_of_empty_list_to_string(self):
        self.assertEqual(to_string([]), "")
