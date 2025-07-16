import string
import secrets
from cryptography.fernet import Fernet

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

    password = [secrets.choice(char_set) for char_set in char_sets]
    all_chars = ''.join(char_sets)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

# Generate secure password
secure_password = generate_password(length=16)
print("Secure Password:", secure_password)

# 🔑 Generate Fernet Key
key = Fernet.generate_key()
fernet = Fernet(key)

# 🔐 Encrypt the contents of the file "sameer"
with open("Sameer.txt", "rb") as file:
    original_data = file.read()

encrypted_data = fernet.encrypt(original_data)

# Save encrypted data
with open("Sameer.txt.encrypted", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

# Save the key securely — this is needed for decryption
with open("Sameer.txt.key", "w") as key_file:
    key_file.write("Sameer Kumar is a person")

print("File 'sameer' encrypted successfully.")
