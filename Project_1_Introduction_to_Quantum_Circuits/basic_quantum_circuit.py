from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a Quantum Circuit with one qubit and one classical bit
qc = QuantumCircuit(1, 1)

# Apply an X gate (NOT gate) to the qubit
qc.x(0)

# Measure the qubit and store the result in the classical bit
qc.measure(0, 0)

# Use Aer's qasm_simulator to simulate the circuit
simulator = Aer.get_backend('qasm_simulator')

# Transpile the circuit for the simulator
compiled_circuit = transpile(qc, simulator)

# Execute the circuit on the simulator
result = simulator.run(compiled_circuit).result()

# Get the counts (measurement outcomes)
counts = result.get_counts(compiled_circuit)
print("Measurement Results:", counts)

# Visualize the results using a histogram
plot_histogram(counts)
plt.show()

# Create a new Quantum Circuit for H and Z gates
qc_hz = QuantumCircuit(1, 1)

# Apply an H gate (Hadamard gate) to the qubit
qc_hz.h(0)

# Apply a Z gate (Pauli-Z gate) to the qubit
qc_hz.z(0)

# Measure the qubit and store the result in the classical bit
qc_hz.measure(0, 0)

# Transpile the circuit for the simulator
compiled_circuit_hz = transpile(qc_hz, simulator)

# Execute the circuit on the simulator
result_hz = simulator.run(compiled_circuit_hz).result()

# Get the counts (measurement outcomes)
counts_hz = result_hz.get_counts(compiled_circuit_hz)
print("Measurement Results after H and Z gates:", counts_hz)

# Visualize the results using a histogram
plot_histogram(counts_hz)
plt.show()
