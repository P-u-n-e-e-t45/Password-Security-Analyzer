def search_space(password_length: int, character_pool: int) -> int:
    if password_length < 0 or character_pool < 0:
        raise ValueError("Length and character pool must be non-negative.")
    return character_pool ** password_length

def estimate_crack_time_seconds(
    password_length: int,
    character_pool: int,
    guesses_per_second: float = 1_000_000,
) -> float:
    if guesses_per_second <= 0:
        raise ValueError("guesses_per_second must be greater than zero.")
    return search_space(password_length, character_pool) / guesses_per_second

def format_duration(seconds: float) -> str:
    if seconds < 1:
        return f"{seconds:.4f} seconds"
    units = [
        ("years", 365.25 * 24 * 3600),
        ("days", 24 * 3600),
        ("hours", 3600),
        ("minutes", 60),
        ("seconds", 1),
    ]
    for name, size in units:
        if seconds >= size:
            return f"{seconds / size:.2f} {name}"
    return f"{seconds:.2f} seconds"
