# Import necessary libraries from Qiskit and other tools
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Define the Oracle
# create_oracle function creates an oracle that flips the phase of the target state.
def create_oracle(n, target_state):
    oracle = QuantumCircuit(n)
    # Convert the target state to binary
    target_bin = f'{target_state:0{n}b}'
    # Apply X gates to the qubits where the target state has a 0
    for qubit, bit in enumerate(reversed(target_bin)):
        if bit == '0':
            oracle.x(qubit)
    # Apply the multi-controlled Z gate
    oracle.h(n-1)
    oracle.mcx(list(range(n-1)), n-1)
    oracle.h(n-1)
    # Revert the X gates to restore the qubits
    for qubit, bit in enumerate(reversed(target_bin)):
        if bit == '0':
            oracle.x(qubit)
    oracle_gate = oracle.to_gate()
    oracle_gate.name = "Oracle"
    return oracle_gate

# Define the Diffusion Operator
# create_diffusion_operator function creates the Grover diffusion operator
# that amplifies the probability amplitude of the target state.
def create_diffusion_operator(n):
    diffusion = QuantumCircuit(n)
    diffusion.h(range(n))  # Apply Hadamard to all qubits
    diffusion.x(range(n))  # Apply X to all qubits
    diffusion.h(n-1)  # Apply Hadamard to the last qubit
    diffusion.mcx(list(range(n-1)), n-1)  # Multi-controlled Z gate
    diffusion.h(n-1)  # Apply Hadamard to the last qubit
    diffusion.x(range(n))  # Apply X to all qubits
    diffusion.h(range(n))  # Apply Hadamard to all qubits
    diffusion_gate = diffusion.to_gate()
    diffusion_gate.name = "Diffusion"
    return diffusion_gate

# Initialize the Circuit
# the quantum circuit is initialized with Hadamard gates to put the qubits in a superposition state.
n = 3  # Number of qubits
target_state = 5  # Target state to be searched (binary 101)
grover_circuit = QuantumCircuit(n)
grover_circuit.h(range(n))  # Initialize in superposition

# The oracle and diffusion operators are appended to the circuit.
# Apply the Oracle
grover_circuit.append(create_oracle(n, target_state), range(n))

# Apply the Diffusion Operator
grover_circuit.append(create_diffusion_operator(n), range(n))

# Measure the Qubits
# The qubits are measured to collapse their states, revealing the target state with high probability.
grover_circuit.measure_all()
grover_circuit.draw(output='mpl')
plt.show()

# Simulate the Circuit
# The circuit is simulated using Qiskit's AerSimulator, and the results are plotted and printed.
simulator = AerSimulator()
compiled_circuit = transpile(grover_circuit, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()
counts = result.get_counts()

# Plot the Results
plot_histogram(counts)
plt.title("Grover's Algorithm Results")
plt.show()

# Print the Results
print("Results of Grover's Algorithm:")
print(counts)
