# Project 1: Introduction to Quantum Circuits

## Objective

To understand basic quantum gates and quantum circuits.

## Overview

- Install Qiskit and set up the environment.
- Create a basic quantum circuit with a single qubit.
- Apply basic quantum gates (X, H, Z) and measure the qubit.
- Visualize the circuit and the measurement results.

## Getting Started

### Prerequisites
- Ensure that the necessary packages have been installed as outlined in the main repository README.

## Concepts and Explanations

### Quantum Circuits

A quantum circuit is a model for quantum computation in which a computation is a sequence of quantum gates. These gates are reversible transformations on a quantum mechanical analog of an n-bit register. Quantum circuits are represented as a series of quantum operations (gates) applied to qubits, and can be visualized using circuit diagrams.

### Quantum Gates

Quantum gates are the basic building blocks of quantum circuits, similar to classical logic gates in traditional circuits. Each quantum gate represents a specific operation that can be performed on qubits. Below are the descriptions of the basic quantum gates used in this project:

#### X Gate (Pauli-X or NOT Gate)

- **Symbol:** X
- **Function:** The X gate flips the state of a qubit. It is equivalent to the classical NOT gate.
- **Matrix Representation:**
  \[
  X = \begin{pmatrix}
  0 & 1 \\
  1 & 0
  \end{pmatrix}
  \]
- **Operation:**
  - If the qubit is in state \( |0\rangle \), applying the X gate changes it to \( |1\rangle \).
  - If the qubit is in state \( |1\rangle \), applying the X gate changes it to \( |0\rangle \).

#### H Gate (Hadamard Gate)

- **Symbol:** H
- **Function:** The H gate creates a superposition state from a basis state. It transforms the qubit from basis states \( |0\rangle \) and \( |1\rangle \) into an equal superposition of these states.
- **Matrix Representation:**
  \[
  H = \frac{1}{\sqrt{2}} \begin{pmatrix}
  1 & 1 \\
  1 & -1
  \end{pmatrix}
  \]
- **Operation:**
  - If the qubit is in state \( |0\rangle \), applying the H gate changes it to \( \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \).
  - If the qubit is in state \( |1\rangle \), applying the H gate changes it to \( \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \).

#### Z Gate (Pauli-Z Gate)

- **Symbol:** Z
- **Function:** The Z gate applies a phase flip to the qubit. It leaves the \( |0\rangle \) state unchanged and flips the sign of the \( |1\rangle \) state.
- **Matrix Representation:**
  \[
  Z = \begin{pmatrix}
  1 & 0 \\
  0 & -1
  \end{pmatrix}
  \]
- **Operation:**
  - If the qubit is in state \( |0\rangle \), applying the Z gate leaves it in \( |0\rangle \).
  - If the qubit is in state \( |1\rangle \), applying the Z gate changes it to \( -|1\rangle \).

## Results

The visualizations can be found within this project folder. They show the behavior of the specified quantum gates on a single qubit:

- The measurement result after applying the X gate is `{'1': 1024}`, indicating that the qubit was in state `|1⟩` 1024 times out of 1024 trials, as expected after applying the X gate (which flipped the qubits state from 0 to 1)
- The measurement result after applying the H and Z gates is approximately `{'0': 500, '1': 524}`, indicating a nearly equal superposition state with a slight variation due to simulation precision. 

To explain the second experiment a bit further, H and Z Gates: Create an equal superposition state with a phase flip, leading to measurement results around `{'0': 512, '1': 512}` due to the equal probability of collapsing to `∣0⟩` or `∣1⟩`.
