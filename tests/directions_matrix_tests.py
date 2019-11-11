import unittest

from parameterized import parameterized

from src.solver import NeedlemanWunschSolver, Direction, CellCostComputer


class DirectionsMatrixTest(unittest.TestCase):

    def setUp(self):
        self.solver = NeedlemanWunschSolver(
            CellCostComputer(
                same_cost=5,
                diff_cost=-5,
                gap_penalty=-2
            )
        )

    @parameterized.expand([
        [
            [
                [[], [], []],
                [[], [Direction.DIAGONAL], [Direction.LEFT, Direction.DIAGONAL]],
                [[], [Direction.UP], [Direction.LEFT, Direction.UP]]
            ], "AD", "AA"
        ],
        [
            [
                [[], [], [], []],
                [[], [Direction.DIAGONAL], [Direction.LEFT, Direction.DIAGONAL], [Direction.LEFT]],
                [[], [Direction.UP], [Direction.LEFT, Direction.UP], [Direction.LEFT, Direction.UP]],
                [[], [Direction.DIAGONAL, Direction.UP], [Direction.DIAGONAL], [Direction.LEFT]]
            ], "ADA", "AAS"
        ],
        [
            [[[]]],
            "", ""
        ],
        [
            [
                [[]],
                [[]],
                [[]]
            ], "AA", ""
        ],
        [
            [
                [[], [], []]
            ], "", "AA"
        ]
    ])
    def test_directions_matrix(self, expected_result, a_seq, b_seq):
        _, result = self.solver.compute_cost_direction_matrices(a_seq=a_seq, b_seq=b_seq)
        self.assertListEqual(result, expected_result)
