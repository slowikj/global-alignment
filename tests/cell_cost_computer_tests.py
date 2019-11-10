import unittest

from parameterized import parameterized

from src.needleman_wunsch_solver import CellCostComputer


class CellCostComputerTests(unittest.TestCase):
    gap_penalty = -2

    diff_cost = -5

    same_cost = 5

    def setUp(self):
        self.cell_cost_computer = CellCostComputer(
            gap_penalty=self.gap_penalty,
            diff_cost=self.diff_cost,
            same_cost=self.same_cost
        )

    def test_gap_penalty_initialization(self):
        self.assertEqual(self.cell_cost_computer.gap_penalty, self.gap_penalty)

    def test_same_cost_initialization(self):
        self.assertEqual(self.cell_cost_computer.same_cost, self.same_cost)

    def test_diff_cost_initialization(self):
        self.assertEqual(self.cell_cost_computer.diff_cost, self.diff_cost)

    @parameterized.expand([
        [
            [-4, 5, -4],
            [[0, -2, -4],
             [-2, 0, 0],
             [0, 0, 0]
            ],
            "AD", "AA",
            1, 1
        ],
        [
            [-6, -7, 3],
            [[0, -2, -4],
             [-2, 5, 3],
             [-4, 0, 0]
            ],
            "AD", "AA",
            2, 1
        ],
        [
            [1, 0, 1],
            [[0, -2, -4],
             [-2, 5, 3],
             [-4, 3, 0]
            ],
            "AD", "AA",
            2, 2
        ]
    ])
    def test_neighbor_costs_computation(self, expected_result,
                                        cost_matrix, a_seq, b_seq,
                                        r, c):
        self.assertListEqual(
            self.cell_cost_computer.get_neighbor_costs(cost_matrix, a_seq, b_seq, r, c),
            expected_result
        )
