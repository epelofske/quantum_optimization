from dwave_qbsolv import QBSolv
import dimod
from classical_solvers import *
from dwave.system.samplers import DWaveSampler
from graphs import *
from qubo_ising_generators import *
#from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

result = []
countx = []
for count in range(1, 30):
        countx.append(count)
        sampler = EmbeddingComposite(DWaveSampler())
        G = nx.gnp_random_graph(7, 0.5, 101)
        Q = maximum_clique_qubo_dwave(G)
        response = sampler.sample_qubo(Q, num_reads=count)
        #print(response)
#       print()
        val = []
        for i in response:
#               print(i)
                val.append(i)
#       print()
        interm = []
        for yv in val:
                out = []
                for a in yv:
                        out.append(yv[a])
                x = subg_is_clique(out, G)
                if x == True:
                        interm.append(out.count(1))
        result.append(max(interm))
        print(result)
        print(countx)

