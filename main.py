import hashlib

def generate_salt(text):
    # Generate salt from input
    hashed_text = hashlib.sha256(text.encode()).hexdigest()
    return hashed_text[:16]

def mix_salt_into_password(password, salt):
    # Mix salt output with password using some algorithm
    mixed_password = ''
    max_len = max(len(password), len(salt))
    for i in range(max_len):
        if i < len(password):
            mixed_password += password[i]
        if i < len(salt):
            mixed_password += salt[i]
    return mixed_password

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
