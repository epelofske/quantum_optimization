"""
Each of these take an input of a Networkx graph object
They return a list of linear terms h,
and a dictionary of quadratic terms J
OR
a dictionary, Q, of h and J combined
"""
import networkx as nx
import dimod
def bqm_ising_to_hj(dictionary):
        hd = dictionary['linear']
        J = dictionary['quadratic']
        h = []
        for a in hd:
                h.append(hd[a])
        return h, J
def maximum_clique_qubo2(G):
        Ql = {}
        Qq = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                Ql[i] = -1
        for a in list(G.edges()):
                Qq[a] = 0
        for a in list(GC.edges()):
                Qq[a] = 2
        return Ql, Qq
def maximum_clique_ising(G):
        one, two = maximum_clique_qubo2(G)
        bqm = dimod.BinaryQuadraticModel(one, two, 0.0, dimod.BINARY)
        bqm_ising = bqm.change_vartype(dimod.SPIN, inplace=False)
        ising_m = vars(bqm_ising)
        h, J = bqm_ising_to_hj(ising_m)
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

def maximum_independent_set_qubo2(G):
        Ql = {}
        Qq = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                Ql[i] = -1
        for a in list(G.edges()):
                Qq[a] = 2
        for a in list(GC.edges()):
                Qq[a] = 0
        return Ql, Qq
def maximum_independent_ising(G):
        one, two = maximum_indpendent_set_qubo2(G)
        bqm = dimod.BinaryQuadraticModel(one, two, 0.0, dimod.BINARY)
        bqm_ising = bqm.change_vartype(dimod.SPIN, inplace=False)
        ising_m = vars(bqm_ising)
        h, J = bqm_ising_to_hj(ising_m)
        return h, J
def maximum_independent_set_qubo(G):
        Q = {}
        GC = nx.algorithms.operators.unary.complement(G)
        for i in list(G.nodes()):
                Q[(i, i)] = -1
        for a in list(GC.edges()):
                Q[a] = 0
        for a in list(G.edges()):
                Q[a] = 2
        return Q
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


