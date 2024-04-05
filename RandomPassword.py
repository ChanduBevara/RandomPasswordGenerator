import random
import string
n=int(input("Enter length of the password :"))

def generate_password(length=12):
    """
    Generates a random password with the specified length.
    The password includes uppercase letters, lowercase letters, digits, and special characters.
    """
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Generate a password with random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


# Example: Generate a password with a custom length (e.g., n characters)
if n<12 | n>12:
    if n>64:
        print("Password is not Generated")
    else:
        print("Generated Password For ",n," characters):", generate_password(length=n))

# Example: Generate a password with default length (12 characters)
else:
    print("Generated Password:", generate_password())
