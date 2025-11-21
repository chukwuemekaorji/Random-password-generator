import random
import string

def generate_password(length=12, use_upper=True, use_numbers=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ""
    numbers = string.digits if use_numbers else ""
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/" if use_symbols else ""

    all_chars = lower + upper + numbers + symbols

    if not all_chars:
        raise ValueError("No character sets were selected.")

    password = "".join(random.choice(all_chars) for _ in range(length))
    return password

def user_interface():
    print("\n=== PASSWORD GENERATOR TOOL ===")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_upper, use_numbers, use_symbols)

    print("\nGenerated password:")
    print(password)
    print("\nCopy and use!")

if __name__ == "__main__":
    user_interface()
