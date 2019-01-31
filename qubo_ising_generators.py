"""
QUBO Generators from NetworkX Graph Objects

Max Cut QUBO formulation from 
https://www.sciencedirect.com/science/article/pii/S0166218X01003419 

Minimum Vertex Cover Ising formluations from 
https://arxiv.org/abs/1302.5843

Maximum clique and maximum indpendent set from
https://arxiv.org/pdf/1801.08649.pdf

"""
import numpy as np
import networkx as nx

def maximum_clique_qubo_rigetti(G):
        lin = []
        quad = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                lin.append(-1)
        for a in list(GC.edges()):
                quad[a] = 2
        return lin, quad
def maximum_clique_qubo_dwave(G):
        Q = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                Q[(i, i)] = -1
        for a in list(GC.edges()):
                Q[a] = 2
        return Q

def maximum_cut_qubo_rigetti(G):
        quad = {}
        lin = []
        for a in list(G.edges()):
                quad[a] = 2
        for i in list(G.nodes()):
                lin.append(-1*G.degree(i))
        return lin, quad
def maximum_cut_qubo_dwave(G):
        Q = {}
        for a in list(G.edges()):
                Q[a] = 2
        for i in list(G.nodes()):
                Q[(i, i)] = -1*G.degree(i)
        return Q

def minimum_vertex_cover_qubo_rigetti(G):
	J = {}
	h = []
	for a in list(G.edges()):
		J[a] = 2
	for i in list(G.nodes()):
		h.append((-2*G.degree(i))+1)
	return h, J
def minimum_vertex_cover_qubo_dwave(G):
	Q = {}
	for a in list(G.edges()):
		Q[a] = 2
	for i in list(G.nodes()):
		Q[(i, i)] = ((-1*G.degree(i))-1)
	return Q
def max_cut_qubo_matrix_ibmqx(G):
        qubo = maximum_cut_qubo_dwave(G)
        data = np.zeros((len(G), len(G)))
        for a in qubo:
                data[a[0], a[1]] = qubo[a]
                data[a[1], a[0]] = qubo[a]
        return data

def minimum_vertex_cover_qubo_matrix_ibmqx(G):
        h, J = minimum_vertex_cover_qubo_rigetti(G)
        data = np.zeros((len(G), len(G)))
        for a in J:
                data[a[0], a[1]] = J[a]
                data[a[1], a[0]] = J[a]
        count = -1
        for i in h:
                count += 1
                data[count, count] = i
        return data

def max_clique_qubo_matrix_ibmqx(G):
        qubo = maximum_clique_qubo_dwave(G)
        data = np.zeros((len(G), len(G)))
        for a in qubo:
                data[a[0], a[1]] = qubo[a]
                data[a[1], a[0]] = qubo[a]
        return data
