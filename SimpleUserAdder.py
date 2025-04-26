import tkinter as tk
from tkinter import messagebox
import subprocess

def add_user():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Input Error", "Username and Password cannot be empty!")
        return

    try:
        # Run Windows command to add user
        result = subprocess.run(
            ["net", "user", username, password, "/add"],
            capture_output=True, text=True, shell=True
        )

        if result.returncode == 0:
            messagebox.showinfo("Success", f"User '{username}' added successfully!")
        else:
            messagebox.showerror("Error", f"Failed to add user:\n{result.stderr}")

    except Exception as e:
        messagebox.showerror("Exception", str(e))


# GUI setup
root = tk.Tk()
root.title("Simple User Adder")
root.geometry("300x250")
root.resizable(False, False)

# Username field
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=(20, 5))
entry_username = tk.Entry(root, width=30)
entry_username.pack()

# Password field
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=(10, 5))
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

# Add user button
btn_add_user = tk.Button(root, text="Add User", command=add_user)
btn_add_user.pack(pady=20)

# Signature
label_signature = tk.Label(root, text="Made in Antwerp by Runaque", font=("Arial", 10), fg="slate gray")
label_signature.pack(side="bottom", pady=5)

root.mainloop()
