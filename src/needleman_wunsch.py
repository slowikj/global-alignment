from typing import Dict, Tuple, Set


class NeedlemanWunschParamsValidator(object):

    def __init__(self):
        self.obligatory_keys = {
            "GAP_PENALTY",
            "SAME",
            "DIFF",
            "MAX_SEQ_LENGTH",
            "MAX_NUMBER_PATHS"
        }

    def validate_config(self, config: Dict[str, int]) -> Tuple[bool, Set[str], Set[str]]:
        keys = config.keys()
        return (
            keys == self.obligatory_keys,
            self.obligatory_keys - keys,
            set(keys) - self.obligatory_keys
        )

    @staticmethod
    def validate_sequence(sequence: str, max_sequence_length: int) -> bool:
        return len(sequence) <= max_sequence_length

