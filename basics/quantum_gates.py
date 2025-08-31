from qiskit import QuantumCircuit
import matplotlib.pyplot as plt

def demo_gates():
    qc = QuantumCircuit(1)
    qc.h(0)  # Hadamard Gate
    qc.x(0)  # Pauli-X
    qc.draw("mpl")
    plt.savefig("results/plots/gate_visualization.png")
    print("✅ Quantum gates visualization saved at results/plots/gate_visualization.png")

