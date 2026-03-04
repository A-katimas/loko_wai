def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")

    try:
        with open("classified_data.txt", "r") as file:
            content_found = False
            for line in file:
                print(f"[CLASSIFIED] {line.strip()}")
                content_found = True

            if not content_found:
                print("[CLASSIFIED] Vault is empty")

    except FileNotFoundError:
        print("[CLASSIFIED] No classified data found")

    print("\nSECURE PRESERVATION:")

    try:
        with open("classified_data.txt", "a") as file:
            file.write("New security protocols archived\n")

        print("[CLASSIFIED] New security protocols archived")

    except Exception as error:
        print(f"Security breach detected: {error}")

    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
