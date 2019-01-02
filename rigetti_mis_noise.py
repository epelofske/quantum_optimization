from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
import networkx as nx
from graphs import *
from classical_solvers import *
import time

def combined_test2():
#        G = melbourne()
        G = nx.gnp_random_graph(7, 0.5, 101)
        top = '7q-noisy-qvm'
        opt = 'POWELL'
        x = []
        ising = []
        qubo = []
        timer = []
        print('Powell, gnp topology, maximum independent set, 7q rigetti qvm noise')
        print(maximum_independent_set(G))
        for a in range(1, 50):
                x.append(a)
                start1 = time.clock()
                start2 = time.time()
                result_out = rigetti_ising_qubo(G, maximum_independent_set_qubo_rigetti, opt, top, a)
                diff2 = time.time()-start2
                diff1 = time.clock()-start1
                timer.append([diff1, diff2])
                ref = is_independent_set(result_out, G)
                if ref == True:
                         qubo.append(result_out.count(1))
                else:
                         qubo.append(0)
                print(x, qubo)
print(combined_test2())

