from enum import IntEnum, unique


@unique
class Direction(IntEnum):
    LEFT = 0,
    DIAGONAL = 1,
    UP = 2


class NeedlemanWunschSolver(object):

    def __init__(self, gap_penalty: int, same_cost: int, diff_cost: int):
        self.gap_penalty = gap_penalty
        self.same_cost = same_cost
        self.diff_cost = diff_cost

    def compute_cost_direction_matrices(self, a_seq: str, b_seq: str):
        len_a, len_b = len(a_seq), len(b_seq)
        cost_matrix = self.generate_initial_cost_matrix(
            a_seq_len=len_a,
            b_seq_len=len_b)
        self.__fill_cost_matrix(a_seq, b_seq, cost_matrix)
        return cost_matrix, []

    def generate_initial_cost_matrix(self, a_seq_len: int, b_seq_len: int):
        return self.__generate_matrix(
            height=a_seq_len + 1,
            width=b_seq_len + 1,
            cell_generator=self.__initial_cost_matrix_cell_generator)

    def generate_initial_directions_matrix(self, a_seq_len: int, b_seq_len: int):
        return self.__generate_matrix(
            height=a_seq_len + 1,
            width=b_seq_len + 1,
            cell_generator=lambda r, c: [])

    def __fill_cost_matrix(self, a_seq, b_seq, cost_matrix):
        cost_matrix_height, cost_matrix_width = len(cost_matrix), len(cost_matrix[0])
        for r in range(1, cost_matrix_height):
            for c in range(1, cost_matrix_width):
                self.__compute_cost_matrix_cell(cost_matrix, a_seq, b_seq, r, c)

    def __compute_cost_matrix_cell(self, cost_matrix, a_seq, b_seq, r, c):
        cost_matrix[r][c] = max(
            cost_matrix[r][c - 1] + self.gap_penalty,
            cost_matrix[r - 1][c - 1] + self.__item_comparison_cost(a_seq[r - 1], b_seq[c - 1]),
            cost_matrix[r - 1][c] + self.gap_penalty)

    def __item_comparison_cost(self, a, b):
        return self.same_cost if a == b else self.diff_cost

    @staticmethod
    def __generate_matrix(height: int, width: int, cell_generator):
        return [
            [cell_generator(r, c) for c in range(width)]
            for r in range(height)
        ]

    def __initial_cost_matrix_cell_generator(self, row: int, col: int):
        if row == 0 or col == 0:
            return max(row, col) * self.gap_penalty
        else:
            return 0
