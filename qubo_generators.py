"""
Each of these take an input of a Networkx graph object
They return a list of linear terms h,
and a dictionary of quadratic terms J
OR
a dictionary, Q, of h and J combined
"""
import networkx as nx
def maximum_clique_ising(G):
        h = []
        J = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                h.append(-1)
        for a in list(G.edges()):
                J[a] = 0
        for a in list(GC.edges()):
                J[a] = 2
        return h, J
def maximum_clique_qubo(G):
        Q = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                Q[(i, i)] = -1
        for a in list(G.edges()):
                Q[a] = 0
        for a in list(GC.edges()):
                Q[a] = 2
        return Q
def maximum_independent_ising(G):
        h = []
        J = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                h.append(-1)
        for a in list(GC.edges()):
                J[a] = 0
        for a in list(G.edges()):
                J[a] = 2
        return h, J
def maximum_independent_qubo(G):
        Q = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                Q[(i, i)] = -1
        for a in list(GC.edges()):
                Q[a] = 0
        for a in list(G.edges()):
                Q[a] = 2
        return Q
def maximum_cut_ising(G):
        J = {}
        h = []
        for a in list(G.edges()):
                J[a] = 2
        for i in list(G.nodes()):
                h.append(-1*G.degree(i))
        return h, J
def maximum_cut_qubo(G):
        Q = {}
        for a in list(G.edges()):
                Q[a] = 2
        for i in list(G.nodes()):
                Q[(i, i)] = -1*G.degree(i)
        return Q
def vertex_cover_qubo(G):
        Q = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for a in list(G.edges()):
                Q[a] = 1
        for i in list(GC.edges()):
                Q[a] = 0
        for a in list(G.nodes()):
                Q[(a, a)] = -1
        return Q
def vertex_cover_ising(G):
        h = []
        J = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for a in list(G.edges()):
                J[a] = 1
        for i in list(GC.edges()):
                J[a] = 0
        for a in list(G.nodes()):
                h.append(-1)
        return h, J

