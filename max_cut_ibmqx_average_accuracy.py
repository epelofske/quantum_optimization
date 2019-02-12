from utils.graphs import *
from utils.ibmqx_ising_qubo_qaoa import *
from utils.qubo_ising_generators import *
from utils.classical_solvers import *
import networkx as nx
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")

def ibqmx_qaoa(G, optimizer, func, r):
        app_ratio = 0
        qubo_main = []
        counter = 0
        for avg in range(0, 1000):
            counter += 1
            result_out = solve_ibmqx_ising_qubo(G, func, optimizer, r)
            result2 = []
            for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)
            x = max_cut_value(result2, G)
            qubo_main.append(x)
            app_ratio += x
            print(float(app_ratio)/float(counter))
G = nx.gnp_random_graph(7, 0.5, 101)
print('maxcut')
for op in opts:
  print(ibqmx_qaoa(G, SLSQP(), max_cut_qubo_matrix_ibmqx, 1))
