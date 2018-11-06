# Imports
from LocalSearch import LocalSearch
import time


class IteratedLS:

    def __init__(self, initial_solution, penalty_matrix, max_time):
        self.solution = initial_solution
        self.local_search = LocalSearch(initial_solution, penalty_matrix)
        self.max_time = max_time

    def do_local_seach_iterated(self):
        # Variables to keep track and display
        seconds = 0
        minutes = 0
        # Begin Process
        while True:
            self.local_search.do_local_search_bi()
            self.solution = self.local_search.solution.solution
            # TODO Pertubar a solução
            # TODO Aplicar a busca local
            # TODO Verificar resultado (Se melhor, salvar)
            seconds += 1
            time.sleep(1)
            if seconds == 60:
                seconds = 0
                minutes += 1
            if minutes == self.max_time:
                break
