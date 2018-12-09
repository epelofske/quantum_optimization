from collections import OrderedDict
import numpy as np
from qiskit.quantum_info import Pauli
from qiskit_aqua import Operator
from qiskit_aqua.algorithms.adaptive import QAOA

def sample_most_likely(state_vector):
    if isinstance(state_vector, dict) or isinstance(state_vector, OrderedDict):
        binary_string = sorted(state_vector.items(), key=lambda kv: kv[1])[-1][0]
        x = np.asarray([int(y) for y in reversed(list(binary_string))])
        return x
    else:
        n = int(np.log2(state_vector.shape[0]))
        k = np.argmax(np.abs(state_vector))
        x = np.zeros(n)
        for i in range(n):
            x[i] = k % 2
            k >>= 1
        return x
def get_qubitops(input):
    w = np.array(input.tolist())
    num_nodes = len(w)
    pauli_list = []
    shift = 0
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            if w[i, j] != 0:
                xp = np.zeros(num_nodes, dtype=np.bool)
                zp = np.zeros(num_nodes, dtype=np.bool)
                zp[i] = True
                zp[j] = True
                pauli_list.append([w[i, j], Pauli(zp, xp)])
                shift += 1
    for i in range(num_nodes):
        degree = np.sum(w[i, :])
        xp = np.zeros(num_nodes, dtype=np.bool)
        zp = np.zeros(num_nodes, dtype=np.bool)
        zp[i] = True
        pauli_list.append([w[i, i], Pauli(zp, xp)])
    return Operator(paulis=pauli_list)
def solve_ising_qubo(G, matrix_func, optimizer):
	w = matrix_func(G)
	ops = get_qubitops(w)
	#optimizer = COBYLA()
	qaoa = QAOA(ops, optimizer, 2*len(G), operator_mode='matrix')
	qaoa.setup_quantum_backend(backend='statevector_simulator', shots=2)
	result = qaoa.run()
	x = sample_most_likely(result['eigvecs'][0])
	return x

