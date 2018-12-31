from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
import networkx as nx
from graphs import *
from classical_solvers import *

def combined_test():
        #G = nx.algorithms.operators.unary.complement(melbourne())
        G = nx.gnp_random_graph(10, 0.5, 101)
        top = '10q-qvm'
        opt = 'POWELL'
        x = []
        ising = []
        qubo = []
        print('Powell, gnp topology, maximum clique, 10q rigetti qvm no noise')
        print(maximum_clique(G))
        for a in range(1, 50):
                x.append(a)
                result_out = rigetti_ising_qubo(G, maximum_clique_qubo_rigetti, opt, top, a)
                ref = subg_is_clique(result_out, G)
                if ref == True:
                         qubo.append(result_out.count(1))
                else:
                         qubo.append(0)
                print(x, qubo)
print(combined_test())
