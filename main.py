from typing import Dict, Tuple, Set
import sys
import getopt

from config_analysis import IntConfigReader
from solver import NeedlemanWunschSolver, CellCostComputer


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


def read_sequence_from_fasta(file_path: str) -> str:
    with open(file_path, "r") as f:
        res = ""
        f.readline()  # we are not interested in the first line
        for line in f:
            res += line
        return res


def read_config(file_path: str) -> Dict[str, int]:
    with open(file_path, "r") as f:
        config_reader = IntConfigReader()
        for line in f:
            config_reader.add_line(line)
        return config_reader.get_attributes()


def extract_config(file_path: str) -> Dict[str, int]:
    try:
        res = read_config(file_path)
    except ValueError:
        print("config file is invalid. Line format should be: KEY INT_VALUE")
        sys.exit(2)
    config_validation_status, missing_params, redundant_params = NeedlemanWunschParamsValidator() \
        .validate_config(res)
    if not config_validation_status:
        print("config file is invalid: \n")
        print("missing params: {}".format(missing_params))
        print("redundant params: {}".format(redundant_params))
        sys.exit(2)
    return res


def extract_params(options):
    for opt, value in options:
        if opt == '-a':
            a = read_sequence_from_fasta(value)
        elif opt == "-b":
            b = read_sequence_from_fasta(value)
        elif opt == "-c":
            conf = extract_config(value)
        elif opt == "-o":
            out_path = value
    return a, b, conf, out_path


def get_alignments(config: Dict[str, int], seq_a: str, seq_b: str):
    solver = NeedlemanWunschSolver(CellCostComputer(
        same_cost=config["SAME"],
        diff_cost=config["DIFF"],
        gap_penalty=config["GAP_PENALTY"]
    ))
    return solver.generate_alignments(seq_a, seq_b, config["MAX_NUMBER_PATHS"])


def compute_and_save_alignments(config: Dict[str, int], seq_a: str, seq_b: str, output_path: str):
    score, alignments = get_alignments(config, seq_a, seq_b)
    with open(output_path, "w") as output:
        output.write("SCORE = {}\n\n".format(score))
        for alignment in alignments:
            output.write("{}\n{}\n\n".format(alignment[0], alignment[1]))


def raise_value_error_if_arg_is_missing(opts):
    if set(map(lambda x: x[0][1:], opts)) != {"a", "b", "c", "o"}:
        raise ValueError()


if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        opts, _ = getopt.getopt(args, "a:b:c:o:")
        raise_value_error_if_arg_is_missing(opts)
    except (ValueError, getopt.GetoptError):
        print("usage: python -m main.py -a seq1.txt -b seq2.txt -c config.txt -o output.txt")
        sys.exit(2)

    seq_a, seq_b, config, output_path = extract_params(opts)

    if all(map(lambda seq: NeedlemanWunschParamsValidator().validate_sequence(seq, config["MAX_SEQ_LENGTH"]),
               [seq_a, seq_b])):
        compute_and_save_alignments(config, seq_a, seq_b, output_path)
    else:
        print("at least one sequence is too long")
