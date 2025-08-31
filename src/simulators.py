
from qiskit import Aer, transpile
from qiskit.providers.backend import Backend
from qiskit.result import Result

def get_qasm_simulator() -> Backend:
    return Aer.get_backend("qasm_simulator")

def get_statevector_simulator() -> Backend:
    return Aer.get_backend("statevector_simulator")

def run(circuit, backend=None, shots=1024) -> Result:
    backend = backend or get_qasm_simulator()
    tcirc = transpile(circuit, backend)
    job = backend.run(tcirc, shots=shots)
    return job.result()
