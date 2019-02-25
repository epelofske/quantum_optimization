from utils.graphs import *
from utils.ibmqx_ising_qubo_qaoa import *
from utils.qubo_ising_generators import *
from utils.classical_solvers import *
import networkx as nx
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")

def combined_test():
        #G = nx.gnp_random_graph(7, 0.5, 101)
        G = melbourne()
        #G = nx.algorithms.operators.unary.complement(G1)
        ising = []
        ising2 = []
        x = []
        print('ibmqx, SLSQP, ibmq 16 melbourne solver, melbourne')
        #print(maximum_clique(G))
        for a in range(1, 20):
             x.append(a)
#             optimizer = POWELL()
             optimizer = SLSQP()
             result_out = solve_ibmqx_ising_qubo_nisq_melbourne(G, max_cut_qubo_matrix_ibmqx, optimizer, a)

             result2 = []
             for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)

             ising2.append(max_cut_value(result2, G))
             print(x, ising2)

print(combined_test())
