import argparse
from src import circuits, simulators, visualizer


---

## 📌 `main.py`

```python
from basics import quantum_gates, superposition, entanglement
from use_cases import quantum_teleportation, grover_search, quantum_fourier_transform

if __name__ == "__main__":
    print("=== Quantum Computing Learning ===")
    quantum_gates.demo_gates()
    superposition.demo_superposition()
    entanglement.demo_entanglement()

    quantum_teleportation.run_teleportation()
    grover_search.run_grover()
    quantum_fourier_transform.run_qft()


def run_demo(demo):
    if demo == "qubit":
        circuits.demo_qubit()
    elif demo == "grover":
        circuits.demo_grover()
    elif demo == "shor":
        circuits.demo_shor()
    else:
        print("Demo not found!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Quantum Computing Demos")
    parser.add_argument("--demo", type=str, required=True,
                        help="Choose demo: qubit | grover | shor")
    args = parser.parse_args()
    run_demo(args.demo)

