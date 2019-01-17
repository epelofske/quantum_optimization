from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
import networkx as nx
from graphs import *
from classical_solvers import *
import time

def combined_test2():
#        G = nx.algorithms.operators.unary.complement(melbourne())
        G = nx.gnp_random_graph(8, 0.5, 101)
        top = '8q-qvm'
        opt = 'SLSQP'
        x = []
        ising = []
        qubo = []
        timer = []
        print('SLSQP, gnp, maximum clique, 8q rigetti qvm no noise')
        print(maximum_clique(G))
        for a in range(1, 50):
                #a = 10
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
                print(x, qubo)
print(combined_test2())
