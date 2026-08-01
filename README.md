# 🔐 SHA3 Secure File Integrity Checker

A Python-based application for **file integrity verification** using the **SHA3-256 cryptographic hash algorithm**. This project provides both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** built with **Tkinter**, allowing users to securely register files, verify file integrity, and generate verification reports.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![GUI](https://img.shields.io/badge/GUI-Tkinter-success)
![Algorithm](https://img.shields.io/badge/Algorithm-SHA3--256-red)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Project Overview

File integrity verification is an essential aspect of cybersecurity, ensuring that files remain unmodified after registration. This project utilizes the **SHA3-256 cryptographic hashing algorithm** to detect unauthorized modifications by comparing the current file hash with the previously stored hash.

The application offers two interfaces:

- 🖥️ **Graphical User Interface (GUI)** built using Tkinter
- ⌨️ **Command-Line Interface (CLI)** for terminal-based interaction

Both interfaces use the same SHA3-256 hashing mechanism to register and verify files.

---

# ✨ Features

- 🔒 SHA3-256 cryptographic hash generation
- 📁 Register files for integrity monitoring
- ✅ Verify file integrity
- 📄 Automatic verification report generation
- 💾 JSON-based hash storage
- 🖥️ Modern Tkinter GUI
- ⌨️ Command-Line Interface (CLI)
- 📂 Browse files using File Explorer
- 🟢 Visual verification status indicator
- 🧹 Clear application fields
- ❌ Safe application exit

---

# 🖥️ Application Interfaces

## Graphical User Interface (GUI)

The GUI version provides a modern and user-friendly desktop application for performing file integrity verification.

### Features

- Browse files using File Explorer
- Register files with a single click
- Generate SHA3-256 hash
- Verify registered files
- Visual verification status
- Automatic report generation
- Clear application fields
- Safe application exit

Run the GUI version:

```bash
python gui_integrity_checker.py
```

---

## Command-Line Interface (CLI)

The CLI version provides the same functionality through a terminal-based interface.

### Features

- Register files
- Verify file integrity
- Generate verification reports
- JSON-based hash storage

Run the CLI version:

```bash
python cli_integrity_checker.py
```

---

# 📸 GUI Preview

### Home Screen

> Add your GUI screenshot here after uploading it.

```markdown
![Home Screen](screenshots/home.png)
```

### Verification

```markdown
![Verification](screenshots/verified.png)
```

---

# 📂 Project Structure

```text
SHA3-File-Integrity-Checker/
│
├── gui_integrity_checker.py
├── cli_integrity_checker.py
├── README.md
├── LICENSE
├── .gitignore
│
├── Vault/
│   └── hashes.json
│
├── Reports/
│   └── report.txt
│
└── screenshots/
    ├── home.png
    ├── registered.png
    └── verified.png
```

---

# ⚙️ Technologies Used

- Python 3
- Tkinter
- hashlib
- JSON
- OS Module
- Datetime Module

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/JefinJaison2005/SHA3-File-Integrity-Checker.git
```

Navigate into the project folder:

```bash
cd SHA3-File-Integrity-Checker
```

No additional Python packages are required.

---

# ▶️ Running the Application

### GUI Version

```bash
python gui_integrity_checker.py
```

### CLI Version

```bash
python cli_integrity_checker.py
```

---

# 🔄 Application Workflow

```text
Start Application
        │
        ▼
Browse File
        │
        ▼
Register File
        │
        ▼
Generate SHA3-256 Hash
        │
        ▼
Store Hash in JSON Database
        │
        ▼
Verify File
        │
        ▼
Generate Current SHA3-256 Hash
        │
        ▼
Compare Stored & Current Hash
        │
        ▼
Generate Verification Report
        │
        ▼
Display Verification Status
```

---

# 📄 Generated Files

## Vault

Stores the SHA3-256 hashes of all registered files.

```text
Vault/
└── hashes.json
```

---

## Reports

Stores the latest verification report.

```text
Reports/
└── report.txt
```

---

# 🎯 Future Improvements

- Drag-and-drop file support
- Batch file verification
- Progress indicator for large files
- Export reports as PDF
- Verification history
- User authentication
- Cloud synchronization

---

# 👨‍💻 Author

**Jefin Jaison**

B.Tech Electronics and Communication Engineering

Rajagiri School of Engineering and Technology

GitHub: **https://github.com/JefinJaison2005**

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

Feedback and suggestions are always welcome!
