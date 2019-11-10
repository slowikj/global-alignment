import unittest

from parameterized import parameterized

from src.needleman_wunsch_solver import NeedlemanWunschSolver


class CostMatrixTests(unittest.TestCase):

    def setUp(self):
        self.solver = NeedlemanWunschSolver(
            same_cost=5,
            diff_cost=-5,
            gap_penalty=-2
        )

    @parameterized.expand([
        [
            [
                [0, -2, -4, -6],
                [-2, 5, 3, 1],
                [-4, 3, 10, 8],
                [-6, 1, 8, 15],
                [-8, -1, 6, 13]],
            "acca", "acc"
        ],
        [
            [
                [0]
            ],
            "", "",
        ],
        [
            [
                [0, -2, -4, -6]
            ],
            "", "ala"
        ],
        [
            [
                [0],
                [-2],
                [-4],
                [-6]
            ],
            "ala", ""
        ]
    ])
    def test_cost_matrix(self, expected_matrix, a_seq, b_seq):
        self.assertListEqual(
            self.solver.compute_cost_matrix(a_seq=a_seq, b_seq=b_seq),
            expected_matrix
        )
