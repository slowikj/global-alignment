import unittest

from utils import to_string, prefix_reversed


class UtilsTests(unittest.TestCase):

    def test_conversion_list_to_string(self):
        self.assertEqual(to_string(["a", "l", "a"]), "ala")

    def test_conversion_of_empty_list_to_string(self):
        self.assertEqual(to_string([]), "")

    def test_prefix_reversed(self):
        self.assertEqual(
            prefix_reversed("ala ma kota", 4),
            " ala"
        )
