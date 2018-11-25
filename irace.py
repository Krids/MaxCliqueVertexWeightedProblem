#!/usr/bin/python

import re
import sys
import matplotlib.pyplot as plt
import Utils as utils
import numpy as np

from LocalSearch import LocalSearch
from InitialSolution import InitialSolution
from IteratedLS import IteratedLS
from RandomLS import RandomLS
from scipy import optimize

complement_matrix = utils.find_complement_matrix(sys.argv[2])
penalty_matrix = utils.apply_preparations(complement_matrix)
type_search = sys.argv[5]
ls_type = sys.argv[6]
iterated_type = sys.argv[7]
initial_solution_type = sys.argv[8]
k = None
p = None

# Chamada do Random Local Search possui dois parâmetros a mais: "p" e "k"
if len(sys.argv) == 11:
    p = float(sys.argv[9])
    k = int(sys.argv[10])

iterated_ls = IteratedLS(penalty_matrix=penalty_matrix, max_time=1, type_search=type_search, ls_type=ls_type, 
                         iterated_type=iterated_type, initial_solution_type=initial_solution_type, k=k, p=p)
iterated_ls.make_iterated_local_search()

print(iterated_ls.value)