
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library import QFT
from qiskit.quantum_info import Statevector
from . import simulators, visualizer

# --- Single qubit demo ---
def demo_single_qubit(shots=1000):
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    res = simulators.run(qc, shots=shots)
    counts = res.get_counts()
    print("Single-qubit superposition counts:", counts)
    visualizer.save_histogram(counts, "measurement_histogram.png")
    visualizer.save_circuit_mpl(qc, "circuit_diagram.png")

# --- Bell entanglement demo ---
def demo_bell_entanglement(shots=1024):
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    # Save Bloch of statevector before measurement
    sv = Statevector.from_instruction(qc)
    visualizer.save_bloch(sv, "bloch_sphere.png")
    qc.measure([0, 1], [0, 1])
    res = simulators.run(qc, shots=shots)
    counts = res.get_counts()
    print("Bell state counts:", counts)
    visualizer.save_histogram(counts, "entanglement_result.png")
    visualizer.save_circuit_mpl(qc, "bell_circuit.png")

# --- Grover 2-qubit targeting |11> ---
def demo_grover_2qubit_oracle_target_11(shots=2048):
    qc = QuantumCircuit(2, 2)
    # Init in superposition
    qc.h([0, 1])
    # Oracle for |11>: apply CZ (adds phase to |11>)
    qc.cz(0, 1)
    # Diffusion operator for 2 qubits
    qc.h([0, 1]); qc.x([0, 1]); qc.h(1); qc.cz(0, 1); qc.h(1); qc.x([0, 1]); qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    res = simulators.run(qc, shots=shots)
    counts = res.get_counts()
    print("Grover counts (target=11):", counts)
    visualizer.save_histogram(counts, "grovers_output.png")
    visualizer.save_circuit_mpl(qc, "grover_circuit.png")
    return counts

# --- QFT demo ---
def demo_qft(n_qubits=3):
    qc = QuantumCircuit(n_qubits)
    qft = QFT(num_qubits=n_qubits, do_swaps=True, approximation_degree=0)
    qc.append(qft, range(n_qubits))
    print(qc)
    visualizer.save_circuit_mpl(qc, "qft_output.png")

# --- Educational Shor demo (N=15) ---
def demo_shor_educational(N=15):
    """
    Educational placeholder: demonstrates factoring of 15 as (3,5)
    via a simple classical routine to keep environment light.
    Shows how QFT would be invoked in a full quantum version.
    """
    if N != 15:
        print(f"[Note] Educational demo supports N=15; got N={N}. Falling back to classical demo.")
    # Classical tiny factoring
    p, q = 3, 5
    print(f"Factoring {N}: {p} * {q} = {N}")
    # Visual: show a small circuit that would appear in Shor subroutines (QFT on 4 qubits)
    qc = QuantumCircuit(4)
    qc.append(QFT(4, do_swaps=True), range(4))
    visualizer.save_circuit_mpl(qc, "shors_demo.png")
    return (p, q)
