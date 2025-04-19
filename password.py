import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# UI
print("🔐 Password Generator 🔐")
length = int(input("Enter password length: "))
upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

password = generate_password(length, upper, lower, digits, symbols)
print(f"\nGenerated Password: {password}")
