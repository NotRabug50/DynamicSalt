# Dynamic Salt

Dynamic Salt is a security algorithm that dynamically generates a salt from a user's password and mixes this salt into the password before hashing it. This approach enhances security without the need to store salts separately.

## Features

- **No Need to Store Salts:** Salts are dynamically generated from the password, eliminating the need for separate storage.
- **High Security:** Dynamically generated salts make passwords more resistant to attacks such as rainbow table attacks.
- **Simplicity:** Without the need to manage and store salts, the system's complexity is reduced.

## Conceptual Enhancements

### 1. Dynamic Distribution of Salt
In addition to generating salts dynamically, the salt distribution process can be adjusted based on the password. This would add an extra layer of complexity to the encryption process.

### 2. Seed Integration
A unique, securely stored seed value could be introduced to influence the salt generation and distribution. This seed would be used in the process of salt creation and mixing, making it even harder for attackers to replicate the salt generation process.

### 3. User-Specific Seed
Implementing a different seed for each user could further enhance individual password security. This means that each user's salt generation and distribution process would be influenced by their own unique seed value.

### 4. Multi-Layered Hashing
Applying multiple layers of hashing throughout the process could provide additional security. Each stage of password processing could involve a new hash function to ensure robust protection against various types of attacks.

## Usage

### Steps

1. **Receive Password:** Prompt the user to enter a password.
2. **Generate Salt:** Dynamically generate a salt from the password.
3. **Mix Salt into Password:** Mix the salt into the password using a specific algorithm.
4. **Hash the Password:** Hash the resulting mixed password.

### Example Walkthrough

#### Sign Up

1. **Receive Password:** The user enters a password, for example, `password123`.
2. **Generate Salt:** The system generates a salt from the password using a specified algorithm.
3. **Mix Salt into Password:** The system interleaves the salt into the password.
4. **Hash the Password:** The system hashes the mixed password.

#### Sign In

1. **Receive Input Password:** The user enters their password again, for example, `password123`.
2. **Generate Salt:** The system generates the salt again from the input password.
3. **Mix Salt into Password:** The system interleaves the salt into the input password as done during sign-up.
4. **Hash the Password:** The system hashes the mixed password and compares it with the stored hashed password from the sign-up process. If they match, the authentication is successful.

## Important Note

This project is a simple demonstration of the algorithm and is **not secure** for real-world applications. Please do not use this code in production environments. The conceptual enhancements discussed offer ideas for improving security but have not been implemented in this demonstration.
