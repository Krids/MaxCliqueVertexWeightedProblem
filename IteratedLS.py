# Imports
from LocalSearch import LocalSearch
from RandomLS import RandomLS
from InitialSolution import InitialSolution
import datetime
import numpy as np


class IteratedLS:

    def __init__(self, penalty_matrix, max_time, type_search, p=None, k=None, ls_type="best_improvement",
                 iterated_type="new_clique", initial_solution_type="best"):
        self.penalty_matrix = penalty_matrix
        self.is_ = InitialSolution(penalty_matrix, initial_solution_type)
        self.ls_type = ls_type
        self.p = p
        self.k = k
        self.type_search = type_search
        if type_search == "local_search":
            ls = LocalSearch(self.is_.get_initial_solution(), penalty_matrix, ls_type)
            ls.make_local_search()
            self.value = ls.solution.value
            self.solution = ls.solution.solution
        else:
            rdn_ls = RandomLS(self.is_.get_initial_solution(), penalty_matrix, p,
                              k, max_time, param=ls_type)
            rdn_ls.do_random_local_search()
            self.value = rdn_ls.solution.value
            self.solution = rdn_ls.solution.solution
        self.best_solution = self.solution
        self.max_time = max_time
        self.iterated_type = iterated_type

    def make_iterated_local_search(self):
        if self.iterated_type == "new_clique":
            self.__do_local_search_iterated_with_new_clique()
        else:
            self.__do_local_search_iterated_with_clique_combination()

    def __do_local_search_iterated_with_new_clique(self):
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=self.max_time)
        while True:
            if datetime.datetime.now() >= end_time:
                break

            self.solution = self.is_.get_initial_solution()

            if self.type_search == "local_search":
                local_search = LocalSearch(self.solution, self.penalty_matrix, self.ls_type)
                local_search.make_local_search()
                if local_search.solution.value >= self.value:
                    self.best_solution = self.solution
                    self.value = local_search.solution.value
            else:
                rdn_ls = RandomLS(self.solution, self.penalty_matrix, self.p, self.k, self.max_time, param=self.ls_type)
                rdn_ls.do_random_local_search()
                if rdn_ls.solution.value >= self.value:
                    self.best_solution = self.solution
                    self.value = rdn_ls.solution.value

    def __do_local_search_iterated_with_clique_combination(self):
        end_time = datetime.datetime.now() + datetime.timedelta(minutes=self.max_time)
        while True:
            if datetime.datetime.now() >= end_time:
                break

            new_clique = self.is_.get_initial_solution()
            half_size = int(new_clique.shape[1] / 2)
            self.solution[0] = np.concatenate((new_clique[0, :half_size],
                                               self.best_solution[0, half_size:]))
            if self.type_search == "local_search":
                local_search = LocalSearch(self.solution, self.penalty_matrix, self.ls_type)
                local_search.make_local_search()
                if local_search.solution.value >= self.value:
                    self.best_solution = self.solution
                    self.value = local_search.solution.value
            else:
                rdn_ls = RandomLS(self.solution, self.penalty_matrix, self.p, self.k, self.max_time, param=self.ls_type)
                rdn_ls.do_random_local_search()
                if rdn_ls.solution.value >= self.value:
                    self.best_solution = self.solution
                    self.value = rdn_ls.solution.value
