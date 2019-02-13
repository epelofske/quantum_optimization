import networkx as nx
import random
from classical_solvers import *

def rand_partition(G):
    sampl = list(G.nodes())
    length = random.randint(0, max(sampl))
    part1 = random.sample(sampl, length)
    return part1

out = []
avg = 0
counter = 0
for i in range(0, 100):
  counter += 1
  G = nx.gnp_random_graph(7, 0.5, 101)
  subg1 = rand_partition(G)
  H = G.subgraph(subg1)
  val = is_clique(H)
  out.append(val)
  avg += val
  print((float(avg)/float(counter))/float(max(out)))
