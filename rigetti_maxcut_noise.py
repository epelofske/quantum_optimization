from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
import networkx as nx
from graphs import *
from classical_solvers import *

def combined_test2():
        #G = melbourne()
        G = nx.gnp_random_graph(10, 0.5, 101)
        top = '10q-noisy-qvm'
        opt = 'POWELL'
        x = []
        ising = []
        qubo = []
        print('Powell, gnp topology, maximum cut, 10q rigetti qvm noise')
        print(20)
        for a in range(1, 50):
                x.append(a)
                result_out = rigetti_ising_qubo(G, maximum_cut_qubo_rigetti, opt, top, a)
                #ref = subg_is_clique(result_out, G)
                #if ref == True:
                qubo.append(max_cut_value(result_out, G))
                #else:
                #         qubo.append(0)
                print(x, qubo)
print(combined_test2())
