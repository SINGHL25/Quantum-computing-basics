
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def demo_qubit():
    qc = QuantumCircuit(1,1)
    qc.h(0)         # Hadamard gate: put qubit in superposition
    qc.measure(0,0)
    
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts()
    
    print("Measurement results:", counts)
    plot_histogram(counts)
    plt.savefig("results/plots/measurement_histogram.png")
    plt.show()
