from getpass import getpass
from .analyzer import check_password
from .report import masked_input_preview, print_report

def main() -> None:
    print("\n" + "=" * 60)
    print("             PASSWORD SECURITY ANALYZER")
    print("=" * 60)
    print("Defensive/educational password analysis tool.")
    print("Type 'quit' to exit.\n")

    while True:
        password = getpass("Enter a password to check: ")
        if password.lower() == "quit":
            print("\nGoodbye!")
            break
        if not password:
            print("Please enter a password.\n")
            continue
        report = check_password(password)
        print(f"\nPassword : {masked_input_preview(password)}")
        print_report(report)
        print()

if __name__ == "__main__":
    main()
