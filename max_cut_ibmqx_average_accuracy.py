from utils.graphs import *
from utils.ibmqx_ising_qubo_qaoa import *
from utils.qubo_ising_generators import *
from utils.classical_solvers import *
import networkx as nx
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")

def ibqmx_qaoa(G, optimizer, func):
        x = []
        timer_main = []
        qubo_main = []
        for a in range(1, (len(G)*2)+1):
            x.append(a)
            qubo = []
            timer = []
                start1 = time.clock()
                result_out = solve_ibmqx_ising_qubo(G, func, SLSQP(), a)
                diff1 = time.clock()-start1
                timer.append(diff1)
                result2 = []
                for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)
                qubo.append(max_cut_value(result2, G))

G = nx.gnp_random_graph(7, 0.5, 101)
print('maxcut')
for op in opts:
  print(op, ibqmx_qaoa(G, op, max_cut_qubo_matrix_ibmqx))
