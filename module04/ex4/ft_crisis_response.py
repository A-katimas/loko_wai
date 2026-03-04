def crisis_handler(fd: str) -> None:
    try:
        with open(fd) as file:
            content = file.read().strip()

        print(f'SUCCESS: Archive recovered - "{content}"')
        print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")

    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")

    except Exception:
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis contained, archives protected\n")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    # lost
    crisis_handler("lost_archive.txt")

    # Permission denied file
    crisis_handler("classified_vault.txt")

    # Normal file
    print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
    crisis_handler("classified_data.txt")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
