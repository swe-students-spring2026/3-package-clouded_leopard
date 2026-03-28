from pypass.passwords import (
    generate_password,
)

def main():
    password = generate_password(length=12, use_symbols=True, use_digits=True, use_upper=True, use_lower=True)
    print("Generated password:", password)

    # Add more examples below

if __name__ == "__main__":
    main()