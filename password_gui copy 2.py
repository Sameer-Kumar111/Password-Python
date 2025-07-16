import tkinter as tk
from tkinter import messagebox
import hashlib

# Stored credentials (hashed password)
STORED_USERNAME = "Sameer"
STORED_PASSWORD_HASH = hashlib.sha256("SMK@123".encode()).hexdigest()

# Function to verify login credentials
def check_login():
    entered_username = username_entry.get().strip()
    entered_password = password_entry.get()

    if not entered_username or not entered_password:
        messagebox.showwarning("Input Error", "Please enter both username and password.")
        return

    entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()

    if entered_username == STORED_USERNAME and entered_password_hash == STORED_PASSWORD_HASH:
        messagebox.showinfo("Login Successful", "Welcome, access Sameer!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main application window
window = tk.Tk()
window.title("Secure Login System")
window.geometry("400x250")
window.configure(bg="#f2f2f2")
window.resizable(False, False)

# Title label
tk.Label(window, text="Login Portal", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#333333").pack(pady=10)

# Frame for form elements
form_frame = tk.Frame(window, bg="#f2f2f2")
form_frame.pack(pady=10)

# Username
tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#f2f2f2").grid(row=0, column=0, sticky="w", pady=5, padx=10)
username_entry = tk.Entry(form_frame, font=("Arial", 12), width=25)
username_entry.grid(row=0, column=1, pady=5)

# Password
tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky="w", pady=5, padx=10)
password_entry = tk.Entry(form_frame, show="*", font=("Arial", 12), width=25)
password_entry.grid(row=1, column=1, pady=5)

# Login button
login_button = tk.Button(window, text="Login", command=check_login,
                         bg="#4C4F50", fg="white", font=("Arial", 12),
                         width=15, pady=5)
login_button.pack(pady=20)

# Run the application
window.mainloop()
