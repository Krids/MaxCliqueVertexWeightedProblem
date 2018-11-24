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
    return numpy_adjacency_matrix


def find_complement_matrix(filename):
    fh = open(filename, 'rb')
    graphs = nx.read_edgelist(fh)
    fh.close()
    comple_graphs = nx.complement(graphs)
    numpy_adjacency_matrix = nx.to_numpy_matrix(comple_graphs)
    return numpy_adjacency_matrix


def apply_preparations(matrix):
    """Get the adjacency matrix and return a triangular matrix with the weights and penalties"""
    matrix = matrix * -1000
    matrix = add_weight_to_matrix(matrix)
    return np.triu(matrix)


    