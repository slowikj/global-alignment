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

