import unittest

from src.needleman_wunsch_solver import NeedlemanWunschSolver


class NeedlemanWunschTests(unittest.TestCase):

    gap_penalty = -2

    def setUp(self):
        self.solver = NeedlemanWunschSolver(gap_penalty=gap_penalty)

    def test_solver_has_properly_initialized_gap_penalty_field(self):
        self.assertEquals(self.solver, gap_penalty)
