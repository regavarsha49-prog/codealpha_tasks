# insecure_login.py
# INSECURE login example

users = {
    "admin": "admin123"
}

print("=== Insecure Login System ===")
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password")
