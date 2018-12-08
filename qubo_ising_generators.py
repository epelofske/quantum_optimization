import networkx as nx
from dwave_qbsolv import QBSolv
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
        return Ql, Qq
def maximum_independent_set_ising(G):
        one, two = maximum_independent_set_qubo2(G)
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
        for a in list(G.edges()):
                Q[a] = 2
        return Q
def maximum_cut_qubo2(G):
        Q = {}
        Q1 = {}
        for a in list(G.edges()):
                Q[a] = 2
        for i in list(G.nodes()):
                Q1[i] = -1*G.degree(i)
        return Q1, Q
def maximum_cut_ising(G):
        one, two = maximum_cut_qubo2(G)
        bqm = dimod.BinaryQuadraticModel(one, two, 0.0, dimod.BINARY)
        bqm_ising = bqm.change_vartype(dimod.SPIN, inplace=False)
        ising_m = vars(bqm_ising)
        h, J = bqm_ising_to_hj(ising_m)
        return h, J
def maximum_cut_qubo(G):
        Q = {}
        for a in list(G.edges()):
                Q[a] = 2
        for i in list(G.nodes()):
                Q[(i, i)] = -1*G.degree(i)
        return Q
def vertex_cover_ising(G):
	J = {}
	h = []
	for a in list(G.edges()):
		J[a] = 2
	for i in list(G.nodes()):
		h.append((-1*G.degree(i))-1)
	return h, J
def vertex_cover_ising2(G):
        J = {}
        h = {}
        for a in list(G.edges()):
                J[a] = 2
        for i in list(G.nodes()):
                h[i] = (-1*G.degree(i))-1
        return h, J
def bqm_to_qubo(q):
	lin = q['linear']
	quad = q['quadratic']
	out = {}
	for a in lin:
		quad[(a, a)] = lin[a]
	return quad
def vertex_cover_qubo(G):
        one, two = vertex_cover_ising2(G)
        bqm = dimod.BinaryQuadraticModel(one, two, 0.0, dimod.SPIN)
        bqm_q = bqm.change_vartype(dimod.BINARY, inplace=False)
        q = vars(bqm_q)
        Q = bqm_to_qubo(q)
        return Q
def max_cut_qubo_matrix(G):
        qubo = maximum_cut_qubo(G)
        data = np.zeros((len(G), len(G)))
        for a in qubo:
                data[a[0], a[1]] = qubo[a]
                data[a[1], a[0]] = qubo[a]
        return data
def max_cut_ising_matrix(G):
        h, J = maximum_cut_ising(G)
        data = np.zeros((len(G), len(G)))
        for a in J:
                data[a[0], a[1]] = J[a]
                data[a[1], a[0]] = J[a]
        count = -1
        for i in h:
                count += 1
                data[count, count] = i
        return data
def min_vertex_cover_qubo_matrix(G):
        qubo = vertex_cover_qubo(G)
        data = np.zeros((len(G), len(G)))
        for a in qubo:
                data[a[0], a[1]] = qubo[a]
                data[a[1], a[0]] = qubo[a]
        return data
def min_vertex_cover_ising_matrix(G):
        h, J = vertex_cover_ising(G)
        data = np.zeros((len(G), len(G)))
        for a in J:
                data[a[0], a[1]] = J[a]
                data[a[1], a[0]] = J[a]
        count = -1
        for i in h:
                count += 1
                data[count, count] = i
        return data
def max_independent_set_qubo_matrix(G):
        qubo = maximum_independent_set_qubo(G)
        data = np.zeros((len(G), len(G)))
        for a in qubo:
                data[a[0], a[1]] = qubo[a]
                data[a[1], a[0]] = qubo[a]
        return data
def max_independent_set_ising_matrix(G):
        h, J = maximum_independent_set_ising(G)
        data = np.zeros((len(G), len(G)))
        for a in J:
                data[a[0], a[1]] = J[a]
                data[a[1], a[0]] = J[a]
        count = -1
        for i in h:
                count += 1
                data[count, count] = i
        return data
def max_clique_qubo_matrix(G):
        qubo = maximum_clique_qubo(G)
        data = np.zeros((len(G), len(G)))
        for a in qubo:
                data[a[0], a[1]] = qubo[a]
                data[a[1], a[0]] = qubo[a]
        return data
def max_clique_ising_matrix(G):
        h, J = maximum_clique_ising(G)
        data = np.zeros((len(G), len(G)))
        for a in J:
                data[a[0], a[1]] = J[a]
                data[a[1], a[0]] = J[a]
        count = -1
        for i in h:
                count += 1
                data[count, count] = i
        return data


