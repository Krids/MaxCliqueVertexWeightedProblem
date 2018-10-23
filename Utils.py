import networkx as nx
import numpy as np


# Read and prepare the instance


def add_weight_to_matrix(matrix):
    for i in range(matrix.shape[0]):
        matrix[i, i] = (i % 200) + 1
    return matrix


def get_adjacency_matrix(filename):
    fh = open(filename, 'rb')
    graphs = nx.read_edgelist(fh)
    fh.close()
    numpy_adjacency_matrix = nx.to_numpy_matrix(graphs)
    print(numpy_adjacency_matrix)
    return numpy_adjacency_matrix


def find_complement_matrix(filename):
    fh = open(filename, 'rb')
    graphs = nx.read_edgelist(fh)
    fh.close()
    comple_graphs = nx.complement(graphs)
    numpy_adjacency_matrix = nx.to_numpy_matrix(comple_graphs)
    print(numpy_adjacency_matrix)
    return numpy_adjacency_matrix


def apply_preparations(matrix):
    """Get the adjacency matrix and return a triangular matrix with the weights and penalties"""
    matrix = matrix * -1000
    matrix = add_weight_to_matrix(matrix)
    return np.triu(matrix)


# Get the initial solution


def get_random_initial_solution(adjacency_matrix):
    initial_solution = np.random.rand(1, len(adjacency_matrix))
    for i in range(initial_solution.shape[1]):
        if initial_solution[0, i] > 0.5:
            initial_solution[0, i] = 1
        else:
            initial_solution[0, i] = 0
    return initial_solution


def get_empty_initial_solution(adjacency_matrix):
    initial_solution = np.zeros((1, len(adjacency_matrix)))
    return initial_solution


def get_neighbors(initial_solution):
    neighbors = np.tile(initial_solution, (initial_solution.shape[1], 1))
    for i in range(initial_solution.shape[1]):
        if neighbors[i, i] == 1.:
            neighbors[i, i] = 0.
        else:
            neighbors[i, i] = 1.
    print(neighbors)
    return neighbors
