
from src import circuits

def test_qubit_runs():
    circuits.demo_single_qubit(shots=100)
    assert True

def test_bell_runs():
    circuits.demo_bell_entanglement(shots=100)
    assert True
