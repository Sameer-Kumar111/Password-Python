import tkinter as tk
from tkinter import messagebox
import hashlib


# Real password stored securely(hashed)
stored_username = "admin"
stored_password_hash = hashlib.sha256("Mysecure@123".encode()).hexdigest()

def check_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()
    entered_password_hash = hashlib.sha256(entered_password.encode()).hexdigest()
    
    if entered_username ==  stored_username and
        entered_password_hash == stored_password_hash:
        messagebox.showinfo("Login Success", "Welcome, Access Granted!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
    
#  create    
window = tk.Tk()
window.title("Secure Login System")
window.geometry("400*250")
window.configure(bg="#f2f2f2")

# label 
tk.Label(window,text="Username:",
bg="#f2f2f2", font=("Arial",12)).pack(pady=(20,5))
username_entry.pack()


tk.Label(window,text="Password:",
bg="#f2f2f2", font=("Arial",
12)).pack(pady=(10,5))
password_entry = tk.Entry(window,
show="*",font=("Arial", 12))
password_entry.pack()

    
    # login 
tk.Button(window, text="Login",
command=check_login, bg="#4C4F50",
fg="white", font=("Arial",12),
padx=10, pady=5).pack(pady=20)

window.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
