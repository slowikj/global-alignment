import unittest

from parameterized import parameterized

from src.needleman_wunsch_solver import NeedlemanWunschSolver, Direction


class DirectionsMatrixTest(unittest.TestCase):

    def setUp(self):
        self.solver = NeedlemanWunschSolver(
            same_cost=5,
            diff_cost=-5,
            gap_penalty=-2
        )

    @parameterized.expand([
        [
            [
                [[], [], []],
                [[], [Direction.DIAGONAL], [Direction.LEFT, Direction.DIAGONAL]],
                [[], [Direction.UP], [Direction.LEFT, Direction.UP]]
            ], "AD", "AA"
        ]
    ])
    def test_directions_matrix(self, expected_result, a_seq, b_seq):
        print("expected_result '{}'".format(expected_result))
        print("a_seq = '{}'".format(a_seq))
        _, result = self.solver.compute_cost_direction_matrices(a_seq=a_seq, b_seq=b_seq)
        self.assertListEqual(result, expected_result)
