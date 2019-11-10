import unittest

from src.needleman_wunsch_solver import NeedlemanWunschSolver


class NeedlemanWunschTests(unittest.TestCase):

    gap_penalty = -2

    same_cost = 5

    diff_cost = -5

    def setUp(self):
        self.solver = NeedlemanWunschSolver(
            gap_penalty=self.gap_penalty,
            same_cost=self.same_cost,
            diff_cost=self.diff_cost)

    def test_solver_has_properly_initialized_gap_penalty_field(self):
        self.assertEqual(self.solver.gap_penalty, self.gap_penalty)

    def test_solver_has_properly_initialized_same_cost_field(self):
        self.assertEqual(self.solver.same_cost, self.same_cost)

    def test_solver_has_properly_initialized_diff_cost_field(self):
        self.assertEqual(self.solver.diff_cost, self.diff_cost)

    def test_generate_initial_cost_matrix(self):
        a_seq_len = 2
        b_seq_len = 3

        result_matrix = self.solver.generate_initial_cost_matrix(
            a_seq_len=a_seq_len,
            b_seq_len=b_seq_len
        )

        gp = self.gap_penalty
        expected_matrix = [
            [0, gp, 2 * gp],
            [gp, 0, 0],
            [2 * gp, 0, 0],
            [3 * gp, 0, 0]
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
            [] * (a_seq_len + 1)
        ] * (b_seq_len + 1)

        self.assertListEqual(result_matrix, expected_matrix)
