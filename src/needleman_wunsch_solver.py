class NeedlemanWunschSolver:

    def __init__(self, gap_penalty: int, same_cost: int, diff_cost: int):
        self.gap_penalty = gap_penalty
        self.same_cost = same_cost
        self.diff_cost = diff_cost

    def generate_initial_cost_matrix(self, a_seq_len: int, b_seq_len: int):
        res = [
            [0 for _ in range(a_seq_len + 1)] for _ in range(b_seq_len + 1)
        ]

        for i in range(a_seq_len + 1):
            res[0][i] = i * self.gap_penalty

        for i in range(b_seq_len + 1):
            res[i][0] = i * self.gap_penalty

        return res

    def generate_initial_directions_matrix(self, a_seq_len, b_seq_len):
        return [[] for _ in range(a_seq_len + 1)] * (b_seq_len + 1)

