def maximum_clique_qubo(G):
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
