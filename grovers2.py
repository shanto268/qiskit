import sys
from qiskit import QuantumRegister , ClassicalRegister , QuantumCircuit
from qiskit import compile , Aer
from qiskit.tools import visualization

# Make a quantum program for the n−bit Grover search . n=3
# Exactly−1 3−SAT formula to be satisfied , in conjunctive
# normal form. We represent literals with integers , positive or # negative to indicate a boolean variable or its negation .
exactly_1_3_sat_formula = [[1, 2, -3], [-1, -2, -3], [-1, 2, 3]]
# Define three quantum registers : ’f_in ’ is the search space (input # to the function f), ’f_out ’ is bit used for the output of function # f , aux are the auxiliary bits used by f to perform its
# computation.
f_in = QuantumRegister(n) 
f_out = QuantumRegister(1)
aux = QuantumRegister(len(exactly_1_3_sat_formula) + 1)
# One classical register to store the result of a measurement
ans = ClassicalRegister(n)
# Create quantum circuit with the quantum and classical registers # defined above
qc = QuantumCircuit(f_in, f_out, aux, ans, name='grover')
input_state(qc, f_in, f_out, n) # Apply two full iterations
black_box_u_f(qc, f_in , f_out , aux, n, exactly_1_3_sat_formula) 
inversion_about_average(qc, f_in , n)
black_box_u_f(qc, f_in , f_out , aux, n, exactly_1_3_sat_formula) 
inversion_about_average(qc, f_in , n)

# Measure the output register in the computational basis for j in range(n):
qc.measure(f_in[j], ans[j])
# Create an instance of the local quantum simulator quantum simulator = Aer.get backend(’qasm simulator py ’)
# Compile the circuit into ”quantum object code” that can be # executed on the simulator
qobj = compile(qc , quantum_simulator , shots=2048)
# Execute and store the results . Note that this could take some # time (up to a few minutes , depending on the machine)
job = quantum_simulator.run(qobj)
result = job.result() # Get counts
counts = result.get_counts('grover') 
print('Observed measurement outcomes: ')
print('string | count')

for key in sorted(counts):
    print(' {:>5s} {:d}'.format(key, counts[key])) # Plot histogram

figure = visualization.plot_histogram(counts)
print ()
# We can display the histogram with figure .show() if matplotlib is # properly configured . Instead , we write it to file .
figure.show()
