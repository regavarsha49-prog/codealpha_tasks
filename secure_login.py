# secure_login.py
# SECURE login example

import getpass
import hashlib

STORED_USERNAME = "admin"
STORED_PASSWORD_HASH = "6f2cb9dd8f4b65e24e1c3f3fa5bc57982349237f11abceacd45bbcb74d621c25"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

print("=== Secure Login System ===")
username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

if username == STORED_USERNAME and hash_password(password) == STORED_PASSWORD_HASH:
    print("Login successful!")
else:
    print("Invalid username or password")
