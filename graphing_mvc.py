import matplotlib.pyplot as plt
import networkx as nx
import pylab
fig, ax = plt.subplots()

#ax = subplot(1,1,1)
#G = nx.gnp_random_graph(7, 0.5, 101)
#nx.draw(G, with_labels=True)
#ibmqx = [8, 8, 10, 9, 9, 8, 8, 8, 8, 8, 8, 10, 8, 8, 7, 8, 10, 8, 8, 8, 8, 8, 8, 8, 8, 6, 8, 7, 8]
#qvm_noise = [5, 0, 0, 8, 6, 8, 9, 8, 8, 9, 6, 8, 7, 8, 6, 5, 2, 7, 3, 5, 6, 6, 0, 7, 7, 0, 7, 4, 7]
#qvm_no = [8, 0, 7, 8, 2, 7, 4, 8, 8, 8, 2, 8, 8, 8, 6, 10, 9, 6, 6, 8, 8, 7, 8, 9, 8, 5, 8, 5, 8]
"""
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
ibmqx = [7, 0, 6, 6, 6, 5, 4, 5, 0, 0, 6, 4, 4, 4, 0, 5, 6, 5, 4, 5, 5, 0, 6, 5, 0, 0, 5, 5, 0]
qvm_no = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
qvm_noise = [0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 5, 7, 0, 0, 0, 0, 6, 6, 0, 0, 0, 0, 0, 0, 6, 0, 0]
"""
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
ibmqx = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0, 7, 0, 0]
qvm_no = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
qvm_noise = [0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 6, 0, 6, 0, 0, 0, 6, 4, 0, 0, 0, 0, 0]
print(len(ibmqx), len(qvm_no), len(qvm_noise))

y = []
for a in x:
	y.append(4)
ibmqx2 = []
for a in ibmqx:
	if a == 0:
		ibmqx2.append(7)
	else:
		ibmqx2.append(a)
qvm_no2 = []
for a in qvm_no:
        if a == 0:
                qvm_no2.append(7)
        else:
                qvm_no2.append(a)
qvm_noise2 = []
for a in qvm_noise:
        if a == 0:
                qvm_noise2.append(7)
        else:
                qvm_noise2.append(a)

plt.title('SLSQP optimizer, Maximum Vertex Cover, Graph gnp(7, 0.5, 101)', fontsize=20)
plt.plot(x, ibmqx2, 'og-', label='qasm_simulator no noise')
plt.plot(x, qvm_noise2, 'ob-', label='qvm noise')
plt.plot(x, qvm_no2, 'or-', label='qvm no noise')
plt.plot(x, y, 'm-', label='minimum vertex cover value')
plt.xlabel('Number of Steps', fontsize=20)
plt.ylabel('Found Solution Size', fontsize=20)
plt.legend(loc='upper right')

plt.rc('xtick')#, fontsize=20)
plt.rc('ytick')#, fontsize=20)
#font = {'family' : 'normal',
#        'weight' : 'bold',
#        'size'   : 20}
#font = {'size':20}
plt.rcParams.update({'font.size': 20})


#plt.plot(x, ibmqx2, 'og-', label='qasm_simulator no noise')
#plt.plot(x, qvm_noise2, 'ob-', label='qvm noise')
#plt.plot(x, qvm_no2, 'or-', label='qvm no noise')
#plt.plot(x, y, 'm-', label='minimum vertex cover value')

#plt.legend(loc='upper right')
#import numpy as np
#import pylab
#x = np.linspace(0, 20, 1000)
#y1 = np.sin(x)
#y2 = np.cos(x)

#pylab.plot(x, y1, '-b', label='sine')
#pylab.plot(x, y2, '-r', label='cosine')
#pylab.legend(loc='upper left')
#pylab.ylim(-1.5, 2.0)
#pylab.show()
ax.legend()
plt.show()
