from grove.ising.ising_qaoa import ising
import sys
import os
from contextlib import contextmanager
from pyquil.api._qvm import QVM
from pyquil.api import QuantumComputer, get_qc
@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
def unique(input):
        output = []
        for x in input:
                if x not in output:
                        output.append(x)
        return output

def rigetti_ising_qubo(G, func, optimizer, comp, p):
        qc = get_qc(comp)
        h, J = func(G)
        with suppress_stdout():
                x, z = ising(h, J, num_steps=p, connection=qc, samples = 100, minimizer_kwargs = {'method': optimizer})
        """
        possible methods: COBYLA, SLSQP, TNC, CG, BFGS, Powell, Nelder-Mead, L-BFGS-B
        """
        return x
        out = unique(x)
        result_out = {}
        for a in out:
                temp = ''
                for inter_ in a:
                        temp += str(inter_)
                result_out[temp] = x.count(a)
        return result_out
