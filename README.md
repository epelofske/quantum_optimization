# quantum_optimization
The primary purpose of this project is to develop code to run optimization experiments on D-Wave devices and simulators, Rigetti devices and simulators, and IBM Quantum Experience devices and simulators. Specifically testing NP-Hard problems, in this case Maximum Clique, Maximum Cut, and Minimum Vertex Cover. In the case of the D-Wave 2000Q, the optimization is based on the process of quantum annealing. In the case, of the NISQ computers, the optimization algorithm used is the hybrid quantum-classical algorithm QAOA, which approximately solves such NP-Hard problems. 

The required files can be downloaded from https://github.com/rigetti/grove, https://github.com/rigetti/pyquil, https://github.com/Qiskit/qiskit-terra, https://github.com/Qiskit/aqua. Additionally, the beta Rigetti QVM must be downloaded. Also, access to D-WaveLeap must be implemented in order to compare to the D-Wave 2000Q, although it should be noted that none of these services are paid - as long as you are curious or a long term developer, this is trivial to sign up for these services. 

Extra information regarding this general topic of quantum computing can be found in the pdf file in this repository called References_and_Code (4).

Scripts which include nisq in the name access an IBM NISQ device.
