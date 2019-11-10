from abc import abstractmethod
from enum import IntEnum, unique

from typing import List, Tuple, Set

from src.utils import to_string


@unique
class Direction(IntEnum):
    LEFT = 0,
    DIAGONAL = 1,
    UP = 2


directions_moves = {
    Direction.LEFT: (0, -1),
    Direction.DIAGONAL: (-1, -1),
    Direction.UP: (-1, 0)
}


class ICellCostComputer(object):

    def __init__(self, gap_penalty: int, same_cost: int, diff_cost: int):
        self.gap_penalty = gap_penalty
        self.same_cost = same_cost
        self.diff_cost = diff_cost

    @abstractmethod
    def get_neighbor_costs(self, cost_matrix: List[List[int]],
                           a_seq: str, b_seq: str,
                           r: int, c: int) -> List[int]:
        raise NotImplementedError


class CellCostComputer(ICellCostComputer):

    def __init__(self, gap_penalty: int, same_cost: int, diff_cost: int):
        super().__init__(gap_penalty, same_cost, diff_cost)

    def get_neighbor_costs(self, cost_matrix: List[List[int]],
                           a_seq: str, b_seq: str,
                           r: int, c: int) -> List[int]:
        return [
            self.__get_left_cost(cost_matrix, r, c),
            self.__get_diagonal_cost(cost_matrix, a_seq, b_seq, r, c),
            self.__get_up_cost(cost_matrix, r, c)
        ]

    def __get_left_cost(self, cost_matrix: List[List[int]],
                        r: int, c: int) -> int:
        return cost_matrix[r][c - 1] + self.gap_penalty

    def __get_diagonal_cost(self, cost_matrix: List[List[int]],
                            a_seq: str, b_seq: str,
                            r: int, c: int) -> int:
        return cost_matrix[r - 1][c - 1] \
               + self.__item_comparison_cost(a_seq[r - 1], b_seq[c - 1])

    def __get_up_cost(self, cost_matrix: List[List[int]],
                      r: int, c: int) -> int:
        return cost_matrix[r - 1][c] + self.gap_penalty

    def __item_comparison_cost(self, a, b) -> int:
        return self.same_cost if a == b else self.diff_cost


class NeedlemanWunschSolver(object):

    gap_string = "-"

    def __init__(self, cell_cost_computer: ICellCostComputer):
        self.cell_cost_computer = cell_cost_computer

    def generate_alignment(self, a_seq: str, b_seq: str) -> Set[Tuple[str, str]]:
        _, directions_matrix = self.compute_cost_direction_matrices(a_seq, b_seq)
        return self.__generate_alignment(
            r=len(a_seq),
            c=len(b_seq),
            a_seq=a_seq,
            b_seq=b_seq,
            directions_matrix=directions_matrix,
            current_a_align=[],
            current_b_align=[]
        )

    def __generate_alignment(self,
                             r: int, c: int,
                             a_seq: str, b_seq: str,
                             directions_matrix: List[List[List[Direction]]],
                             current_a_align: List[str],
                             current_b_align: List[str]) \
            -> Set[Tuple[str, str]]:
        if r == 0 or c == 0:
            rest = max(r, c)
            a_align = current_a_align + ([self.gap_string] * rest if r == 0 else [x for x in a_seq[:r]])
            b_align = current_b_align + ([self.gap_string] * rest if c == 0 else [x for x in b_seq[:c]])
            return {tuple(map(
                lambda l: to_string(l)[::-1],
                [a_align, b_align]))[:2]
            }

        res = set()
        for direction in directions_matrix[r][c]:
            res |= self.__generate_alignment(
                r=r + directions_moves[direction][0],
                c=c + directions_moves[direction][1],
                a_seq=a_seq,
                b_seq=b_seq,
                directions_matrix=directions_matrix,
                current_a_align=current_a_align + [
                    a_seq[r - 1] if direction in (Direction.DIAGONAL, Direction.UP) else self.gap_string],
                current_b_align=current_b_align + [
                    b_seq[c - 1] if direction in (Direction.DIAGONAL, Direction.LEFT) else self.gap_string]
            )
        return res

    def compute_cost_direction_matrices(self, a_seq: str, b_seq: str) \
            -> (List[List[int]], List[List[List[Direction]]]):
        len_a, len_b = len(a_seq), len(b_seq)
        cost_matrix = self.generate_initial_cost_matrix(len_a, len_b)
        directions_matrix = self.generate_initial_directions_matrix(len_a, len_b)
        self.__fill_cost_and_direction_matrix(a_seq, b_seq, cost_matrix, directions_matrix)
        return cost_matrix, directions_matrix

    def generate_initial_cost_matrix(self, a_seq_len: int, b_seq_len: int) -> List[List[int]]:
        return self.__generate_matrix(
            height=a_seq_len + 1,
            width=b_seq_len + 1,
            cell_generator=self.__initial_cost_matrix_cell_generator
        )

    def generate_initial_directions_matrix(self, a_seq_len: int, b_seq_len: int) \
            -> List[List[List[Direction]]]:
        return self.__generate_matrix(
            height=a_seq_len + 1,
            width=b_seq_len + 1,
            cell_generator=lambda r, c: [])

    def __fill_cost_and_direction_matrix(self, a_seq: str, b_seq: str,
                                         cost_matrix: List[List[int]],
                                         directions_matrix: List[List[List[Direction]]]) -> None:
        matrix_height, matrix_width = len(cost_matrix), len(cost_matrix[0])
        for r in range(1, matrix_height):
            for c in range(1, matrix_width):
                neighbor_costs = self.cell_cost_computer.get_neighbor_costs(
                    cost_matrix, a_seq, b_seq, r, c
                )
                cost_matrix[r][c] = max(neighbor_costs)
                directions_matrix[r][c] = self.__get_directions(neighbor_costs, cost_matrix[r][c])

    @staticmethod
    def __get_directions(neighbor_costs: List[int], max_cost: int) -> List[Direction]:
        return list(
            map(
                lambda index_cost: Direction(index_cost[0]),
                filter(lambda index_cost: index_cost[1] == max_cost,
                       enumerate(neighbor_costs))
            )
        )

    @staticmethod
    def __generate_matrix(height: int, width: int,
                          cell_generator) -> List[List]:
        return [
            [cell_generator(r, c) for c in range(width)]
            for r in range(height)
        ]

    def __initial_cost_matrix_cell_generator(self, row: int, col: int) -> int:
        if row == 0 or col == 0:
            return max(row, col) * self.cell_cost_computer.gap_penalty
        else:
            return 0
