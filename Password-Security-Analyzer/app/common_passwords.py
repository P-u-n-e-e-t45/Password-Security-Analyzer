from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "common_passwords.txt"

def load_common_passwords() -> set[str]:
    if not DATA_FILE.exists():
        return set()
    return {
        line.strip().lower()
        for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    }

COMMON_PASSWORDS = load_common_passwords()

def is_common_password(password: str) -> bool:
    return password.lower() in COMMON_PASSWORDS
