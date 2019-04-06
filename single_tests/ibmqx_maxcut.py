import os
import sys
d = os.path.dirname(os.getcwd())+'/utils'
sys.path.append(d)
from graphs import *
from ibmqx_ising_qubo_qaoa import *
from qubo_ising_generators import *
from classical_solvers import *
import networkx as nx
import numpy as np
import time
from qiskit import *
from qiskit_aqua.components.optimizers import *
from qiskit_aqua import QuantumInstance
import warnings
warnings.filterwarnings("ignore")

def combined_test():
        G = nx.gnp_random_graph(8, 0.5, 101)
        ising = []
        ising2 = []
        x = []
        print('ibmqx, max cut, slsqp, qasm simulator, no noise, gnp')
        for a in range(1, 50):
             x.append(a)
             optimizer = SLSQP()
             result_out = solve_ibmqx_ising_qubo(G, max_cut_qubo_matrix_ibmqx, optimizer, a)

             result2 = []
             for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)

             ising2.append(max_cut_value(result2, G))
             print(x, ising2)

print(combined_test())

