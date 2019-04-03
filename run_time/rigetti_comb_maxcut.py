from utils.rigetti_ising_qubo_qaoa import *
from utils.qubo_ising_generators import *
from utils.graphs import *
from utils.classical_solvers import *
import networkx as nx
import time

def qaoa_rigetti(G, opt, func):
        top = str(len(G))+'q-noisy-qvm'
        x = []
        timer_main = []
        qubo_main = []
        for a in range(1, (len(G)*2)+1):
            x.append(a)
            qubo = []
            timer = []
            for avg in range(0, 10):
                start1 = time.clock()
                result_out = rigetti_ising_qubo(G, func, opt, top, a)
                diff1 = time.clock()-start1
                timer.append(diff1)
                qubo.append(max_cut_value(result_out, G))
            t_avg = 0
            for i in timer:
              t_avg += i
            t_avg = float(float(t_avg)/float(10))
            q_avg = 0
            for i in qubo:
              q_avg += i
            q_avg = float(float(q_avg)/float(10))
            timer_main.append(t_avg)
            qubo_main.append(q_avg)
            print(x, qubo_main, timer_main)

opts = ['SLSQP', 'COBYLA', 'NELDER-MEAD', 'POWELL', 'CG', 'TNC', 'L-BFGS-B']
print('maxcut')
G = nx.gnp_random_graph(7, 0.5, 101)
for op in opts:
  print(op, qaoa_rigetti(G, op, maximum_cut_qubo_rigetti))
