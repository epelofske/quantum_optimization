from quil2qasm import *
from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
from pyquil.api import get_qc
import networkx as nx
import numpy as np
from dwave_qbsolv import QBSolv
import dimod
from dwave.system.samplers import DWaveSampler
from qiskit import *
from qiskit_aqua.algorithms.components.optimizers import *

def mc_solver(G):
	x = list(nx.algorithms.clique.enumerate_all_cliques(G))
	length = []
	for a in x:
		length.append(len(a))
	maximum = max(length)
	out = []
	for i in x:
		if len(i) ==  maximum:
			out.append(i)
	return out
def analysis(given):
	main = []
	for a in given:
		if given[a] == 1:
			main.append(a)
	return main
def combined_test(file_name):
	result_file = open(file_name, 'w')
	G = nx.gnp_random_graph(2, 1)
	classical = mc_solver(G)
	print(classical)
	result_file.write('classical '+str(classical)+'\n')
	Q = maximum_clique_qubo(G)
	response = QBSolv().sample_qubo(Q)
	x = response.samples()
	resp = []
	for i in x:
		resp.append(analysis(i))
	print(resp)
	result_file.write('qubo qbsolv '+str(resp) + '\n')
	h, J = maximum_clique_ising_rigetti(G)
	response = QBSolv().sample_ising(h, J)
	x = response.samples()
	resp = []
	for i in x:
		resp.append(analysis(i))
	print(resp)
	result_file.write('ising qbsolv '+str(resp)+'\n')

	result_out = rigetti_ising_qubo(G, maximum_clique_qubo_rigetti, 'COBYLA')
	result_file.write('qubo rigetti '+str(result_out)+'\n')
	print(result_out)
	#IBMQ.load_accounts()

	result_out = rigetti_ising_qubo(G, maximum_clique_ising_rigetti, 'COBYLA')
	result_file.write('ising rigetti '+str(result_out)+'\n')
	print(result_out)

	optimizer = COBYLA()
	x = solve_ising_qubo(G, max_clique_qubo_matrix_ibmqx, optimizer)
	print(x)
	result_file.write('qubo ibmqx '+str(x)+'\n')

	x = solve_ising_qubo(G, max_clique_ising_matrix_ibmqx, optimizer)
	print(x)
	result_file.write('ising ibmqx '+str(x)+'\n')

	#sampler = DWaveSampler()
	#response = sampler.sample_qubo(Q, num_reads=1000)
	#result_file.write('Dwave QUBO'+str(response)+'\n')
	#print(response)
	#response2 = sampler.sample_ising(h, J, num_reads=1000)
	#result_file.write('Dwave ising'+str(response2)+'\n')
	#print(response2)

print(combined_test('out2.txt'))
