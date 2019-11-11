import unittest

from src.config_analysis import ConfigReader


class ConfigAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.config_reader = ConfigReader()

    def test_empty_config_reader_returns_empty_list(self):
        self.assertListEqual(
            self.config_reader.get_attributes(),
            []
        )

