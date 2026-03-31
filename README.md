# PyPasserer 🔐

[![Build Status](https://github.com/swe-students-spring2026/3-package-clouded_leopard/actions/workflows/main.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-clouded_leopard/actions)

## 📦 Description

PyPasserer is a lightweight and fun Python package for generating, validating, and analyzing passwords.

It provides developers with simple tools to:
- generate secure passwords
- validate password requirements
- estimate password strength
- save passwords to a file

This package is designed as a learning exercise in building, testing, and distributing Python packages.

---

## 🚀 Installation

pip install PyPasserer

PyPI: (https://pypi.org/project/PyPasserer/)

---

## 🧪 Usage

### Generate a Password

from pypasserer.passwords import generate_password

password = generate_password(length=12)
print(password)

---

### Validate a Password

from pypasserer.passwords import validate_password

validate_password("Abc123!")  # True
validate_password("abc")      # False

---

### Check Password Strength

from pypasserer.passwords import password_strength

strength = password_strength("Abc123!")
print(strength)

---

### Save a Password

from pypasser.passwords import password_save

password_save("Abc123!")

---

## 📚 Functions

generate_password(...)
- Generates a password with customizable options (length, lowercase, uppercase, digits, symbols)
- Guarantees at least one character from each selected category

validate_password(...)
- Validates password requirements:
  - minimum length
  - lowercase letters
  - uppercase letters
  - digits
  - symbols
- Returns True or False
- Raises TypeError if password is not a string

password_strength(password)
- Estimates how long it would take to crack a password
- Returns a float between 0 and 1
- Raises Exception if password contains spaces

password_save(password, path="saved_passwords.txt")
- Saves password to a file
- Returns True on success, False on failure

---

## 💻 Example Program

See examples/demo.py for a complete script demonstrating all features.

---

## 🛠️ Development Setup

git clone https://github.com/swe-students-spring2026/3-package-clouded_leopard.git
cd 3-package-clouded_leopard

pipenv install
pipenv install -e .

pipenv run pytest

---

## 🔁 Workflow (Contributing)

1. git checkout -b feature/your-feature-name
2. git add .
3. git commit -m "Describe your changes"
4. git push -u origin feature/your-feature-name
5. Open a Pull Request

---

## 👥 Contributors

- [Hanson Huang](https://github.com/Hansonhzh)
- [Cary Ho](https://github.com/CakeOfThePans)
- [Natt Hong](https://github.com/nmh6063-star)

---

## ⚙️ Configuration

No environment variables are required.

---

## 🧾 License

See LICENSE file for details.