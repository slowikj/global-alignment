import unittest

from src.needleman_wunsch import NeedlemanWunschParamsValidator


class NeedlemanWunschParamsValidatorTests(unittest.TestCase):

    def setUp(self):
        self.params_validator = NeedlemanWunschParamsValidator()

    def test_return_params_that_are_not_set_in_config_dict(self):
        # arrange
        config = {
            "GAP_PENALTY": 1,
            "SAME": 5,
            "DIFF": 5
        }

        # act
        validation_status, missing_params = self.params_validator.validate_config(config)

        # assert
        self.assertEqual(validation_status, False)
        self.assertSetEqual(missing_params, {"MAX_SEQ_LENGTH", "MAX_NUMBER_PATHS"})
