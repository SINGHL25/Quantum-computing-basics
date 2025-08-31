
import os
import matplotlib
matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector

PLOTS_DIR = "results/plots"

def ensure_dirs():
    os.makedirs(PLOTS_DIR, exist_ok=True)

def save_histogram(counts, filename="measurement_histogram.png"):
    ensure_dirs()
    fig = plot_histogram(counts)
    fig.savefig(os.path.join(PLOTS_DIR, filename), bbox_inches="tight")
    plt.close(fig)

def save_circuit_mpl(circuit, filename="circuit_diagram.png"):
    ensure_dirs()
    fig = circuit.draw(output="mpl")
    fig.savefig(os.path.join(PLOTS_DIR, filename), bbox_inches="tight")
    plt.close(fig)

def save_bloch(statevector: Statevector, filename="bloch_sphere.png"):
    ensure_dirs()
    fig = plot_bloch_multivector(statevector)
    fig.savefig(os.path.join(PLOTS_DIR, filename), bbox_inches="tight")
    plt.close(fig)
