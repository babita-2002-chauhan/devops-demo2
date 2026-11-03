from tkinter import *
from db_config import topics_col

def dashboard_gui():
    total = topics_col.count_documents({})
    completed = topics_col.count_documents({"status": "Completed"})
    pending = topics_col.count_documents({"status": "Not Started"})
    in_progress = topics_col.count_documents({"status": "In Progress"})

    root = Tk()
    root.title("Dashboard")
    root.geometry("350x250")
    root.configure(bg="#fff0f5")  # Lavender background

    Label(root, text="--- Dashboard ---", font=("Arial", 14, "bold"), bg="#fff0f5").pack(pady=10)
    Label(root, text=f"Total Topics: {total}", font=("Arial", 12), bg="#fff0f5").pack(pady=5)
    Label(root, text=f"Completed: {completed}", font=("Arial", 12), bg="#fff0f5").pack(pady=5)
    Label(root, text=f"In Progress: {in_progress}", font=("Arial", 12), bg="#fff0f5").pack(pady=5)
    Label(root, text=f"Pending: {pending}", font=("Arial", 12), bg="#fff0f5").pack(pady=5)

    Button(root, text="Close", width=20, bg="#dda0dd", font=("Arial", 12), command=root.destroy).pack(pady=10)
    root.mainloop()
    #uploated in fresh-branch 
