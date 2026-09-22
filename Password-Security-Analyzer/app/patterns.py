import re

SPECIAL_PATTERN = r"""[!@#$%^&*()\-_=+\[\]{};:'",.<>?/\\|`~]"""

def analyze_patterns(password: str) -> dict[str, bool]:
    return {
        "At least 8 characters": len(password) >= 8,
        "At least 12 characters (ideal)": len(password) >= 12,
        "Contains uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Contains lowercase letter": bool(re.search(r"[a-z]", password)),
        "Contains a number": bool(re.search(r"\d", password)),
        "Contains a special symbol": bool(re.search(SPECIAL_PATTERN, password)),
    }

def has_sequential_pattern(password: str) -> bool:
    value = password.lower()
    for i in range(len(value) - 2):
        a, b, c = value[i:i+3]
        if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
            return True
        if ord(b) == ord(a) - 1 and ord(c) == ord(b) - 1:
            return True
    return False
