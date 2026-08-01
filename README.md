# 🔐 SHA3 File Integrity Checker

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SHA3-256](https://img.shields.io/badge/Algorithm-SHA3--256-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

A Python-based cybersecurity application that verifies file integrity using the **SHA3-256 cryptographic hash algorithm**. The application detects unauthorized file modifications by comparing newly generated hashes with previously stored trusted hashes.

---

# 📌 Table of Contents

- Overview
- Features
- Project Architecture
- Workflow
- Folder Structure
- Technologies Used
- Installation
- Usage
- Future Improvements
- Author
- License

---

# 📖 Overview

The Secure File Integrity Checker is designed to ensure that important files remain unchanged after registration.

The application generates a SHA3-256 cryptographic hash for a selected file and securely stores it. During verification, a new hash is generated and compared against the stored value.

If both hashes match, the file is verified as authentic.

If the hashes differ, the application reports that the file has been modified.

---

# ✨ Features

- 🔐 SHA3-256 Hash Generation
- 📂 Register Files
- ✅ Verify File Integrity
- 📄 Automatic Verification Reports
- 💾 Secure Hash Storage
- 📁 Automatic Folder Creation
- 🖥️ Menu Driven Interface

---

# 🏗 Project Architecture

```text
                User
                  │
                  ▼
        Register / Verify File
                  │
                  ▼
      Generate SHA3-256 Hash
                  │
          ┌───────┴────────┐
          ▼                ▼
      Store Hash       Compare Hash
          │                │
          ▼                ▼
        Vault         Verification
                             │
                             ▼
                      Generate Report
```

---

# 🔄 Workflow

```text
Start
 │
 ▼
Create Required Folders
 │
 ▼
Display Menu
 │
 ├──────────────┐
 ▼              ▼
Register      Verify
 │              │
 ▼              ▼
Generate     Generate
SHA3 Hash    SHA3 Hash
 │              │
 ▼              ▼
Store        Compare
Hash         Hashes
 │              │
 ▼              ▼
             Report
 │
 ▼
Exit
```

---

# 📂 Folder Structure

```text
SHA3-File-Integrity-Checker/
│
├── integrity_checker.py
├── README.md
├── LICENSE
├── .gitignore
│
├── Vault/
│   └── hashes.json
│
└── Reports/
```

---

# ⚙ Technologies Used

- Python 3
- hashlib
- json
- os
- datetime

---

# 🚀 Installation

Clone the repository.

```bash
git clone https://github.com/JefinJaison2005/SHA3-File-Integrity-Checker.git
```

Go into the project directory.

```bash
cd SHA3-File-Integrity-Checker
```

Run the application.

```bash
python integrity_checker.py
```

---

# ▶ Usage

1. Run the application.
2. Register a file.
3. SHA3-256 hash is generated.
4. Hash is stored securely.
5. Verify the same file later.
6. Application reports whether the file has been modified.

---

# 📊 Technologies Demonstrated

- Cryptography
- File Handling
- JSON Storage
- Modular Programming
- Error Handling
- SHA3-256
- Cybersecurity Concepts

---

# 🔮 Future Improvements

- GUI using Tkinter
- Folder Monitoring
- SQLite Database
- User Authentication
- PDF Report Generation
- Drag-and-Drop File Selection
- Dark Theme
- Automatic Periodic Verification

---

# 👨‍💻 Author

**Jefin Jaison**

Electronics and Communication Engineering

Rajagiri School of Engineering and Technology

GitHub:
https://github.com/JefinJaison2005

---

# 📜 License

This project is licensed under the MIT License.
