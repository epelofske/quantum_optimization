import networkx as nx
import itertools

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
def subg_is_clique(list, G):
	count = -1
	mc = []
	for i in list:
		count += 1
		if i == 1:
			mc.append(count)
	H = G.subgraph(mc)
	if is_clique(H) == True:
		return True
	else:
		return False
