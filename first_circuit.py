############################################################
#                                                          #
#                       ALINA ABANDEH                     #
#                                                          #
# File: fist_circuit.py                                   #
# Author: Alina Abandeh                                   #
# Created: 2026-09-07                                     #
# Last Modified: 2026-09-07                               #
# Description:                                             #
#                                                          #
############################################################

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)
# Put qubit 0 into superposition (mix of 0 and 1)
qc.h(0)
# Entangle qubit 0 with qubit 1 - measuring one affects the other
qc.cx(0, 1)
qc.measure([0,1], [0,1])

print(qc.draw())
 
sim = AerSimulator()
result = sim.run(qc).result()
print(result.get_counts())
