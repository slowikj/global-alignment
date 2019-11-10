import unittest

from parameterized import parameterized

from src.needleman_wunsch_solver import NeedlemanWunschSolver, CellCostComputer


class AlignmentPathsTests(unittest.TestCase):

    def setUp(self):
        self.solver = NeedlemanWunschSolver(CellCostComputer(
            same_cost=5,
            diff_cost=-5,
            gap_penalty=-2
        ))

    @parameterized.expand([
        [
            [("", "")],
            "", ""
        ]
    ])
    def test(self, expected_result, seq_a, seq_b):
        self.assertListEqual(
            self.solver.generate_alignment(seq_a=seq_a, seq_b=seq_b),
            expected_result
        )
