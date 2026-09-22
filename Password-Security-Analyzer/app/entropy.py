import math
import string

def get_character_pool(password: str) -> int:
    pool = 0
    if any(c in string.ascii_lowercase for c in password):
        pool += 26
    if any(c in string.ascii_uppercase for c in password):
        pool += 26
    if any(c in string.digits for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    return pool

def calculate_entropy(password: str) -> float:
    pool = get_character_pool(password)
    if not password or pool == 0:
        return 0.0
    return round(len(password) * math.log2(pool), 2)
