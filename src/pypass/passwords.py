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