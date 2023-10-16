import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_special_chars=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

length = int(input("Enter the desired password length: "))
use_letters = input("Include letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

password = generate_password(length, use_letters, use_digits, use_special_chars)
print("Generated Password:", password)
