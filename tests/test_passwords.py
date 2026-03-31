import string
import pytest
import os

from pypass.passwords import generate_password, validate_password, password_strength, password_save

def test_generate_password_returns_string():
    password = generate_password()
    assert isinstance(password, str)

def test_generate_password_custom_length():
    password = generate_password(length=20)
    assert len(password) == 20

def test_generate_password_includes_lower():
    password = generate_password(use_lower=True, use_upper=False, use_digits=False, use_symbols=False)
    assert all(ch in string.ascii_lowercase for ch in password)

def test_generate_password_includes_upper():
    password = generate_password(use_lower=False, use_upper=True, use_digits=False, use_symbols=False)
    assert all(ch in string.ascii_uppercase for ch in password)

def test_generate_password_includes_digits():
    password = generate_password(use_lower=False, use_upper=False, use_digits=True, use_symbols=False)
    assert all(ch in string.digits for ch in password)

def test_generate_password_includes_symbols():
    password = generate_password(use_lower=False, use_upper=False, use_digits=False, use_symbols=True)
    assert all(ch in string.punctuation for ch in password)

def test_generate_password_includes_all_selected_categories():
    password = generate_password(length=16, use_lower=True, use_upper=True, use_digits=True, use_symbols=True)
    assert any(ch in string.ascii_lowercase for ch in password)
    assert any(ch in string.ascii_uppercase for ch in password)
    assert any(ch in string.digits for ch in password)
    assert any(ch in string.punctuation for ch in password)

def test_generate_password_with_upper_and_lower_only():
    password = generate_password(use_lower=True, use_upper=True, use_digits=False, use_symbols=False)
    assert all(ch in (string.ascii_lowercase + string.ascii_uppercase) for ch in password)
    assert not any(ch in string.digits for ch in password)
    assert not any(ch in string.punctuation for ch in password)

def test_generate_password_raises_if_no_categories_selected():
    with pytest.raises(ValueError, match="at least one character category must be enabled"):
        generate_password(
            length=10,
            use_lower=False,
            use_upper=False,
            use_digits=False,
            use_symbols=False,
        )

def test_generate_password_raises_if_length_too_small():
    with pytest.raises(ValueError, match="length must be at least the number of enabled character categories"):
        generate_password(
            length=2,
            use_lower=True,
            use_upper=True,
            use_digits=True,
            use_symbols=False,
        )

def test_generate_password_raises_if_length_not_positive():
    with pytest.raises(ValueError, match="length must be greater than 0"):
        generate_password(length=0)

def test_validate_password_valid():
    password = "Abc123!"
    assert validate_password(password, min_length=6, require_symbols=True) is True


def test_validate_password_too_short():
    password = "Ab1!"
    assert validate_password(password, min_length=8) is False


def test_validate_password_missing_upper():
    password = "abc123!"
    assert validate_password(password, require_uppercase=True) is False


def test_validate_password_missing_digits():
    password = "Abcdef!"
    assert validate_password(password, require_digits=True) is False


def test_validate_password_invalid_type():
    with pytest.raises(TypeError):
        validate_password(12345)

def test_password_strength_valid_all():
    password = "Abc123!"
    assert password_strength(password) == 0.00185

def test_password_strength_valid_upper_only():
    password = "ABCDEFGHIJ"
    assert password_strength(password) == 0.00373

def test_password_strength_valid_lower_only():
    password = "abcdefghij"
    assert password_strength(password) == 0.00373

def test_password_strength_valid_number_only():
    password = "01234567898765"
    assert password_strength(password) == 0.00264

def test_password_strength_valid_symbol_only():
    password = "!@#$%^&*()"
    assert password_strength(password) == 0.04047

def test_password_strength_valid_upper_lower_only():
    password = "aBcDeFgH"
    assert password_strength(password) == 0.00141

def test_password_strength_valid_upper_lower_number_only():
    password = "Abc123de"
    assert password_strength(password) == 0.00577

def test_password_strength_spaces():
    password = "Ab c123!"
    with pytest.raises(Exception, match="Spaces not allowed in strings"):
        password_strength(password)

def test_password_save_default():
    assert password_save(
        password="Abc123!"
    ) is True
    os.remove("saved_passwords.txt")

def test_password_save_to_path():
    path="saved_passwords_path.txt"
    assert password_save(
        password="Abc123!",
        path=path
    ) is True
    os.remove("saved_passwords_path.txt")

def test_password_save_to_faulty_path():
    path="test/saved_passwords_path.txt"
    assert password_save(
        password="Abc123!",
        path=path
    ) is False