import unittest

from src.needleman_wunsch import NeedlemanWunschConfigValidator


class NeedlemanWunschParamsValidatorTests(unittest.TestCase):

    def setUp(self):
        self.params_validator = NeedlemanWunschConfigValidator()

    def test_return_params_that_are_not_set_in_config_dict(self):
        # arrange
        config = {
            "GAP_PENALTY": 1,
            "SAME": 5,
            "DIFF": 5
        }

        # act
        validation_status, missing_params, _ = self.params_validator.validate_config(config)

        # assert
        self.assertEqual(validation_status, False)
        self.assertSetEqual(missing_params, {"MAX_SEQ_LENGTH", "MAX_NUMBER_PATHS"})

    def test_return_redundant_params_that_are_not_handled(self):
        # arrange
        config = {
            "GAP_PENALTY": 1,
            "aaa": 44
        }

        # act
        validation_status, _, redundant_params = self.params_validator.validate_config(config)

        # assert
        self.assertEqual(validation_status, False)
        self.assertSetEqual(redundant_params, {"aaa"})

    def test_validate_proper_config(self):
        # arrange
        config = {
            "GAP_PENALTY": 3,
            "SAME": 3,
            "DIFF": 3,
            "MAX_SEQ_LENGTH": 3,
            "MAX_NUMBER_PATHS": 3
        }

        # act
        validation_status, missing_params, redundant_params = self.params_validator.validate_config(config)

        # assert
        self.assertEqual(validation_status, True)
        self.assertSetEqual(missing_params, set())
        self.assertSetEqual(redundant_params, set())
