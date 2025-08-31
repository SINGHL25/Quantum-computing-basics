import argparse
from src import circuits, simulators, visualizer

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

