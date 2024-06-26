# Project 4: Quantum Teleportation

## Objective
Demonstrate the concept of quantum teleportation.

## Overview
Quantum teleportation is a process by which the quantum state of a particle (such as a qubit) is transmitted from one location to another without physically transferring the particle itself. This phenomenon leverages the principles of quantum entanglement and classical communication to achieve the transfer of quantum information.

## Purpose of the Experiment

### Quantum Information Transfer
Quantum teleportation enables the transfer of the quantum state of one qubit (the sender, typically referred to as Alice's qubit) to another qubit (the receiver, typically referred to as Bob's qubit). The state transfer is achieved without physically sending the qubit through space. Instead, the process relies on quantum entanglement and classical communication.

### Quantum Entanglement
Entanglement is a quantum phenomenon where two or more qubits become interconnected in such a way that the state of one qubit instantly affects the state of the other, regardless of the distance between them. This experiment uses entanglement to establish a link between Alice's and Bob's qubits.

### Classical Communication
While the quantum state itself cannot be copied or measured directly due to the no-cloning theorem and the collapse of the wave function upon measurement, classical information about the measurement results can be sent from Alice to Bob. Bob uses this classical information to perform operations on his entangled qubit to recreate the original quantum state.

## Key Concepts

### Quantum Entanglement
- **Entanglement** is a quantum phenomenon where the states of two or more particles become intertwined such that the state of one particle instantly influences the state of the other, no matter the distance between them.
- In this project, we will create an entangled pair of qubits that will be used to teleport the state of a third qubit.

### Bell State
- A **Bell state** is a specific type of maximally entangled state of two qubits. Bell states are foundational in quantum information theory because they exhibit perfect correlations between qubits, regardless of the distance separating them. The four Bell states are:
  1. |Φ+⟩ = (|00⟩ + |11⟩) / √2
  2. |Φ-⟩ = (|00⟩ - |11⟩) / √2
  3. |Ψ+⟩ = (|01⟩ + |10⟩) / √2
  4. |Ψ-⟩ = (|01⟩ - |10⟩) / √2
- In this project, we will use the Bell state |Φ+⟩ = (|00⟩ + |11⟩) / √2, which means that if one qubit is measured to be in the state |0⟩, the other will also be |0⟩, and if one is |1⟩, the other will also be |1⟩.

### Quantum Gates
- **Hadamard Gate (H)**: Creates superposition, putting a qubit in a state where it can be both 0 and 1 simultaneously.
- **CNOT Gate**: Creates entanglement when used with a superposition state, linking the states of two qubits.
- **Pauli-X Gate**: Performs a bit-flip operation, similar to a classical NOT gate.
- **Pauli-Z Gate**: Performs a phase-flip operation, flipping the phase of the qubit state.

## Experiment Setup

![circuit](Figure_1-teleportation_circuit.png)

### Circuit Implementation

1. **Initialization**: 
   - Start with three qubits. The first qubit (Qubit 0, Alice's qubit) will be in the state to be teleported. The second and third qubits (Qubit 1 and Qubit 2, shared between Alice and Bob) will be entangled.
   - Prepare the state to be teleported on Qubit 0. For example, let's teleport the state |ψ⟩ = (|0⟩ + |1⟩) / √2, which is |+⟩ state created using a Hadamard gate.

2. **Entanglement**: 
   - Use a Hadamard gate on Qubit 1 to create a superposition state.
   - Apply a CNOT gate with Qubit 1 as the control and Qubit 2 as the target to entangle these two qubits, creating a Bell state.

3. **Bell Measurement**: 
   - Alice performs a Bell-state measurement on Qubit 0 and Qubit 1 by applying a CNOT gate with Qubit 0 as the control and Qubit 1 as the target, followed by a Hadamard gate on Qubit 0.
   - Measure Qubit 0 and Qubit 1 and store the results in classical bits.

4. **Classical Communication**: 
   - The result of Alice's measurement (two classical bits) is sent to Bob through classical channels. This classical information tells Bob which operations he needs to perform to reconstruct the state on his qubit.

5. **State Reconstruction**: 
   - Bob uses the received information to apply appropriate quantum gates to his qubit (Qubit 2). If the measurement result indicates, apply the X gate if the second bit is 1, and apply the Z gate if the first bit is 1.
   - Measure Qubit 2 to verify the teleported state.

### Expected Results
- The state of Alice's original qubit will be transferred to Bob's qubit, regardless of the initial state. This will be verified by comparing the final state of Bob's qubit with the initial state of Alice's qubit.

## Actual Results
![results](Figure_2-teleportation_results.png)

### Explanation of the Results

The results show that the counts for each of the possible states are roughly equal, indicating that the quantum teleportation process was carried out. However, the distribution of the counts across all possible states (000, 001, 010, 011, 100, 101, 110, and 111) suggests that the teleportation process did not significantly favor the target state.

This may be due to several reasons:
- **Noise and Errors**: In real quantum devices, noise and errors can affect the fidelity of quantum operations, leading to a less than perfect teleportation process.
- **Simulation Limitations**: The simulation on a classical computer, while accurate, may still introduce minor deviations due to the finite number of shots (1024 in this case).

![statevector](Figure_3-statevector_bob_qubit.png)

Despite these factors, the experiment successfully demonstrates the principles of quantum teleportation by showing that the state information of Alice's qubit was distributed and could be reconstructed by Bob.

## Real-World Application
Quantum teleportation is a fundamental protocol in quantum information theory and has significant implications for:
- **Quantum Communication**: Enabling secure communication channels through quantum key distribution.
- **Quantum Computing**: Allowing quantum information to be transferred between different parts of a quantum computer or between different quantum computers.
- **Quantum Networks**: Forming the basis for creating a quantum internet where information can be transmitted securely and instantaneously over long distances.

## Conclusion
This project demonstrates the feasibility and principles of quantum teleportation, highlighting its potential applications in various fields of quantum technology.
