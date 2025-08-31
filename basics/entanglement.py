
from qiskit import QuantumCircuit, Aer, execute

def demo_entanglement():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1],[0,1])

    simulator = Aer.get_backend("qasm_simulator")
    result = execute(qc, simulator, shots=1000).result()
    counts = result.get_counts()

    print("Entanglement Result:", counts)
