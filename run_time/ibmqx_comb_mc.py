from utils.graphs import *
from utils.ibmqx_ising_qubo_qaoa import *
from utils.qubo_ising_generators import *
from utils.classical_solvers import *
import networkx as nx
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")

def ibqmx_qaoa(G, optimizer, func):
        x = []
        timer_main = []
        qubo_main = []
        for a in range(1, len(G)*2):
            x.append(a)
            qubo = []
            timer = []
            for avg in range(0, 10):
                start1 = time.clock()
                result_out = solve_ibmqx_ising_qubo(G, func, optimizer, a)
                diff1 = time.clock()-start1
                timer.append(diff1)
                result2 = []
                for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)
                ref = subg_is_clique(result2, G)
                if ref == True:
                  qubo.append(result2.count(1))
                else:
                  qubo.append(0)
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

opts = [SLSQP(), COBYLA(), NELDER_MEAD(), POWELL(), CG(), TNC(), L_BFGS_B()]
G = nx.gnp_random_graph(7, 0.5, 101)

for op in opts:
  print(op, ibqmx_qaoa(G, op, max_clique_qubo_matrix_ibmqx))
