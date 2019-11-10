class NeedlemanWunschSolver:

    def __init__(self, gap_penalty: int, same_cost: int):
        self.gap_penalty = gap_penalty
        self.same_cost = same_cost
