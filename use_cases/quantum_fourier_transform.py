
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT

def run_qft():
    qc = QuantumCircuit(3)
    qft = QFT(3)
    qc.append(qft, [0,1,2])
    print("Quantum Fourier Transform Circuit:")
    print(qc)
