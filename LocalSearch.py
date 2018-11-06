# Imports
from Solution import Solution


class LocalSearch:
    def __init__(self, initial_solution, penalty_matrix, ls_type):
        """ Read the penalty matrix and initial solution and compute the best solution"""
        self.solution = Solution(initial_solution, penalty_matrix)
        self.ls_type = ls_type

    def make_local_search(self):
        if self.ls_type == "best_improvement":
            self.__do_local_search_bi()
        else:
            self.__do_local_search_fi()

    def __do_local_search_bi(self):
        """ Make a best improvement localsearch on the initial solution"""
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
                improved = True

    def __do_local_search_fi(self):
        """ Make a first improvement localsearch on the initial solution"""
        improved = True
        while improved:
            improved = False
            for i in range(self.solution.size):
                if self.solution.flip_value(i) > 0:
                    self.solution.flip_solution(i)
                    improved = True
                    break
