from pypass.passwords import (
    generate_password,
    password_save,
    password_strength,
    validate_password,
)

def main():
    print("=== generate_password examples ===")
    print("1) Default settings")
    generated_default = generate_password()
    print(generated_default)

    print("2) Custom length 20")
    generated_length_20 = generate_password(length=20)
    print(generated_length_20)

    print("3) Upper + lower only")
    generated_upper_lower = generate_password(
        use_lower=True,
        use_upper=True,
        use_digits=False,
        use_symbols=False,
    )
    print(generated_upper_lower)

    print("\n=== validate_password examples ===")
    print("1) Valid password 'Abc123!' with min_length=6, require_symbols=True")
    print(
        validate_password("Abc123!", min_length=6, require_symbols=True),
    )
    print("2) Too short password 'Ab1!' with min_length=8")
    print(
        validate_password(
            "Ab1!",
            min_length=8,
        ),
    )
    print("3) Missing uppercase in 'abc123!' with require_uppercase=True")
    print(
        validate_password(
            "abc123!",
            require_uppercase=True,
        ),
    )

    print("\n=== password_strength examples ===")
    print("1) Strength for 'Abc123!'")
    print(password_strength("Abc123!"))
    print("2) Strength for 'ABCDEFGHIJ'")
    print(password_strength("ABCDEFGHIJ"))
    print("3) Strength for '!@#$%^&*()'")
    print(password_strength("!@#$%^&*()"))

    print("\n=== password_save examples ===")
    print("1) Save to default path")
    print(
        password_save(password="Abc123!"),
    )

    save_path = "saved.txt"
    print("2) Save to custom path")
    print(
        password_save(password="Abc123!", path=save_path),
    )

if __name__ == "__main__":
    main()