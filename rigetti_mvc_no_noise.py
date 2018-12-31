from quil2qasm import *
from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
from pyquil.api import get_qc
import networkx as nx
import numpy as np
from dwave_qbsolv import QBSolv
import dimod
from graphs import *
#from dwave.system.samplers import DWaveSampler
from qiskit import *
from qiskit_aqua.components.optimizers import *
from qiskit_aqua import QuantumInstance
from classical_solvers import *

def combined_test():
        #G = melbourne()
        G = nx.gnp_random_graph(10, 0.5, 101)
        top = '10q-qvm'
        opt = 'POWELL'
        x = []
        ising = []
        qubo = []
        print('Powell, gnp topology, minimum vertex cover, 10q rigetti qvm no noise')
        print(minimum_vertex_cover(G))
        for a in range(1, 50):
                x.append(a)
                result_out = rigetti_ising_qubo(G, minimum_vertex_cover_ising_rigetti, opt, top, a)
                ref = is_vertex_cover(result_out, G)
                if ref == True:
                         ising.append(result_out.count(1))
                else:
                         ising.append(0)
                print(x, ising)
print(combined_test())


