import os


def main():

    file = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")

    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("[ENTRY 001] New quantum algorithm discovered\n")
            f.write("[ENTRY 002] Efficiency increased by 347%\n")
            f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
        print("Storage unit created successfully...\n")
    else:
        print("the file already exist\n")
        pass
    print("Inscribing preservation data...")
    with open(file, "r") as fd:
        print(fd.read())

    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    main()
