import unittest

from solver import NeedlemanWunschSolver, CellCostComputer


class GeneralNeedlemanWunschTests(unittest.TestCase):
    gap_penalty = -2

    same_cost = 5

    diff_cost = -5

    def setUp(self):
        self.solver = NeedlemanWunschSolver(
            CellCostComputer(
                gap_penalty=self.gap_penalty,
                same_cost=self.same_cost,
                diff_cost=self.diff_cost)
        )

    def test_generate_initial_cost_matrix(self):
        a_seq_len = 2
        b_seq_len = 3

        result_matrix = self.solver.generate_initial_cost_matrix(
            a_seq_len=a_seq_len,
            b_seq_len=b_seq_len
        )

        gp = self.gap_penalty
        expected_matrix = [
            [0, gp, 2 * gp, 3 * gp],
            [gp, 0, 0, 0],
            [2 * gp, 0, 0, 0]
        ]

        self.assertListEqual(result_matrix, expected_matrix)

    def test_generate_initial_directions_matrix(self):
        a_seq_len = 2
        b_seq_len = 3

        result_matrix = self.solver.generate_initial_directions_matrix(
            a_seq_len=a_seq_len,
            b_seq_len=b_seq_len
        )

        expected_matrix = [
                              [[] for _ in range(b_seq_len + 1)]
                          ] * (a_seq_len + 1)

        self.assertListEqual(result_matrix, expected_matrix)
