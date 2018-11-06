import numpy as np
import random


class InitialSolution:

    def __init__(self, penalty_matrix):
        self.penalty_matrix = penalty_matrix
        self.initial_solution = np.zeros((1, len(self.penalty_matrix)))

    def get_random_initial_solution(self):
        """ Return a random initial solution ex. [10101..."""
        self.initial_solution = np.random.rand(1, len(self.penalty_matrix))
        for i in range(self.initial_solution.shape[1]):
            if self.initial_solution[0, i] > 0.5:
                self.initial_solution[0, i] = 1
            else:
                self.initial_solution[0, i] = 0
        return self.initial_solution

    def get_empty_initial_solution(self):
        """ Return a empty initial solution ex. [0000..."""
        self.initial_solution = np.zeros((1, len(self.penalty_matrix)))
        return self.initial_solution

    def get_random_clique_initial_solution(self):
        """ Return a random clique for the initial solution"""
        self.initial_solution = np.zeros((1, len(self.penalty_matrix)))
        rdn_initial_position = random.randint(0, self.penalty_matrix.shape[0] + 1)
        ones_list = [rdn_initial_position]
        start = 0
        self.initial_solution[0, rdn_initial_position] = 1
        while start != len(self.penalty_matrix):
            if self.initial_solution[0, start] == 0:
                violation = False
                for j in ones_list:
                    if self.penalty_matrix[j, start] != 0 or self.penalty_matrix[start, j] != 0:
                        violation = True
                        break

                if not violation:
                    ones_list.append(start)
                    self.initial_solution[0, start] = 1
            start += 1
        return self.initial_solution

    def get_random_clique_initial_solution_with_random_start(self):
        """ Return a random clique for the initial solution but with random start point"""
        self.initial_solution = np.zeros((1, len(self.penalty_matrix)))
        rdn_initial_position = random.randint(0, self.penalty_matrix.shape[0] + 1)
        ones_list = [rdn_initial_position]
        start = random.randint(0, self.penalty_matrix.shape[0] + 1)
        startpoint = start
        count = 0
        self.initial_solution[0, rdn_initial_position] = 1
        while start != len(self.penalty_matrix):
            if self.initial_solution[0, start] == 0:
                violation = False
                for j in ones_list:
                    if self.penalty_matrix[j, start] != 0 or self.penalty_matrix[start, j] != 0:
                        violation = True
                        break

                if not violation:
                    ones_list.append(start)
                    self.initial_solution[0, start] = 1
            start += 1
        while count != startpoint:
            if self.initial_solution[0, count] == 0:
                violation = False
                for j in ones_list:
                    if self.penalty_matrix[j, count] != 0 or self.penalty_matrix[count, j] != 0:
                        violation = True
                        break

                if not violation:
                    ones_list.append(count)
                    self.initial_solution[0, count] = 1
            count += 1
        return self.initial_solution

    def get_random_clique_initial_solution_with_random_walking(self):
        """ Return a random clique for the initial solution"""
        self.initial_solution = np.zeros((1, len(self.penalty_matrix)))
        rdn_initial_position = random.randint(0, self.penalty_matrix.shape[0] + 1)
        ones_list = [rdn_initial_position]
        self.initial_solution[0, rdn_initial_position] = 1
        rdn_walking = np.arange(0, self.penalty_matrix.shape[1], 1)
        random.shuffle(rdn_walking)
        for i, x in enumerate(rdn_walking):
            if self.initial_solution[0, x] == 0:
                violation = False
                for j in ones_list:
                    if self.penalty_matrix[j, x] != 0 or self.penalty_matrix[x, j] != 0:
                        violation = True
                        break

                if not violation:
                    ones_list.append(i)
                    self.initial_solution[0, x] = 1
        return self.initial_solution
