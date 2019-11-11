import unittest

from src.needleman_wunsch import NeedlemanWunschParamsValidator


class NeedlemanWunschParamsValidatorTests(unittest.TestCase):

    def setUp(self):
        self.params_validator = NeedlemanWunschParamsValidator()

    def test_return_params_that_are_not_set_in_config_dict(self):
        config = {
            "GAP_PENALTY": 1,
            "SAME": 5,
            "DIFF": 5
        }

        self.assertEqual(
            self.params_validator.validate_config(config),
            (False, ["MAX_SEQUENCE_LENGTH", "MAX_NUMBER_PATHS"])
        )
