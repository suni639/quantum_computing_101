# Import necessary libraries from Qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

# Initialize the Quantum Circuit
# Create a Quantum Circuit with 3 qubits and 3 classical bits
circuit = QuantumCircuit(3, 3)

# Step 1: Prepare the state to be teleported on Qubit 0
# For example, let's teleport the state |ψ⟩ = (|0⟩ + |1⟩) / √2, which is |+⟩ state
circuit.h(0)

# Step 2: Create entanglement between Qubit 1 and Qubit 2
circuit.h(1)          # Hadamard gate on Qubit 1
circuit.cx(1, 2)      # CNOT gate with control on Qubit 1 and target on Qubit 2

# Step 3: Alice performs a Bell-state measurement on Qubit 0 and Qubit 1
circuit.cx(0, 1)      # CNOT gate with control on Qubit 0 and target on Qubit 1
circuit.h(0)          # Hadamard gate on Qubit 0
circuit.barrier()

# Measure Qubit 0 and Qubit 1 and store the results in classical bits 0 and 1
circuit.measure([0, 1], [0, 1])
circuit.barrier()

# Step 4: Bob applies the appropriate gates to Qubit 2 based on the classical bits received from Alice
# Apply X gate to Qubit 2 if classical bit 1 is 1
circuit.x(2).c_if(circuit.clbits[1], 1)

# Apply Z gate to Qubit 2 if classical bit 0 is 1
circuit.z(2).c_if(circuit.clbits[0], 1)

# Measure Qubit 2 to verify the teleported state
circuit.measure(2, 2)

# Draw the circuit
circuit.draw(output='mpl')
plt.show()

# Simulate the Circuit
simulator = AerSimulator()
compiled_circuit = transpile(circuit, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()

# Get the counts of the results
counts = result.get_counts()
plot_histogram(counts)
plt.title("Quantum Teleportation Results")
plt.show()

# Print the counts
print("Results of Quantum Teleportation:")
print(counts)

# Additional visualization: Statevector plot of Bob's qubit
# Remove measurements and classical control for statevector simulation
circuit_statevector = QuantumCircuit(3)
circuit_statevector.h(0)
circuit_statevector.h(1)
circuit_statevector.cx(1, 2)
circuit_statevector.cx(0, 1)
circuit_statevector.h(0)
circuit_statevector.cx(1, 2)
circuit_statevector.cz(0, 2)

# Get the statevector
statevector_simulator = Aer.get_backend('statevector_simulator')
statevector_result = statevector_simulator.run(circuit_statevector).result()
statevector = statevector_result.get_statevector()

# Plot the Bloch sphere of Bob's qubit
plot_bloch_multivector(statevector)
plt.title("Statevector of Bob's Qubit After Teleportation")
plt.show()
