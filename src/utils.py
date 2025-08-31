
import os
import json
import argparse

NOTEBOOKS = {
    "01_qubit_basics.ipynb": [
        "# Qubit Basics",
        "from src.circuits import demo_single_qubit\n",
        "demo_single_qubit()"
    ],
    "02_superposition_entanglement.ipynb": [
        "# Superposition & Entanglement",
        "from src.circuits import demo_bell_entanglement\n",
        "demo_bell_entanglement()"
    ],
    "03_quantum_gates.ipynb": [
        "# Quantum Gates",
        "from src.circuits import demo_single_qubit\n",
        "demo_single_qubit()"
    ],
    "04_grovers_algorithm.ipynb": [
        "# Grover's Algorithm (2-qubit toy)",
        "from src.circuits import demo_grover_2qubit_oracle_target_11\n",
        "demo_grover_2qubit_oracle_target_11()"
    ],
    "05_shors_algorithm.ipynb": [
        "# Shor's Algorithm (Educational Demo for N=15)",
        "from src.circuits import demo_shor_educational\n",
        "demo_shor_educational(15)"
    ],
    "06_quantum_fourier.ipynb": [
        "# Quantum Fourier Transform",
        "from src.circuits import demo_qft\n",
        "demo_qft(3)"
    ]
}

def write_notebook(path, title, code_lines):
    nb = {
        "cells":[
            {"cell_type":"markdown","metadata":{},"source":[title]},
            {"cell_type":"code","metadata":{},"source":code_lines,"execution_count":None,"outputs":[]}
        ],
        "metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"}},
        "nbformat":4,"nbformat_minor":5
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)

def make_notebooks():
    os.makedirs("notebooks", exist_ok=True)
    for fname, lines in NOTEBOOKS.items():
        write_notebook(os.path.join("notebooks", fname), lines[0], lines[1:])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--make-notebooks", action="store_true")
    args = parser.parse_args()
    if args.make_notebooks:
        make_notebooks()
        print("Notebooks created in notebooks/")
