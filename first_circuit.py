############################################################
#                                                          #
#                       ALINA ABANDEH                     #
#                                                          #
# File: fist_circuit.py                                   #
# Author: Alina Abandeh                                   #
# Created: 2026-09-07                                     #
# Last Modified: 2026-09-07                               #
# Description:Demonstrates superposition and quantum      #
# entanglement using Qiskit.                              #
#                                                          #
############################################################

from qiskit import QuantumCircuit

from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Build the circuit: 2 qubits, 2 classical bits to store measurement results
qc = QuantumCircuit(2, 2)

# Put qubit 0 into superposition (a mix of 0 and 1 at the same time)
qc.h(0)

# Entangle qubit 0 with qubit 1 - measuring one instantly affects the other
qc.cx(0, 1)

# Measure both qubits and store results in the classical bits
qc.measure([0, 1], [0, 1])

# Print an ASCII diagram of the circuit to the terminal
print(qc.draw())

# Save a proper image of the circuit diagram
qc.draw(output='mpl', filename='circuit.png')

# Run the circuit on a local simulator (pretends to be a quantum computer)
sim = AerSimulator()
result = sim.run(qc).result()
counts = result.get_counts()

# Print the raw measurement counts
print(counts)

# Save a histogram image of the results
plot_histogram(counts, filename='results.png')
