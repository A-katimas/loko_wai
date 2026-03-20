import sys
import os
import site

# Codes couleur ANSI
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def is_venv():
    return sys.prefix != sys.base_prefix


def get_venv_name():
    return os.path.basename(sys.prefix)


def matrix_banner():
    print(
        GREEN
        + """
  __  __       _        _       
 |  \/  | __ _| |_ _ __(_)_  __ 
 | |\/| |/ _` | __| '__| \ \/ / 
 | |  | | (_| | |_| |  | |>  <  
 |_|  |_|\__,_|\__|_|  |_/_/\_\ 
"""
        + RESET
    )


def main():
    matrix_banner()

    if is_venv():
        print(GREEN + "MATRIX STATUS: Welcome to the construct" + RESET)

        print(CYAN + f"Current Python: {sys.executable}" + RESET)
        print(CYAN + f"Virtual Environment: {get_venv_name()}" + RESET)
        print(CYAN + f"Environment Path: {sys.prefix}" + RESET)

        print(GREEN + "\nSUCCESS: You're in an isolated environment!" + RESET)
        print(
            GREEN
            + "Safe to install packages without affecting the global system."
            + RESET
        )

        site_packages = site.getsitepackages()[0]
        print(YELLOW + "\nPackage installation path:" + RESET)
        print(YELLOW + site_packages + RESET)

    else:
        print(RED + "MATRIX STATUS: You're still plugged in" + RESET)

        print(CYAN + f"Current Python: {sys.executable}" + RESET)
        print(CYAN + "Virtual Environment: None detected" + RESET)

        print(RED + "\nWARNING: You're in the global environment!" + RESET)
        print(RED + "The machines can see everything you install." + RESET)

        print(YELLOW + "\nTo enter the construct, run:" + RESET)
        print(CYAN + "python -m venv matrix_env" + RESET)

        if os.name == " ":
            print(CYAN + "matrix_env\\Scripts\\activate" + RESET)
        else:
            print(CYAN + "source matrix_env/bin/activate" + RESET)

        print(YELLOW + "\nThen run this program again." + RESET)


if __name__ == "__main__":
    main()
