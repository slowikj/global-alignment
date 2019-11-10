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
        directions_matrix = self.generate_initial_directions_matrix(
            a_seq_len=len_a,
            b_seq_len=len_b
        )
        self.__fill_cost_and_direction_matrix(a_seq, b_seq, cost_matrix, directions_matrix)
        return cost_matrix, directions_matrix

    def generate_initial_cost_matrix(self, a_seq_len: int, b_seq_len: int):
        return self.__generate_matrix(
            height=a_seq_len + 1,
            width=b_seq_len + 1,
            cell_generator=self.__initial_cost_matrix_cell_generator
        )

    def generate_initial_directions_matrix(self, a_seq_len: int, b_seq_len: int):
        return self.__generate_matrix(
            height=a_seq_len + 1,
            width=b_seq_len + 1,
            cell_generator=lambda r, c: [])

    def __fill_cost_and_direction_matrix(self, a_seq, b_seq, cost_matrix, directions_matrix):
        matrix_height, matrix_width = len(cost_matrix), len(cost_matrix[0])
        for r in range(1, matrix_height):
            for c in range(1, matrix_width):
                costs = self.__get_neighbor_costs(cost_matrix, a_seq, b_seq, r, c)
                max_cost = max(costs)
                cost_matrix[r][c] = max_cost
                directions_matrix[r][c] = list(map(
                    lambda x: Direction(x[0]),
                    filter(lambda t: t[1] == max_cost, enumerate(costs))
                ))

    def __get_neighbor_costs(self, cost_matrix, a_seq, b_seq, r, c):
        return (
            self.__get_left_cost(cost_matrix, r, c),
            self.__get_diagonal_cost(cost_matrix, a_seq, b_seq, r, c),
            self.__get_up_cost(cost_matrix, r, c)
        )

    def __get_left_cost(self, cost_matrix, r, c):
        return cost_matrix[r][c - 1] + self.gap_penalty

    def __get_diagonal_cost(self, cost_matrix, a_seq, b_seq, r, c):
        return cost_matrix[r - 1][c - 1] + self.__item_comparison_cost(a_seq[r - 1], b_seq[c - 1])

    def __get_up_cost(self, cost_matrix, r, c):
        return cost_matrix[r - 1][c] + self.gap_penalty

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
