import random
import string

def generate_password(length=12):
    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all character sets
    all_chars = lower + upper + digits + special

    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from the combined set
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the resulting list to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

# Specify the length of the password
password_length = 12
password = generate_password(password_length)
print(f"\nGenerated password: {password}\n")
