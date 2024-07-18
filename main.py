import hashlib

def generate_salt(text):
    # Generate salt from input
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return hashed_text

def mix_salt_into_password(password, salt):
    # Mix salt with password using XOR operation
    password_bytes = password.encode()
    salt_bytes = salt.encode()
    
    max_len = max(len(password_bytes), len(salt_bytes))
    mixed_password = bytearray(max_len)
    for i in range(max_len):
        mixed_password[i] = password_bytes[i % len(password_bytes)] ^ salt_bytes[i % len(salt_bytes)]
    
    return mixed_password.hex()

def hash_password(password):
    # Hash password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

# Get password input
password = input("Enter a password: ")

# Generate salt
salt = generate_salt(password)

# Mix salt with password and hash the password
mixed_password = mix_salt_into_password(password, salt)
hashed_password = hash_password(mixed_password)

#Print results
print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"Mixed Password: {mixed_password}")
print(f"Hashed Password: {hashed_password}")
