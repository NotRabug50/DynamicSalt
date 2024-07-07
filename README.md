# Dynamic Salt

Dynamic Salt is a security algorithm that dynamically generates a salt from a user's password and mixes this salt into the password before hashing it. This approach enhances security without the need to store salts separately.

## Features

- **No Need to Store Salts:** Salts are dynamically generated from the password, eliminating the need for separate storage.
- **High Security:** Dynamically generated salts make passwords more resistant to attacks such as rainbow table attacks.
- **Simplicity:** Without the need to manage and store salts, the system's complexity is reduced.

## Usage

### Steps

1. **Receive Password**: Prompt the user to enter a password.
2. **Generate Salt**: Dynamically generate a salt from the password.
3. **Mix Salt into Password**: Mix the salt into the password using a specific algorithm.
4. **Hash the Password**: Hash the resulting mixed password.

### Example Walkthrough

#### Sign Up

1. **Receive Password**: The user enters a password, for example, `password123`.
2. **Generate Salt**: The system generates a salt from the password using the SHA-256 algorithm (It will be more secure if you generate salt through text with your own private algorithm). The first 16 characters of the hash are taken as the salt. For `password123`, the salt might be `ef92b778bafe771e`.
3. **Mix Salt into Password**: The system interleaves the salt into the password. For instance, combining `password123` and `ef92b778bafe771e` might result in `peafs9s2wbo7r7d81b2a3fe771e`.
4. **Hash the Password**: The system hashes the mixed password using the SHA-256 algorithm, producing the final hashed password.

#### Sign In

1. **Receive Input Password**: The user enters their password again, for example, `password123`.
2. **Generate Salt**: The system generates the salt again from the input password using the same method as during sign-up.
3. **Mix Salt into Password**: The system interleaves the salt into the input password as done during sign-up.
4. **Hash the Password**: The system hashes the mixed password and compares it with the stored hashed password from the sign-up process. If they match, the authentication is successful.

## Important Note

This project is a simple demonstration of the algorithm and is **not secure** for real-world applications. Please do not use this code in production environments.
