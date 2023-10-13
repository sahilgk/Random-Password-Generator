import string
import secrets
import hashlib

# Password storage dictionary
passwords = {}

# Function to generate a secure password
def generate_password(maxlen):
    if maxlen < 12:
        print("The password length is too short. Please choose a minimum length of 12 characters.")
        return None
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(maxlen))
    return password
    
# Function to save password and hashed values
def save_password(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    passwords[username] = {'salt': salt, 'hashed_password': hashed_password}
    with open("passwords.txt", "a") as file:
        file.write(f"Username: {username}, Salt: {salt}, Hashed Password: {hashed_password}\n")
    print("Password saved to 'passwords.txt'.")

# Function to verify a user's entered password
def verify_password(username, entered_password):
    if username in passwords:
        stored_data = passwords[username]
        stored_salt = stored_data['salt']
        stored_hashed_password = stored_data['hashed_password']
        hashed_password = hash_password(entered_password, stored_salt)
        if hashed_password == stored_hashed_password:
            print("Password is correct.")
            return
    print("Password is incorrect.")

# Function to generate a random salt
def generate_salt():
    return secrets.token_hex(16)

# Function to hash a password with a salt
def hash_password(password, salt):
    salted_password = password + salt
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password

# Function to display the menu and handle user's choice
def menu():
    while True:
        print("\nMenu:")
        print("1. Generate Password")
        print("2. Save Password")
        print("3. Verify Password")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            maxlen = int(input("Enter the maximum length of the password: "))
            password = generate_password(maxlen)
            if password:
                print("Generated Password:", password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter the password to save: ")
            save_password(username, password)
        elif choice == "3":
            username = input("Enter your username for verification: ")
            entered_password = input("Enter the password for verification: ")
            verify_password(username, entered_password)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    menu()
