
from qiskit import QuantumCircuit, Aer, execute

def run_grover():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])

    simulator = Aer.get_backend("qasm_simulator")
    result = execute(qc, simulator, shots=1000).result()
    counts = result.get_counts()

    print("Grover Search Result:", counts)
