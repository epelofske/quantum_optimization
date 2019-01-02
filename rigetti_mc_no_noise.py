from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
import networkx as nx
from graphs import *
from classical_solvers import *
import time

def combined_test2():
        #G = nx.algorithms.operators.unary.complement(melbourne())
        G = nx.gnp_random_graph(7, 0.5, 101)
        top = '7q-qvm'
        opt = 'POWELL'
        x = []
        ising = []
        qubo = []
        timer = []
        print('Powell, gnp topology, maximum clique, 7q rigetti qvm no noise')
        print(maximum_clique(G))
        for a in range(1, 50):
                x.append(a)
                start1 = time.clock()
                start2 = time.time()
                result_out = rigetti_ising_qubo(G, maximum_clique_qubo_rigetti, opt, top, a)
                diff2 = time.time()-start2
                diff1 = time.clock()-start1
                timer.append([diff1, diff2])
                ref = subg_is_clique(result_out, G)
                if ref == True:
                         qubo.append(result_out.count(1))
                else:
                         qubo.append(0)
                print(x, qubo, timer)
print(combined_test2())

