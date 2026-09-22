def masked_input_preview(password: str) -> str:
    return "*" * len(password)

def print_report(report: dict) -> None:
    print("\n" + "=" * 60)
    print("             PASSWORD SECURITY REPORT")
    print("=" * 60)
    print(f"Length        : {report['length']} characters")
    print(f"Score         : {report['score']}/{report['max_score']}")
    print(f"Strength      : {report['strength']}")
    print(f"Entropy       : {report['entropy']} bits")
    print(f"Character pool: {report['character_pool']}")
    print(f"Common        : {'YES' if report['is_common'] else 'NO'}")
    print(f"Sequential    : {'YES' if report['has_sequential_pattern'] else 'NO'}")
    print("\nCriteria:")
    for name, passed in report["criteria"].items():
        print(f"  {'[PASS]' if passed else '[FAIL]'} {name}")
    print("\nSuggestions:")
    if report["tips"]:
        for tip in report["tips"]:
            print(f"  - {tip}")
    else:
        print("  No basic improvements required.")
    print("=" * 60)
