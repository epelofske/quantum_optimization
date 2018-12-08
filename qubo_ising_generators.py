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
def analysis(given):
        main = []
        for a in given:
                if given[a] == 1:
                        main.append(a)
        return main
G = nx.gnp_random_graph(10, 0.6)

print('Maximum Cut:')
Q = maximum_cut_qubo(G)
response = QBSolv().sample_qubo(Q)
x = response.samples()
resp = []
for i in x:
	resp.append(analysis(i))
print(resp)
h, J = maximum_cut_ising(G)
response = QBSolv().sample_ising(h, J)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)

print('Maximum Clique:')
Q = maximum_clique_qubo(G)
response = QBSolv().sample_qubo(Q)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)
h, J = maximum_clique_ising(G)
response = QBSolv().sample_ising(h, J)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)

print('Minimum Vertex Cover:')
Q = vertex_cover_qubo(G)
response = QBSolv().sample_qubo(Q)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)
h, J = vertex_cover_ising(G)
response = QBSolv().sample_ising(h, J)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)

print('Maximum Independent Set:')
Q = maximum_independent_set_qubo(G)
response = QBSolv().sample_qubo(Q)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)
h, J = maximum_independent_set_ising(G)
response = QBSolv().sample_ising(h, J)
x = response.samples()
resp = []
for i in x:
        resp.append(analysis(i))
print(resp)




