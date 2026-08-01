# =====[ IMPORT REQUIRED MODULES ]=============================

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import hashlib
import json
import os
from datetime import datetime


# =====[ PROJECT FOLDER CONFIGURATION ]========================

VAULT_FOLDER = "Vault"
REPORTS_FOLDER = "Reports"

os.makedirs(VAULT_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)

HASH_FILE = os.path.join(VAULT_FOLDER, "hashes.json")


# =====[ COLOR PALETTE ]========================================

BG_DARK = "#0f1117"
BG_CARD = "#171a23"
BG_INPUT = "#1f2330"
ACCENT = "#6366f1"
ACCENT_HOVER = "#4f46e5"
TEXT_MAIN = "#e5e7eb"
TEXT_MUTED = "#8b8fa3"
GREEN = "#22c55e"
RED = "#ef4444"
ORANGE = "#f59e0b"
BORDER = "#2a2e3d"


# =====[ HASH DATABASE ]=======================================

def load_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as file:
            return json.load(file)
    return {}


def save_hashes(hashes):
    with open(HASH_FILE, "w") as file:
        json.dump(hashes, file, indent=4)


# =====[ SHA3-256 HASH GENERATION ]============================

def generate_hash(file_path):
    sha3 = hashlib.sha3_256()
    with open(file_path, "rb") as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            sha3.update(chunk)
    return sha3.hexdigest()


# =====[ REPORT GENERATION ]===================================

def generate_report(file_path, stored_hash, current_hash, status):
    report_path = os.path.join(REPORTS_FOLDER, "report.txt")
    with open(report_path, "w") as report:
        report.write("========== FILE INTEGRITY REPORT ==========\n\n")
        report.write(f"Date & Time : {datetime.now()}\n")
        report.write(f"File Path   : {file_path}\n\n")
        report.write(f"Stored Hash :\n{stored_hash}\n\n")
        report.write(f"Current Hash:\n{current_hash}\n\n")
        report.write(f"Status      : {status}\n")


# =====[ INITIALIZE MAIN APPLICATION WINDOW ]==================

window = tk.Tk()
window.title("SHA3 Secure File Integrity Checker")
window.geometry("760x580")
window.minsize(760, 580)
window.configure(bg=BG_DARK)


# =====[ TTK STYLING ]==========================================

style = ttk.Style(window)
style.theme_use("clam")

style.configure(
    "Accent.TButton",
    background=ACCENT,
    foreground="#ffffff",
    font=("Segoe UI", 10, "bold"),
    borderwidth=0,
    focuscolor=ACCENT,
    padding=(18, 10),
)
style.map(
    "Accent.TButton",
    background=[("active", ACCENT_HOVER), ("pressed", ACCENT_HOVER)],
)

style.configure(
    "Ghost.TButton",
    background=BG_CARD,
    foreground=TEXT_MAIN,
    font=("Segoe UI", 10),
    borderwidth=1,
    focuscolor=BG_CARD,
    padding=(18, 10),
)
style.map(
    "Ghost.TButton",
    background=[("active", BG_INPUT), ("pressed", BG_INPUT)],
    bordercolor=[("!disabled", BORDER)],
)

style.configure(
    "Danger.TButton",
    background="#2a1418",
    foreground=RED,
    font=("Segoe UI", 10, "bold"),
    borderwidth=0,
    focuscolor="#2a1418",
    padding=(18, 10),
)
style.map(
    "Danger.TButton",
    background=[("active", "#3a1a20"), ("pressed", "#3a1a20")],
)


# =====[ ROUNDED CARD HELPER (via canvas) ]=====================

def rounded_card(parent, height):
    card = tk.Frame(parent, bg=BG_CARD, height=height)
    card.pack_propagate(False)
    return card


# =====[ APPLICATION FUNCTIONS ]===============================

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a File")
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        hash_entry.delete(0, tk.END)
        set_status("waiting")


def set_status(state):
    states = {
        "waiting": ("●  Waiting for Verification", ORANGE),
        "registered": ("●  File Registered Successfully", GREEN),
        "verified": ("●  File Integrity Verified", GREEN),
        "modified": ("●  Warning — File Has Been Modified", RED),
        "not_registered": ("●  File Not Registered Yet", ORANGE),
    }
    text, color = states[state]
    status_message.config(text=text, fg=color)
    status_dot_frame.config(bg=color)


def register_action():
    file_path = file_entry.get().strip()

    if not file_path:
        messagebox.showwarning("No File Selected", "Please browse and select a file first.")
        return
    if not os.path.exists(file_path):
        messagebox.showerror("File Not Found", "The selected file could not be found.")
        return

    file_hash = generate_hash(file_path)
    hashes = load_hashes()
    hashes[file_path] = file_hash
    save_hashes(hashes)

    hash_entry.delete(0, tk.END)
    hash_entry.insert(0, file_hash)
    set_status("registered")
    generate_report(file_path, file_hash, file_hash, "File Registered")


def verify_action():
    file_path = file_entry.get().strip()

    if not file_path:
        messagebox.showwarning("No File Selected", "Please browse and select a file first.")
        return
    if not os.path.exists(file_path):
        messagebox.showerror("File Not Found", "The selected file could not be found.")
        return

    hashes = load_hashes()
    if file_path not in hashes:
        messagebox.showinfo("Not Registered", "This file has not been registered yet.\nPlease register it first.")
        set_status("not_registered")
        return

    stored_hash = hashes[file_path]
    current_hash = generate_hash(file_path)

    hash_entry.delete(0, tk.END)
    hash_entry.insert(0, current_hash)

    if current_hash == stored_hash:
        set_status("verified")
        status = "File Integrity Verified"
    else:
        set_status("modified")
        status = "File Modified"

    generate_report(file_path, stored_hash, current_hash, status)


def clear_action():
    file_entry.delete(0, tk.END)
    hash_entry.delete(0, tk.END)
    set_status("waiting")


# =====[ OUTER CONTAINER ]======================================

container = tk.Frame(window, bg=BG_DARK)
container.pack(fill="both", expand=True, padx=36, pady=30)


# =====[ HEADER ]================================================

header_frame = tk.Frame(container, bg=BG_DARK)
header_frame.pack(fill="x", pady=(0, 26))

icon_label = tk.Label(header_frame, text="🔐", font=("Segoe UI Emoji", 26), bg=BG_DARK)
icon_label.pack(side="left", padx=(0, 12))

title_box = tk.Frame(header_frame, bg=BG_DARK)
title_box.pack(side="left")

heading = tk.Label(
    title_box,
    text="Secure File Integrity Checker",
    font=("Segoe UI", 18, "bold"),
    bg=BG_DARK,
    fg=TEXT_MAIN,
)
heading.pack(anchor="w")

subheading = tk.Label(
    title_box,
    text="SHA3-256 cryptographic verification",
    font=("Segoe UI", 10),
    bg=BG_DARK,
    fg=TEXT_MUTED,
)
subheading.pack(anchor="w")


# =====[ FILE SELECTION CARD ]==================================

file_card = rounded_card(container, 110)
file_card.pack(fill="x", pady=(0, 16))

file_inner = tk.Frame(file_card, bg=BG_CARD)
file_inner.pack(fill="both", expand=True, padx=22, pady=18)

file_label = tk.Label(
    file_inner, text="SELECTED FILE", font=("Segoe UI", 9, "bold"),
    bg=BG_CARD, fg=TEXT_MUTED,
)
file_label.pack(anchor="w", pady=(0, 8))

file_row = tk.Frame(file_inner, bg=BG_CARD)
file_row.pack(fill="x")

file_entry = tk.Entry(
    file_row, font=("Segoe UI", 10), bg=BG_INPUT, fg=TEXT_MAIN,
    insertbackground=TEXT_MAIN, relief="flat", highlightthickness=1,
    highlightbackground=BORDER, highlightcolor=ACCENT,
)
file_entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))

browse_button = ttk.Button(file_row, text="Browse", style="Ghost.TButton", command=browse_file)
browse_button.pack(side="left")


# =====[ HASH DISPLAY CARD ]====================================

hash_card = rounded_card(container, 110)
hash_card.pack(fill="x", pady=(0, 16))

hash_inner = tk.Frame(hash_card, bg=BG_CARD)
hash_inner.pack(fill="both", expand=True, padx=22, pady=18)

hash_label = tk.Label(
    hash_inner, text="SHA3-256 HASH", font=("Segoe UI", 9, "bold"),
    bg=BG_CARD, fg=TEXT_MUTED,
)
hash_label.pack(anchor="w", pady=(0, 8))

hash_entry = tk.Entry(
    hash_inner, font=("Consolas", 10), bg=BG_INPUT, fg=ACCENT,
    insertbackground=TEXT_MAIN, relief="flat", highlightthickness=1,
    highlightbackground=BORDER, highlightcolor=ACCENT,
)
hash_entry.pack(fill="x", ipady=8)


# =====[ STATUS CARD ]==========================================

status_card = rounded_card(container, 80)
status_card.pack(fill="x", pady=(0, 26))

status_inner = tk.Frame(status_card, bg=BG_CARD)
status_inner.pack(fill="both", expand=True, padx=22, pady=16)

status_title = tk.Label(
    status_inner, text="VERIFICATION STATUS", font=("Segoe UI", 9, "bold"),
    bg=BG_CARD, fg=TEXT_MUTED,
)
status_title.pack(anchor="w", pady=(0, 8))

status_row = tk.Frame(status_inner, bg=BG_CARD)
status_row.pack(anchor="w")

status_dot_frame = tk.Frame(status_row, bg=ORANGE, width=10, height=10)
status_dot_frame.pack_propagate(False)
status_dot_frame.pack(side="left", padx=(0, 8))

status_message = tk.Label(
    status_row, text="Waiting for Verification", font=("Segoe UI", 11, "bold"),
    bg=BG_CARD, fg=ORANGE,
)
status_message.pack(side="left")


# =====[ ACTION BUTTONS ]======================================

button_frame = tk.Frame(container, bg=BG_DARK)
button_frame.pack(fill="x")

register_button = ttk.Button(button_frame, text="Register", style="Accent.TButton", command=register_action)
register_button.pack(side="left", padx=(0, 10))

verify_button = ttk.Button(button_frame, text="Verify", style="Accent.TButton", command=verify_action)
verify_button.pack(side="left", padx=(0, 10))

clear_button = ttk.Button(button_frame, text="Clear", style="Ghost.TButton", command=clear_action)
clear_button.pack(side="left", padx=(0, 10))

exit_button = ttk.Button(button_frame, text="Exit", style="Danger.TButton", command=window.destroy)
exit_button.pack(side="right")


# =====[ START APPLICATION ]===================================

window.mainloop()
