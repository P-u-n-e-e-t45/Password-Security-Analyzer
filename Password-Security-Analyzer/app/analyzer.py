from .common_passwords import is_common_password
from .entropy import calculate_entropy, get_character_pool
from .patterns import analyze_patterns, has_sequential_pattern

def check_password(password: str) -> dict:
    criteria = analyze_patterns(password)
    score = sum(criteria.values())
    common = is_common_password(password)
    sequential = has_sequential_pattern(password)

    if common:
        strength = "BLACKLISTED (extremely common password)"
    elif score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Fair"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    tips = []
    if not criteria["At least 12 characters (ideal)"]:
        tips.append("Use at least 12 characters.")
    if not criteria["Contains uppercase letter"]:
        tips.append("Add an uppercase letter.")
    if not criteria["Contains lowercase letter"]:
        tips.append("Add a lowercase letter.")
    if not criteria["Contains a number"]:
        tips.append("Add a number.")
    if not criteria["Contains a special symbol"]:
        tips.append("Add a special symbol.")
    if common:
        tips.append("Do not use this common password.")
    if sequential:
        tips.append("Avoid simple sequential patterns such as abc or 123.")

    return {
        "length": len(password),
        "score": score,
        "max_score": len(criteria),
        "strength": strength,
        "entropy": calculate_entropy(password),
        "character_pool": get_character_pool(password),
        "criteria": criteria,
        "is_common": common,
        "has_sequential_pattern": sequential,
        "tips": tips,
    }
