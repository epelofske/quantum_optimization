from quil2qasm import *
from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
from pyquil.api import get_qc
import networkx as nx
import numpy as np
from dwave_qbsolv import QBSolv
from graphs import *
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
def is_clique(G):
	n = len(G)
	m = len(G.edges())
	if m == ((n*(n-1))/2):
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
def subg_is_clique2(list, G):
        H = G.subgraph(list)
        if is_clique(H) == True:
                return True
        else:
                return False

def ibmqx_run(file_name):
        result_file = open(file_name, 'w')
#        G = nx.gnp_random_graph(8, 0.6)
        G = nx.algorithms.operators.unary.complement(agave())
        print(G.edges())
        result_file.write('agave graph: '+str(list(G.edges()))+'\n')
        classical = mc_solver(G)
        print(classical)
        for i in classical:
             print(subg_is_clique2(i, G))
        result_file.write('classical '+str(classical)+'\n')
        for a in range(1, 25):
             optimizer = SLSQP()
             x = solve_ising_qubo(G, max_clique_qubo_matrix_ibmqx, optimizer, a)
             ref = subg_is_clique(x, G)
             print('qubo', a, x, ref)
             result_file.write(str(a)+'qubo ibmqx '+str(x)+str(ref)+'\n')
             x = solve_ising_qubo(G, max_clique_ising_matrix_ibmqx, optimizer, a)
             ref = subg_is_clique(x, G)
             print('ising', a, x, ref)
             result_file.write(str(a)+'ising ibmqx '+str(x)+str(ref)+'\n')
print(ibmqx_run('agave_ibmqx_no_noise.txt'))
def rigetti_run(file_name):
        result_file = open(file_name, 'w')
        #G = nx.gnp_random_graph(8, 0.6)
        G = nx.algorithms.operators.unary.complement(agave())
        print(G.edges())
        top = '8q-qvm'
        result_file.write('graph agave: '+str(list(G.edges()))+'\n')
        result_file.write('SLSQP,'+ top+'\n')
        classical = mc_solver(G)
        print(classical)
        for i in classical:
             print(subg_is_clique2(i, G))
        result_file.write('classical '+str(classical)+'\n')
        for a in range(1, 25):
                result_out = rigetti_ising_qubo(G, maximum_clique_qubo_rigetti, 'SLSQP', top, a)
                ref = subg_is_clique(result_out, G)
                result_file.write(str(a)+'qubo rigetti '+str(result_out)+str(ref)+'\n')
                print(a, 'qubo', result_out, ref)
                ref = subg_is_clique(result_out, G)
                result_out = rigetti_ising_qubo(G, maximum_clique_ising_rigetti, 'SLSQP', top, a)
                result_file.write(str(a)+'ising rigetti '+str(result_out)+str(ref)+'\n')
                print(a, 'ising', result_out, ref)
print(rigetti_run('agave_rigetti_no_noise.txt'))
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

       h, J = maximum_clique_ising_rigetti(G)
       Q = maximum_clique_qubo(G)
       sampler = DWaveSampler()
       response = sampler.sample_qubo(Q, num_reads=1000)
       result_file.write('Dwave QUBO'+str(response)+'\n')
       print(response)
       response2 = sampler.sample_ising(h, J, num_reads=1000)
       result_file.write('Dwave ising'+str(response2)+'\n')
       print(response2)


print(combined_test('out2.txt'))
