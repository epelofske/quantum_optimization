from dwave_qbsolv import QBSolv
import dimod
from classical_solvers import *
from dwave.system.samplers import DWaveSampler
from graphs import *
from qubo_ising_generators import *
#from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
"""
from dwave.cloud import Client
with Client.from_config() as client:
	for a in range(1, 2):
		G = nx.gnp_random_graph(7, 0.5, 101)
		Q = maximum_cut_qubo_dwave(G)
		solver = client.get_solver()
		computation = solver.sample_qubo(Q, num_reads=a)
		print(computation)
"""
#from dwave.system.samplers import DWaveSampler
#>>> from dwave.system.composites import EmbeddingComposite
result = []
countx = []
for count in range(1, 30):
	countx.append(count)
	sampler = EmbeddingComposite(DWaveSampler())
	G = nx.gnp_random_graph(7, 0.5, 101)
	Q = maximum_cut_qubo_dwave(G)
	response = sampler.sample_qubo(Q, num_reads=count)
	#print(response)
#	print()
	val = []
	for i in response:
#		print(i)
		val.append(i)
#	print()
	interm = []
	for yv in val:
		out = []
		for a in yv:
			out.append(yv[a])
		x = max_cut_value(out, G)
		interm.append(x)
	result.append(max(interm))
	print(result)
	print(countx)
#G = melbourne()

"""
G = nx.gnp_random_graph(7, 0.5, 101)
Q = maximum_cut_qubo_dwave(G)
response = QBSolv().sample_qubo(Q)
x = list(response.samples())
out = []
print()
for a in x:
	out = []
	for i in a:
		out.append(a[i])
	x = max_cut_value(out, G)
	print(x)
	#print(out.count(1))
"""
