# Imports
from Solution import Solution


class LocalSearch:
    def __init__(self, initial_solution, penalty_matrix):
        """ Read the penalty matrix and initial solution and compute the best solution"""
        self.solution = Solution(initial_solution, penalty_matrix)

    def do_local_search2(self):
        improved = True
        while improved:
            improved = False
            best_candidate = -1
            best_improvement = 0
            for i in range(self.solution.size):
                value = self.solution.flip_value(i)
                if value > best_improvement:
                    best_improvement = value
                    best_candidate = i

            if best_candidate != -1:
                self.solution.flip_solution(best_candidate)
                #improved = True


    def do_local_search(self):
        improved = True
        while improved:
            improved = False
            for i in range(self.solution.size):
                if self.solution.flip_value(i) > 0:
                    self.solution.flip_solution(i)
                    improved = True
                    break  # First improvement
