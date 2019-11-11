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
