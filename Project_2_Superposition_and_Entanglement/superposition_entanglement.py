# Import necessary libraries from Qiskit and other tools
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram

# Importing AerSimulator that provides a convenient interface to the most commonly used qasm_simulator
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Function to print results
def print_results(title, counts):
    print(f"{title}")
    for key, value in counts.items():
        print(f"{key}: {value}")
    print("\n")

# Creating a Quantum Circuit for Superposition

# Step 1: Initialize a Quantum Circuit with 1 qubit
qc_superposition = QuantumCircuit(1)  # Create a quantum circuit with 1 qubit

# Step 2: Apply the Hadamard gate to put the qubit in a superposition state
qc_superposition.h(0)  # Apply Hadamard gate to the first qubit

# Step 3: Visualize the superposition circuit
qc_superposition.draw(output='mpl')
plt.show()

# Step 4: Measure the qubit
qc_superposition.measure_all()

# Step 5: Initialize the AerSimulator
simulator = AerSimulator()

# Step 6: Transpile (i.e. optimize) the circuit for the simulator backend
compiled_circuit_superposition = transpile(qc_superposition, simulator)

# Step 7: Simulate the superposition circuit.
# "shots" refers to the number of times a quantum circuit is run to obtain measurement outcomes.
# The default number of shots is often set to 1024 (=2^10)
result_superposition = simulator.run(compiled_circuit_superposition, shots=1024).result()
counts_superposition = result_superposition.get_counts()

# Step 8: Plot the results of the superposition circuit
plot_histogram(counts_superposition)
plt.title("Superposition Results")
plt.show()

# Step 9: Print the results of the superposition circuit
print_results("Superposition Results", counts_superposition)

# Explanation: The Hadamard gate places the qubit in an equal superposition of |0⟩ and |1⟩.
# By measuring the qubit, we expect roughly equal counts of |0⟩ and |1⟩.


# Creating a Quantum Circuit for Entanglement (Bell State)

# Step 1: Initialize a Quantum Circuit with 2 qubits
qc_entanglement = QuantumCircuit(2)  # Create a quantum circuit with 2 qubits

# Step 2: Apply the Hadamard gate to the first qubit to create a superposition
qc_entanglement.h(0)  # Apply Hadamard gate to the first qubit

# Step 3: Apply the CNOT gate to entangle the first qubit with the second qubit
qc_entanglement.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1

# Step 4: Visualize the entanglement circuit
qc_entanglement.draw(output='mpl')
plt.show()

# Step 5: Measure both qubits
qc_entanglement.measure_all()

# Step 6: Transpile the circuit for the simulator backend
compiled_circuit_entanglement = transpile(qc_entanglement, simulator)

# Step 7: Simulate the entanglement circuit
result_entanglement = simulator.run(compiled_circuit_entanglement, shots=1024).result()
counts_entanglement = result_entanglement.get_counts()

# Step 8: Plot the results of the entanglement circuit
plot_histogram(counts_entanglement)
plt.title("Entanglement Results")
plt.show()

# Step 9: Print the results of the entanglement circuit
print_results("Entanglement Results", counts_entanglement)

# Explanation: The Hadamard gate puts the first qubit in superposition.
# The CNOT gate entangles the second qubit with the first. The result is a Bell state
# where the qubits are correlated, yielding results like |00⟩ and |11⟩ with equal probability.
