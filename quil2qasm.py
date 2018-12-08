"""
This are limited scope quil to qasm converters - it only deals with Hadamard gates, CNOT operators, and the U1 gate (z axis rotation).
Takes input of a .txt file with quil code, outputs qasm code in a list
"""
def quil2qasm(name):
        file = open(name, 'r')
        x = file.readlines()
        #file2 = ['include "qelib1.inc";']
        for a in x:
                ref = list(a)
                out = ''
                for i in ref:
                        try:
                                x = int(i)
                                out = out+str(x)
                        except ValueError:
                                _ = 92
                if ref[0] == 'H':
                        file2.append('h q['+out+'];')
                allstring = ''
                for i in ref:
                        allstring = allstring+i
                lstring = allstring.split()
                if ref[0] == 'C':
                        file2.append('cx q['+lstring[1]+'],q['+lstring[2]+'];')
                if ref[0] == 'R':
                        strz1 = lstring[0]
                        strz2 = lstring[1]
                        splitstr = strz1.split('(')[1]
                        splitstr2 = splitstr.split(')')[0]
                        file2.append('u1('+str(splitstr2)+') q['+str(strz2)+'];')
        return file2
def quil2qasm_prog(name, qc, q, c):
        file = open(name, 'r')
        x = file.readlines()
        file2 = []
        for a in x:
                ref = list(a)
                out = ''
                for i in ref:
                        try:
                                x = int(i)
                                out = out+str(x)
                        except ValueError:
                                rand = 92
                if ref[0] == 'H':
                        qc.h(q[int(out)])
                        #file2.append('h q['+out+'];')
                allstring = ''
                for i in ref:
                        allstring = allstring+i
                lstring = allstring.split()
                if ref[0] == 'C':
                        qc.cx(q[int(lstring[1])], q[int(lstring[2])])
                        #file2.append('cx q['+lstring[1]+'],q['+lstring[2]+'];')
                if ref[0] == 'R':
                        strz1 = lstring[0]
                        strz2 = lstring[1]
                        splitstr = strz1.split('(')[1]
                        splitstr2 = splitstr.split(')')[0]
                        qc.u1(float(splitstr2), q[int(strz2)])
                        #file2.append('u1('+str(splitstr2)+') q['+str(strz2)+'];')
        return qc, q, c
