import tkinter as tk
from tkinter import messagebox
import os


VALID_LICENSE_FILE = "valid_license.txt"
USER_LICENSE_FILE = "license.txt"


def load_valid_license() -> str:
    if not os.path.exists(VALID_LICENSE_FILE):
        raise FileNotFoundError("The File 'valid_license.txt' does not exist")
    with open(VALID_LICENSE_FILE, "r") as f:
        return f.read().strip()


def save_user_license(key: str):
        with open(USER_LICENSE_FILE, "w") as f:
            f.write(key)



def load_user_license() -> str:
    if not os.path.exists(USER_LICENSE_FILE):
        return ""
        with open(USER_LICENSE_FILE, "r") as f:
            return f.read().strip()


def is_valid_license(license: str) -> bool:
    with open(VALID_LICENSE_FILE, "r") as f:
        return f.read().strip()





# UI
def check_license():
    key = entry_key.get().strip()
    if not key:
        messagebox.showwarning("Warning", "Please enter a license key")
        return

    try:
        if is_valid_license(key):
            save_user_license(key)
            messagebox.showinfo("Success" , "Your license key is valid.")
            root.destroy()
        else:
            messagebox.showerror("Error", "Invalid license key")
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))

def autofill_license():
    key = load_user_license()
    if key:
        entry_key.insert(0, key)


# GUI
root = tk.Tk()
root.title("License System")
root.geometry("350x160")
root.resizable(False, False)

tk.Label(root, text="License key:").pack(pady=(30, 0))
entry_key = tk.Entry(root, width=40)
entry_key.pack()

tk.Button(root, text="Check License", command=check_license).pack(pady=20)

autofill_license()
root.mainloop()