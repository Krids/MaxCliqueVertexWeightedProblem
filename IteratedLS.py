# Imports
from LocalSearch import LocalSearch
from InitialSolution import InitialSolution
import datetime
import numpy as np


class IteratedLS:

    def __init__(self, penalty_matrix, max_time):
        self.penalty_matrix = penalty_matrix
        self.is_ = InitialSolution(penalty_matrix)
        ls = LocalSearch(self.is_.get_random_clique_initial_solution_with_random_start(), penalty_matrix)
        ls.do_local_search_bi()
        self.value = ls.solution.value
        self.solution = ls.solution.solution
        self.best_solution = self.solution
        self.max_time = max_time

    def do_local_search_iterated_with_new_clique(self):
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=self.max_time)
        while True:
            if datetime.datetime.now() >= end_time:
                break

            self.solution = self.is_.get_random_clique_initial_solution_with_random_start()
            local_search = LocalSearch(self.solution, self.penalty_matrix)
            local_search.do_local_search_bi()
            if local_search.solution.value >= self.value:
                self.best_solution = self.solution
                self.value = local_search.solution.value

    def do_local_search_iterated_with_clique_combination(self):
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=self.max_time)
        while True:
            if datetime.datetime.now() >= end_time:
                break

            new_clique = self.is_.get_random_clique_initial_solution_with_random_walking()
            half_size = int(new_clique.shape[1] / 2)
            self.solution[0] = np.concatenate((new_clique[0, :half_size],
                                               self.best_solution[0, half_size:]))
            local_search = LocalSearch(self.solution, self.penalty_matrix)
            local_search.do_local_search_bi()
            if local_search.solution.value >= self.value:
                self.best_solution = self.solution
                self.value = local_search.solution.value
