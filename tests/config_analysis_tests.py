import unittest

from src.config_analysis import IntConfigReader


class ConfigAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.config_reader = IntConfigReader()

    def test_empty_config_reader_returns_empty_list(self):
        self.assertListEqual(
            self.config_reader.get_attributes(),
            []
        )

    def test_after_add_line_returns_list_with_appropriate_key_value(self):
        # arrange
        line = "FIST_PARAM 5"
        # act
        self.config_reader.add_line(line)
        # assert
        self.assertListEqual(
            self.config_reader.get_attributes(),
            [("FIST_PARAM", 5)]
        )

    def test_add_line_with_many_spaces_raises_value_error(self):
        # arrange
        line = "FIRST_PARAM   5"
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_add_line_with_no_value_raises_value_error(self):
        # arrange
        line = "FIRST_PARAM"
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_add_line_without_key_raises_value_error(self):
        # arrange
        line = "5"
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_add_line_with_key_and_space_raises_value_error(self):
        # arrange
        line = "PARAM "
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_add_line_with_key_and_spaces_raises_value_error(self):
        # arrange
        line = "PARAM    "
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_add_line_with_too_many_values_raises_value_error(self):
        # arrange
        line = "PARAM 54 55 P"
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_add_line_with_not_integer_value_raises_value_error(self):
        # arrange
        line = "PARAM A"
        # act and assert
        self.assertRaises(
            ValueError,
            lambda: self.config_reader.add_line(line)
        )

    def test_adding_two_valid_lines_gives_proper_key_value_attrs_list(self):
        # arrange
        line1 = "A 1"
        line2 = "B 3"

        # act
        self.config_reader.add_line(line1)
        self.config_reader.add_line(line2)

        # assert
        self.assertListEqual(
            self.config_reader.get_attributes(),
            [("A", 1), ("B", 3)]
        )
