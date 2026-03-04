import sys
import os


def readfile(file: str):

    try:
        with open(file, "r+") as fd:
            fd.read()
            fd.seek(0, os.SEEK_END)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError:", e)
        sys.exit(1)

    with open(file, "r") as fd:
        print(fd.read())


def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file = "ancient_fragment.txt"
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...\n")
    print("RECOVERED DATA")
    readfile(file)
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
