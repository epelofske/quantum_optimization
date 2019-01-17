from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
import networkx as nx
from graphs import *
from classical_solvers import *
import time

def combined_test2():
#        G = melbourne()
        G = nx.gnp_random_graph(8, 0.5, 101)
        top = '8q-noisy-qvm'
        opt = 'SLSQP'
        x = []
        ising = []
        qubo = []
        timer = []
        print('SLSQP, gnp, minimum vertex cover, 8q rigetti qvm noise')
        print(minimum_vertex_cover(G))
        for a in range(1, 50):
                x.append(a)
                start1 = time.clock()
                start2 = time.time()
                result_out = rigetti_ising_qubo(G, minimum_vertex_cover_qubo_rigetti, opt, top, a)
                diff2 = time.time()-start2
                diff1 = time.clock()-start1
                timer.append([diff1, diff2])
                ref = is_vertex_cover(result_out, G)
                if ref == True:
                         ising.append(result_out.count(1))
                else:
                         ising.append(0)
                print(x, ising)
print(combined_test2())
