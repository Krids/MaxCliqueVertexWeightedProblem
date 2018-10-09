# Imports
import networkx as nx
import numpy as np
import pandas as pd


def get_adjacency_matrix(filename):
    fh = open(filename, 'rb')
    graphs = nx.read_edgelist(fh)
    fh.close()
    numpy_adjacency_matrix = nx.to_numpy_matrix(graphs)
    print(numpy_adjacency_matrix)
    return numpy_adjacency_matrix


def addWeightToVector(df):
    weights = pd.DataFrame(np.zeros([1, 1272]))
    for i in range(len(df.index)):
        weights[i] += (i % 200) + 1
    print(weights)
    return weights


def findTheComplementMatrix(filename):
    fh = open(filename, 'rb')
    graphs = nx.read_edgelist(fh)
    fh.close()
    comple_graphs = nx.complement(graphs)
    numpy_adjacency_matrix = nx.to_numpy_matrix(comple_graphs)
    print(numpy_adjacency_matrix)
    return numpy_adjacency_matrix


def apply_penalty(matrix):
    return matrix * -1000