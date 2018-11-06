# Imports
from LocalSearch import LocalSearch


class IteratedLS:

    def __init__(self, initial_solution, penalty_matrix):
        self.local_search = LocalSearch(initial_solution, penalty_matrix)

    #TODO Busca Local Randomizada
    """
    Parametro p = [0,1]
    Busca Local
    Se random <= p
        Modifica k vertices
    Senao 
        Busca Local (Fi/Bi)
    """