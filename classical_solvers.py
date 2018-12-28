import networkx as nx
import itertools
from graphs import *
def maximum_clique(G):
	return nx.algorithms.clique.graph_clique_number(G)
def maximum_independent_set(G):
	GC = nx.algorithms.operators.unary.complement(G)
	return nx.algorithms.clique.graph_clique_number(GC)
def minimum_vertex_cover(G):
        GC = nx.algorithms.operators.unary.complement(G)
        return len(G) - nx.algorithms.clique.graph_clique_number(GC)
def is_clique(G):
	n = len(G)
	m = len(G.edges())
	if m == ((n*(n-1))/2):
		return True
	else:
		return False
def max_cut_value(vector, G):
	count = -1
	subg1 = []
	subg2 = []
	for a in vector:
		count += 1
		if a == 1:
			subg1.append(count)
		if a != 1:
			subg2.append(count)
	H1 = G.subgraph(subg1)
	H2 = G.subgraph(subg2)
	m1 = len(H1.edges())
	m2 = len(H2.edges())
	val = len(G.edges())-(m1+m2)
	return val
def is_independent_set(vector, G):
        count = -1
        subg1 = []
        for a in vector:
                count += 1
                if a == 1:
                        subg1.append(count)
        H = G.subgraph(subg1)
        HC = nx.algorithms.operators.unary.complement(H)
        if is_clique(HC) == True:
                return True
        else:
                return False
def list_difference(list1, list2):
	out = []
	for a in list1:
		if a not in list2:
			out.append(a)
	return out
def is_vertex_cover(vector, G):
        count = -1
        subg1 = []
        for a in vector:
                count += 1
                if a == 1:
                        subg1.append(count)
        list1 = list(G.nodes())
        mis_subg = list_difference(list1, subg1)
        H = G.subgraph(mis_subg)
        HC = nx.algorithms.operators.unary.complement(H)
        if is_clique(HC) == True:
                return True
        else:
                return False
def maximum_cut(G):
	n = list(G.nodes())
	out = {}
	ref_length = []
	p = ''
	for i in n:
		p += str(i)
	m = list(G.edges())
	for length in range(1, len(G)):
		comb = itertools.combinations(p, length)
		for i in comb:
			subg1 = []
			subg2 = []
			for rem in i:
				subg1.append(int(rem))
			G1 = G.copy()
			for node in list(G.nodes()):
				if node not in subg1:
					subg2.append(node)
			H1 = G.subgraph(subg1)
			H2 = G.subgraph(subg2)
			m1 = len(H1.edges())
			m2 = len(H2.edges())
			val = len(G.edges())-(m1+m2)
			out[val] = [list(H1.nodes()), list(H2.nodes())]
#			print(val, list(H1.nodes()), list(H2.nodes()))
#	print(out)
	return max(out)
G = nx.Graph()
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(0, 3)
G.add_edge(2, 3)
G = nx.gnp_random_graph(7, 0.6)
GC = nx.algorithms.operators.unary.complement(G)
print(min_vertex_cover(G))
print(minimum_vertex_cover(G))
print(mc_solver(GC))
print(G.nodes())
#print(maximum_cut(G))

"""
file = open('graph2', 'w')
for a in list(G.edges()):
	file.write(str(a[0])+' '+str(a[1])+' 1\n')
"""
#nx.draw(G, with_labels=True)
#import matplotlib.pyplot as plt
#plt.show()
