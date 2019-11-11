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
            {("", "")},
            "", ""
        ],
        [
            {("A", "A")},
            "A", "A"
        ],
        [
            {("AA", "A-"), ("AA", "-A")},
            "AA", "A"
        ],
        [
            {("A-S", "AA-"), ("-AS", "AA-"), ("AS-", "A-A")},
            "AS", "AA"
        ],
        [
            {('AAA-D', '--AS-'),
             ('A-AAD', 'AS---'),
             ('AA-AD', 'A-S--'),
             ('AAA-D', 'A--S-'),
             ('AA-AD', '-AS--'),
             ('AAAD-', 'A---S'),
             ('AAAD-', '--A-S'),
             ('AAAD-', '-A--S'),
             ('AAA-D', '-A-S-')},
            "AAAD", "AS"
        ],
        [
            {("----", "AAAD")},
            "", "AAAD"
        ]
    ])
    def test(self, expected_result, seq_a, seq_b):
        alignment = self.solver.generate_alignment(a_seq=seq_a, b_seq=seq_b)
        self.assertSetEqual(
            alignment,
            expected_result
        )
