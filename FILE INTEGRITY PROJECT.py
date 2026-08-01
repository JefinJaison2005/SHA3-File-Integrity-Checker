import hashlib
import json
import os
from datetime import datetime


# Project Folder Configuration


VAULT_FOLDER = "Vault"
REPORTS_FOLDER = "Reports"

if not os.path.exists(VAULT_FOLDER):
    os.mkdir(VAULT_FOLDER)

if not os.path.exists(REPORTS_FOLDER):
    os.mkdir(REPORTS_FOLDER)

HASH_FILE = os.path.join(VAULT_FOLDER, "hashes.json")


# Load Existing Hashes


def load_hashes():

    if os.path.exists(HASH_FILE):

        with open(HASH_FILE, "r") as file:

            return json.load(file)

    return {}

# Save Hashes


def save_hashes(hashes):

    with open(HASH_FILE, "w") as file:

        json.dump(hashes, file, indent=4)

# Generate SHA3-256 Hash


def generate_hash(file_path):

    sha3 = hashlib.sha3_256()

    with open(file_path, "rb") as file:

        while True:

            chunk = file.read(4096)

            if not chunk:
                break

            sha3.update(chunk)

    return sha3.hexdigest()        

# Register a File


def register_file():

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):

        print("\nFile not found!")

        return

    hashes = load_hashes()

    file_hash = generate_hash(file_path)

    hashes[file_path] = file_hash

    save_hashes(hashes)

    print("\nFile Registered Successfully!")

    print("SHA3-256 Hash:")

    print(file_hash)

# Verify File Integrity


def verify_file():

    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):

        print("\nFile not found!")

        return

    hashes = load_hashes()

    if file_path not in hashes:

        print("\nFile has not been registered!")

        return

    current_hash = generate_hash(file_path)

    stored_hash = hashes[file_path]

    if current_hash == stored_hash:

        print("\n✔ File Integrity Verified")
        print("No changes detected.")

    else:

        print("\n❌ WARNING!")
        print("File has been modified.")

# Generate Verification Report


def generate_report(file_path, stored_hash, current_hash, status):

    report_path = os.path.join(REPORTS_FOLDER, "report.txt")

    with open(report_path, "w") as report:

        report.write("========== FILE INTEGRITY REPORT ==========\n\n")

        report.write(f"Date & Time : {datetime.now()}\n")

        report.write(f"File Path   : {file_path}\n\n")

        report.write(f"Stored Hash :\n{stored_hash}\n\n")

        report.write(f"Current Hash:\n{current_hash}\n\n")

        report.write(f"Status      : {status}\n")

# Main Menu

while True:

    print("\n===================================")
    print(" Secure File Integrity Checker")
    print("===================================")

    print("1. Register File")
    print("2. Verify File")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":

        register_file()

    elif choice == "2":

        verify_file()

    elif choice == "3":

        print("\nThank you for using the application.")
        break

    else:

        print("\nInvalid Choice! Please try again.")        
