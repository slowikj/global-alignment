class NeedlemanWunschSolver(object):

    def __init__(self, gap_penalty: int, same_cost: int, diff_cost: int):
        self.gap_penalty = gap_penalty
        self.same_cost = same_cost
        self.diff_cost = diff_cost

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

    def __initial_cost_matrix_cell_generator(self, row: int, col: int):
        if row == 0 or col == 0:
            return max(row, col) * self.gap_penalty
        else:
            return 0

    @staticmethod
    def __generate_matrix(height: int, width: int, cell_generator):
        return [[cell_generator(r, c) for c in range(width)]
                for r in range(height)
                ]

