class NeedlemanWunschSolver(object):

    def __init__(self, gap_penalty: int, same_cost: int, diff_cost: int):
        self.gap_penalty = gap_penalty
        self.same_cost = same_cost
        self.diff_cost = diff_cost

    def generate_initial_cost_matrix(self, a_seq_len: int, b_seq_len: int):
        res = self.__generate_matix(
            height=b_seq_len + 1,
            width=a_seq_len + 1,
            cell_generator=lambda r, c: 0
        )

        for i in range(a_seq_len + 1):
            res[0][i] = i * self.gap_penalty

        for i in range(b_seq_len + 1):
            res[i][0] = i * self.gap_penalty

        return res

    def generate_initial_directions_matrix(self, a_seq_len: int, b_seq_len: int):
        return self.__generate_matix(
            height=b_seq_len + 1,
            width=a_seq_len + 1,
            cell_generator=lambda r, c: [])

    def __generate_matix(self, height: int, width: int, cell_generator):
        return [[cell_generator(r, c) for c in range(width)]
                for r in range(height)
                ]

