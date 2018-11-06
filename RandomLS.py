# Imports
import random
import datetime
import numpy as np
from Solution import Solution


class RandomLS:

    def __init__(self, initial_solution, penalty_matrix, p, k, max_time, param):
        self.param = param
        self.p = p
        self.k = k
        self.max_time = max_time
        self.solution = Solution(initial_solution, penalty_matrix)
        self.best_solution = self.solution

    def do_random_local_search(self):
        pertubation = np.zeros((1, len(self.solution.solution)))

        end_time = datetime.datetime.now() + datetime.timedelta(minutes=self.max_time)
        while True:
            if datetime.datetime.now() >= end_time:
                break

        if random.random() <= self.p:
            #TODO arrumar a pertubação
            pertubation[0] = np.random.binomial(len(self.solution.solution), 0.5)
        else:
            if self.param == "first_improvement":
                self.__first_improvement()
            else:
                self.__best_improvement()

    def __first_improvement(self):
        """ Make a first improvement move on the solution"""
        for i in range(self.solution.size):
            if self.solution.flip_value(i) > 0:
                self.solution.flip_solution(i)
                break

    def __best_improvement(self):
        """ Make a best improvement move on the solution"""
        best_candidate = -1
        best_improvement = 0
        for i in range(len(self.solution.solution)):
            value = self.solution.flip_value(i)
            if value > best_improvement:
                best_improvement = value
                best_candidate = i
        if best_candidate != -1:
            self.solution.flip_solution(best_candidate)
