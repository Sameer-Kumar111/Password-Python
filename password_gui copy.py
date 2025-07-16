import string
import secrets

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if length < 6:
        raise ValueError("Password length should be at least 6 characters for security.")

    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append("!@#$%^&*()-_=+[]{}|;:,.<>?/")

    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    # Ensure password contains at least one character from each selected set
    password = [secrets.choice(char_set) for char_set in char_sets]

    # Fill the rest of the password
    all_chars = ''.join(char_sets)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle to prevent predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

# Example usage
print("Secure Password:", generate_password(length=6))


