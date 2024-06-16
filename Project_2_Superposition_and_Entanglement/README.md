# Project 2: Superposition and Entanglement

## Objective

To explore superposition and entanglement

## Overview

- Create circuits that demonstrate superposition using the Hadamard gate and entanglement with Bell states.
- Visualize the results and understand the concepts.

## Getting Started

### Prerequisites
- Ensure that the necessary packages have been installed as outlined in the main repository README.

## Concepts and Explanations

### Superposition
- Also covered in Project 1, superposition is where a quantum bit (qubit) can exist in multiple states (|0⟩ and |1⟩) simultaneously.
- The Hadamard gate (H gate) is used to create superposition. It transforms the basis state |0⟩ into (|0⟩ + |1⟩)/√2 and |1⟩ into (|0⟩ - |1⟩)/√2.

### Entanglement
- Entanglement is a phenomenon where qubits become interconnected such that the state of one qubit directly influences the state of another.
- Bell states are specific quantum states of two qubits representing the simplest form of entanglement.

## Results

See the png files within the project folder to observe the results for both the superposition and entanglement experiments (as well as the graphical representations of the simple quantum circuits).

### Superposition Results

In the superposition experiment, a single qubit is put into a superposition state using the Hadamard gate. For reference, if we were to measure the state of the qubit without applying the gate, the qubit would always remain in its initial state (which is initialized by default in the state |0⟩). 

Here’s what happens in the phase of the experiment:

1. **Hadamard Gate Application**: The Hadamard gate transforms the qubit from state |0⟩ to a superposition state (|0⟩ + |1⟩)/√2.
2. **Measurement**: When measured, the qubit collapses to either |0⟩ or |1⟩ with equal probability (50%).

**Observed Results**:
- **Counts for |0⟩**: 514
- **Counts for |1⟩**: 510

These results are approximately equal, which is expected because the qubit was in a perfect superposition state. The slight difference between the counts (514 vs. 510) is due to the statistical nature of quantum measurements and the finite number of shots (1024). Ideally, with an infinite number of shots, the counts would converge to a 50/50 distribution.

### Entanglement Results

In the entanglement experiment, two qubits are entangled using a combination of the Hadamard gate and the CNOT gate to create a Bell state. Here’s what happens:

1. **Hadamard Gate Application on Qubit 0**: This puts qubit 0 in a superposition state (|0⟩ + |1⟩)/√2.
2. **CNOT Gate Application**: The CNOT gate uses qubit 0 as the control and qubit 1 as the target, entangling them. The resulting state is the Bell state (|00⟩ + |11⟩)/√2.

**Measurement**: When both qubits are measured, their states are perfectly correlated:
- If qubit 0 is measured as |0⟩, qubit 1 will also be |0⟩.
- If qubit 0 is measured as |1⟩, qubit 1 will also be |1⟩.

**Observed Results**:
- **Counts for |00⟩**: 517
- **Counts for |11⟩**: 507

These results show a near 50/50 distribution between the |00⟩ and |11⟩ states, indicating that the qubits are entangled. The counts are near equal because the entangled state (Bell state) ensures that the qubits always collapse to either both |0⟩ or both |1⟩ with equal probability. The slight difference between the counts for |00⟩ and |11⟩ in the entanglement experiment is due to the probabilistic nature of quantum measurements and the finite number of shots.

### Conclusion

- **Superposition**: The results from the superposition experiment (approximately equal counts for |0⟩ and |1⟩) confirm that the Hadamard gate successfully placed the qubit into a superposition state.
- **Entanglement**: The results from the entanglement experiment (equal counts for |00⟩ and |11⟩) confirm that the Hadamard and CNOT gates successfully created an entangled Bell state, demonstrating strong correlation between the two qubits.

These experiments illustrate fundamental principles of quantum mechanics and are essential steps towards understanding more complex quantum algorithms and phenomena.
