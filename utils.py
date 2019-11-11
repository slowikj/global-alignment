from typing import List


def to_string(l: List[str]) -> str:
    return "".join(l)


def prefix_reversed(seq, current_index):
    return seq[0:current_index][::-1]
