from graphs import *
from quil2qasm import *
from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
from pyquil.api import get_qc
import networkx as nx
import numpy as np
from dwave_qbsolv import QBSolv
import dimod
#from dwave.system.samplers import DWaveSampler
from qiskit import *
from qiskit_aqua.components.optimizers import *
from qiskit_aqua import QuantumInstance
from classical_solvers import *
import warnings
from graphs import *
warnings.filterwarnings("ignore")

def combined_test():
        #G = nx.gnp_random_graph(7, 0.5, 101)
        G = nx.algorithms.operators.unary.complement(ibmqx4())
#        G = nx.algorithms.operators.unary.complement(partial_melbourne())
#        G1 = nx.Graph()
#        G1.add_edge(0, 1)
#        G1.add_edge(1, 2)
#        G1.add_edge(2, 3)
#        G1.add_edge(0, 3)
#        G = nx.algorithms.operators.unary.complement(G1)
        ising = []
        ising2 = []
        x = []
        print('ibmqx, slsqp, ibmqx4 solver, complement of ibmqx4')
        print(maximum_clique(G))
        for a in range(1, 50):
             x.append(a)
#             optimizer = POWELL()
             optimizer = SLSQP()
             result_out = solve_ibmqx_ising_qubo_nisq_ibmqx4(G, max_clique_qubo_matrix_ibmqx, optimizer, a)

             result2 = []
             for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)

             ref = subg_is_clique(result2, G)
             if ref == True:
                  ising2.append(result2.count(1))
             else:
                  ising2.append(0)

             print(x, ising2)

print(combined_test())

