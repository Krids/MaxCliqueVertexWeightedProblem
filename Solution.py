import numpy as np


class Solution:
    def __init__(self, initial_solution, penalty_matrix):
        self.solution = initial_solution
        self.size = initial_solution.shape[1]
        self.delta = np.zeros((1, self.size))
        self.penalty_matrix = penalty_matrix
        self.value = self.evaluate()
        self.create_delta()

    def evaluate(self):
        quality = 0
        for i in range(self.size):
            for j in range(self.size):
                quality += self.solution[0, i] * self.solution[0, j] * self.penalty_matrix[i, j]
        self.value = quality
        return quality

    def flip_value(self, position):
        return self.delta[0, position]

    def flip_solution(self, position):
        if self.solution[0, position] == 0:
            self.solution[0, position] = 1
        else:
            self.solution[0, position] = 0
        self.value += self.delta[0, position]
        self.update_delta(position)

    def create_delta(self):
        for i in range(self.size):
            if self.solution[0, i] == 0:
                self.delta[0, i] += self.penalty_matrix[i, i]
            else:
                self.delta[0, i] -= self.penalty_matrix[i, i]

            for j in range(self.size):
                if i != j:
                    if self.solution[0, i] == 1 and self.solution[0, j] == 1:
                        self.delta[0, i] -= self.penalty_matrix[i, j]
                    if self.solution[0, i] == 0 and self.solution[0, j] == 1:
                        self.delta[0, i] += self.penalty_matrix[i, j]

    def update_delta(self, position):
        self.delta[0, position] = -self.delta[0, position]
        for i in range(self.size):
            if position != i:
                if self.solution[0, position] == 1 and self.solution[0, i] == 1:
                    self.delta[0, i] -= self.penalty_matrix[position, i]
                if self.solution[0, position] == 1 and self.solution[0, i] == 0:
                    self.delta[0, i] += self.penalty_matrix[position, i]

                if self.solution[0, position] == 0 and self.solution[0, i] == 1:
                    self.delta[0, i] += self.penalty_matrix[position, i]
                if self.solution[0, position] == 0 and self.solution[0, i] == 0:
                    self.delta[0, i] -= self.penalty_matrix[position, i]


