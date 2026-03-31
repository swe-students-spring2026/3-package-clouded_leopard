import random
import string

def generate_password(
    length: int = 12,
    use_lower: bool = True,
    use_upper: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generate a password based on the selected character categories and length.
    The generated password guarantees at least one character from each selected category.
    """

    if length <= 0:
        raise ValueError("length must be greater than 0")

    categories = []

    if use_lower:
        categories.append(string.ascii_lowercase)
    if use_upper:
        categories.append(string.ascii_uppercase)
    if use_digits:
        categories.append(string.digits)
    if use_symbols:
        categories.append(string.punctuation)

    if not categories:
        raise ValueError("at least one character category must be enabled")

    if length < len(categories):
        raise ValueError(
            "length must be at least the number of enabled character categories"
        )

    # Guarantee one char from each selected category
    password_chars = [random.choice(category) for category in categories]

    # Fill remaining length
    remaining = length - len(password_chars)
    chars = "".join(categories)
    password_chars.extend(random.choice(chars) for _ in range(remaining))

    # Shuffle so required chars are not always in front
    random.shuffle(password_chars)

    return "".join(password_chars)

def validate_password(
    password: str,
    min_length: int = 8,
    require_lowercase: bool = True,
    require_uppercase: bool = True,
    require_digits: bool = True,
    require_symbols: bool = True,
) -> bool:
    "Validate whether the password meets given requirements"

    if not isinstance(password, str):
        raise TypeError("password must be a string")
    
    if len(password) < min_length:
        return False
    
    if require_lowercase and not any(ch in string.ascii_lowercase for ch in password):
        return False

    if require_uppercase and not any(ch in string.ascii_uppercase for ch in password):
        return False

    if require_digits and not any(ch in string.digits for ch in password):
        return False

    if require_symbols and not any(ch in string.punctuation for ch in password):
        return False
    
    return True

def password_strength(
    password: str
    ) -> float:
    """
    Give a strength value for a password based on the amount of time it takes to crack.
    Caps strength at 10,000 years to crack, as it's reasonable to assume password is very unlikely to crack by then
    """
    #Roughly 95 unique keys, 120k guesses per second
    #3784320000000 guesses per year, cap strength at 10,000 years to crack
    if " " in password:
        raise Exception("Spaces not allowed in strings")
    pool = 0
    for c in password:
        if c.islower() and c.isalpha():
            pool += 26
            break
    for c in password:
        if c.isupper() and c.isalpha():
            pool += 26
            break
    for c in password:
        if c.isdigit():
            pool += 10
            break;
    if any(not c.isalnum() for c in password):
        pool += 33
    combos = pow(pool, len(password))
    strengthVal = combos/(3784320000000.0 * 10000)
    if strengthVal > 1.0:
        strengthVal = 1.0
    return round(strengthVal, 5)

def password_save(
    password: str,
    path: str = "saved_passwords.txt"
    ) -> bool:
    """
    Saves a given password at a directory.
    Returns true on success and false on failure.
    """
    try:
        file = open(path, "a")
        file.write(password + "\n")
        file.close()
        return True
    except OSError:
        return False