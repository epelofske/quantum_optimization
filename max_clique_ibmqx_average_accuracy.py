
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
        for avg in range(0, 100):
            counter += 1
            result_out = solve_ibmqx_ising_qubo(G, func, optimizer, r)
            result2 = []
            for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)
            H = G.subgraph(result2)
            if is_clique(H) == True:
              qubo_main.append(len(H))
              app_ratio += len(H)
            else:
              qubo_main.append(0)
              app_ratio += 0
            print(float(app_ratio)/float(counter))
G = nx.gnp_random_graph(7, 0.5, 101)
print('max clique')
for op in opts:
  print(ibqmx_qaoa(G, SLSQP(), max_clique_qubo_matrix_ibmqx, 1))
