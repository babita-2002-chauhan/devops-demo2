from tkinter import *
from tkinter import messagebox
from db_config import users_col

# Create initial user (run once)
def create_default_user():
    if users_col.count_documents({}) == 0:
        users_col.insert_one({"username": "admin", "password": "admin123"})

def login_gui():
    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        user = users_col.find_one({"username": username, "password": password})
        if user:
            messagebox.showinfo("Login", "Login Successful!")
            root.destroy()  # Close login window
        else:
            messagebox.showerror("Login", "Invalid Login!")

    create_default_user()  # ensure a user exists

    root = Tk()
    root.title("Login")
    root.geometry("350x250")
    root.configure(bg="#f0f8ff")  # Light blue background

    Label(root, text="Username", bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)
    username_entry = Entry(root, font=("Arial", 12))
    username_entry.pack(pady=5)

    Label(root, text="Password", bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)
    password_entry = Entry(root, show="*", font=("Arial", 12))
    password_entry.pack(pady=5)

    Button(root, text="Login", width=20, bg="#87cefa", font=("Arial", 12), command=check_login).pack(pady=20)

    root.mainloop()
