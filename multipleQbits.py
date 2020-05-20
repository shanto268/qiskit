from qiskit import *
from math import pi
import numpy as np
from qiskit.visualization import plot_bloch_multivector, plot_histogram

qc = QuantumCircuit(3)
# Apply H-gate to each qubit:
for qubit in range(3):
    qc.h(qubit)
# See the circuit:
#qc.draw()

# Let's see the result
backend = Aer.get_backend('statevector_simulator')
final_state = execute(qc,backend).result().get_statevector()
print(final_state)

qc = QuantumCircuit(2)
qc.h(0)
qc.x(1)
#qc.draw()

backend = Aer.get_backend('unitary_simulator')
unitary = execute(qc,backend).result().get_unitary()

print(unitary)
