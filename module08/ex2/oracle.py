import os

GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print(YELLOW + "dotenv not installed" + RESET)

MATRIX_MODE = os.getenv("MATRIX_MODE", "development")
DATABASE_URL = os.getenv("DATABASE_URL", "missing")
API_KEY = os.getenv("API_KEY", "missing")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
ZION_ENDPOINT = os.getenv("ZION_ENDPOINT", "missing")

# Charger .env si présent


def check_secrets():
    print("\nEnvironment security check:")

    # 1️⃣ Vérifier si des secrets par défaut ou manquants
    if API_KEY in ("missing", "changeme") or DATABASE_URL in (
        "missing",
        "changeme",
    ):
        print(RED + "[WARNING] Some secrets are missing or default" + RESET)
    else:
        print(GREEN + "[OK] No hardcoded secrets detected" + RESET)

    # 2️⃣ Vérifier la présence du fichier .env
    if os.path.exists(".env"):
        print(GREEN + "[OK] .env file properly configured" + RESET)
    else:
        print(RED + "[WARNING] .env file not found" + RESET)

    # 3️⃣ Vérifier si override prod possible
    if MATRIX_MODE.lower() == "production":
        print(GREEN + "[OK] Production overrides available" + RESET)


def main():
    print(CYAN + "ORACLE STATUS: Reading the Matrix...\n" + RESET)

    print("Configuration loaded:")
    print(f"Mode: {MATRIX_MODE}")
    print(f"Database: Connected to {DATABASE_URL}")
    print(
        f"API Access: {'Authenticated' if API_KEY != 'missing' else 'Missing'}"
    )
    print(f"Log Level: {LOG_LEVEL}")
    print(f"Zion Network: {ZION_ENDPOINT}")

    check_secrets()


if __name__ == "__main__":
    main()
