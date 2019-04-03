import networkx as nx
import random

def rand_partition(G):
    sampl = list(G.nodes())
    length = random.randint(0, max(sampl))
    part1 = random.sample(sampl, length)
    part2 = []
    for a in sampl:
      if a not in part1:
        part2.append(a)
    return part1, part2
def cut_value(G, subg1, subg2):
  H1 = G.subgraph(subg1)
  H2 = G.subgraph(subg2)
  m1 = len(H1.edges())
  m2 = len(H2.edges())
  val = len(G.edges())-(m1+m2)
  return val

out = []
avg = 0
counter = 0
for i in range(0, 1000):
  counter += 1
  G = nx.gnp_random_graph(10, 0.5, 101)
  subg1, subg2 = rand_partition(G)
  val = cut_value(G, subg1, subg2)
  out.append(val)
  avg += val
  print((float(avg)/float(counter))/float(max(out)))
