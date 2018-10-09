# Imports
import numpy as np


class LocalSearch:

    def __init__(self, adjacency_matrix, penalty_matrix):
        self.adjacency_matrix = adjacency_matrix
        self.penalty_matrix = penalty_matrix

    def get_random_initial_solution(self):
        initial_solution = np.random.rand(1, len(self.adjacency_matrix))
        for i in range(initial_solution.shape[1]):
            if initial_solution[0, i] > 0.5:
                initial_solution[0, i] = 1
            else:
                initial_solution[0, i] = 0
        print(initial_solution)
        return initial_solution

    def get_neighbors(self, initial_solution):
        neighbors = np.tile(initial_solution, (self.adjacency_matrix.shape[1], 1))
        for i in range(initial_solution.shape[1]):
            if neighbors[i, i] == 1.:
                neighbors[i, i] = 0.
            else:
                neighbors[i, i] = 1.
        print(neighbors)
        return neighbors

    def get_best_in_neighborhood(self, neighborhood):
        array_sum = np.zeros((1, neighborhood.shape[0]))
        best_solution = np.zeros((1, neighborhood.shape[0]))
        print(array_sum.shape)
        for row in range(neighborhood.shape[0]):
            objective_sum = 0
            for i in range(self.adjacency_matrix.shape[0]):
                for j in range(self.adjacency_matrix.shape[1]):
                    if neighborhood[row, i] == neighborhood[row, j] and neighborhood[row, i] == 1:
                        objective_sum += self.penalty_matrix[i, j]
            array_sum[0, row] += objective_sum
            if array_sum.max() == objective_sum:
                best_solution = neighborhood[row, :]
        return array_sum.max(), best_solution
