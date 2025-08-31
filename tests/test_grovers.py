
from src import circuits

def test_grover_biases_target():
    counts = circuits.demo_grover_2qubit_oracle_target_11(shots=512)
    # Expect target "11" to be among top outcomes
    dominant = max(counts, key=counts.get)
    assert dominant in ["11"], f"Expected '11' to dominate, got {dominant}"
