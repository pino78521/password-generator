import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    letters = random.choices(string.ascii_letters, k=6)
    digits = random.choices(string.digits, k=2)
    specials = random.choices("!@#$%^&*()-_=+[]{}", k=1)

    password_chars = letters + digits + specials
    random.shuffle(password_chars)
    password = ''.join(password_chars)
    result_var.set(password)

def copy_to_clipboard():
    password = result_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No password", "Generate a password first!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.resizable(False, False)

result_var = tk.StringVar()

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

generate_btn = tk.Button(frame, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

entry = tk.Entry(frame, textvariable=result_var, width=30, font=("Arial", 12), justify='center')
entry.pack(pady=10)

copy_btn = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=10)

root.mainloop()
