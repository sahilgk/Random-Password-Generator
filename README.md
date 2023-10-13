# Random-Password-Generator

This Python script serves as a simple password management system with a menu-driven interface. It allows users to perform actions such as generating secure passwords, securely storing them, and verifying passwords. The script focuses on password security by utilizing salting and hashing.

# Modules Used:

string: This module provides a collection of characters and character-related operations. In the script, it's used to define the character sets for generating passwords.

secrets: The secrets module provides access to cryptographically strong random numbers suitable for generating secure passwords.

hashlib: The hashlib module allows for secure hashing of passwords using various hash algorithms, enhancing password security.

# Key Functions:

generate_password(maxlen): Generates a secure password with a specified maximum length. If the length provided is less than 12 characters, it displays an error message.

save_password(username, password): Saves a password securely by generating a random salt, hashing the password with the salt, and storing the salt and hashed password along with the username. It also appends this information to a "passwords.txt" file.

verify_password(username, entered_password): Verifies a user's entered password by comparing it to the stored password's hash. If a match is found, it confirms that the password is correct; otherwise, it informs the user that the password is incorrect.

generate_salt(): Generates a random salt used to enhance password security by adding randomness during the password hashing process.

hash_password(password, salt): Hashes a password with a given salt using the SHA-256 hashing algorithm.

menu(): Displays a menu-driven interface where users can choose between generating, saving, and verifying passwords or quitting the program. It continuously prompts for user input until they choose to quit.
