
from qiskit import QuantumCircuit, Aer, execute

def run_teleportation():
    qc = QuantumCircuit(3, 3)
    qc.h(1)
    qc.cx(1, 2)
    qc.cx(0, 1)
    qc.h(0)
    qc.measure([0,1], [0,1])
    qc.cx(1, 2)
    qc.cz(0, 2)
    qc.measure(2, 2)

    simulator = Aer.get_backend("qasm_simulator")
    result = execute(qc, simulator, shots=1000).result()
    counts = result.get_counts()

    print("Teleportation Result:", counts)
