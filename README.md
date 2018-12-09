# quantum_optimization
The primary purpose of this project is to develop code to run optimization experiments on D-Wave devices and simulators, Rigetti devices and simulators, and IBM Quantum Experience devices and simulators. Specifically testing NP-Hard problems. 

If all of the required simulators and files are installed, running combined_qaoa_test.py will run an example of maximum clique on a clique of size 2. The results will be written to out2.txt. 

The required files can be downloaded from https://github.com/rigetti/grove, https://github.com/rigetti/pyquil, https://github.com/Qiskit/qiskit-terra, https://github.com/Qiskit/aqua. Additionally, the beta Rigetti QVM must be downloaded. Also, access to DWaveLeap must be implemented in order to compare to the Dwave 2000Q.
