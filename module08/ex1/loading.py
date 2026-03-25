import os
import importlib.metadata

# Flags
HAS_PANDAS = True
HAS_NUMPY = True
HAS_MATPLOTLIB = True

try:
    import pandas as pd
except ImportError:
    HAS_PANDAS = False

try:
    import numpy as np
except ImportError:
    HAS_NUMPY = False

try:
    import matplotlib.pyplot as plt
except ImportError:
    HAS_MATPLOTLIB = False

# Couleurs
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def check_package(name):
    try:
        importlib.import_module(name)
        version = importlib.metadata.version(name)
        print(GREEN + f"[OK] {name} ({version})" + RESET)
        return True
    except Exception:
        print(RED + f"[MISSING] {name}" + RESET)
        return False


def detect_environment():
    if os.path.exists("pyproject.toml"):
        print(CYAN + "Environment: Poetry (pyproject.toml detected)" + RESET)
    if os.path.exists("requirements.txt"):
        print(CYAN + "Environment: pip (requirements.txt detected)" + RESET)
    else:
        print(YELLOW + "Environment: Unknown" + RESET)


def install_help():
    print(YELLOW + "\nTo install dependencies:" + RESET)
    print(CYAN + "pip install -r requirements.txt" + RESET)
    print(CYAN + "or" + RESET)
    print(CYAN + "poetry install" + RESET)


def main():

    print(GREEN + "LOADING STATUS: Loading programs...\n" + RESET)

    detect_environment()

    print("\nChecking dependencies:")

    all_ok = True

    if HAS_PANDAS:
        print(GREEN + "[OK] pandas" + RESET)
        pand = pd
    else:
        print(RED + "[MISSING] pandas" + RESET)
        all_ok = False
        pand = None

    if HAS_NUMPY:
        print(GREEN + "[OK] numpy" + RESET)
        numb = np
    else:
        print(RED + "[MISSING] numpy" + RESET)
        all_ok = False
        numb = None

    if HAS_MATPLOTLIB:
        print(GREEN + "[OK] matplotlib" + RESET)
        plot = plt
    else:
        print(RED + "[MISSING] matplotlib" + RESET)
        all_ok = False
        plot = None

    if not all_ok:
        print(RED + "\nERROR: Missing dependencies." + RESET)
        install_help()
        return

    # Imports après vérification

    print(GREEN + "\nAnalyzing Matrix data..." + RESET)

    # Simulation de données
    data = pand.DataFrame(
        {"time": numb.arange(100), "signal": numb.random.randn(100)}
    )

    print(CYAN + "Processing 1000 data points..." + RESET)

    # Graphique
    plot.figure()
    plot.plot(data["time"], data["signal"])
    plot.plot([0, 100], [-2, 2], color="green")
    plot.plot([50, 50], [2, 2.01], color="red")
    plot.title("Matrix Signal")
    plot.xlabel("Time")
    plot.ylabel("Signal")

    output_file = "matrix_analysis.png"
    plot.savefig(output_file)

    print(GREEN + "\nAnalysis complete!" + RESET)
    print(GREEN + f"Results saved to: {output_file}" + RESET)


if __name__ == "__main__":
    main()
