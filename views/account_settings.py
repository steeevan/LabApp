# views/account_settings.py
from tkinter import *
from tkinter import messagebox

class AccountSettings(Frame):
    def __init__(self, parent, controller, user, on_back):
        super().__init__(parent)
        self.controller = controller
        self.user = user
        self.configure(bg="#f0f0f0")

        # Title
        self.title_label = Label(self, text="Account Settings", font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Username
        Label(self, text="Username:", font=('Arial', 12), bg="#f0f0f0").pack(pady=5)
        self.username_label = Label(self, text=user.username, font=('Arial', 12), bg="#f0f0f0")
        self.username_label.pack(pady=5)

        # Role
        Label(self, text="Role:", font=('Arial', 12), bg="#f0f0f0").pack(pady=5)
        self.role_label = Label(self, text=user.role, font=('Arial', 12), bg="#f0f0f0")
        self.role_label.pack(pady=5)

        # Change Password (Placeholder for additional functionality)
        self.change_password_button = Button(self, text="Change Password", command=self.change_password, font=('Arial', 12), width=20)
        self.change_password_button.pack(pady=10)

        # Back Button
        self.back_button = Button(self, text="Back", command=on_back, font=('Arial', 12), width=15)
        self.back_button.pack(pady=20)

    def change_password(self):
        # Logic to change the password (Placeholder for future implementation)
        messagebox.showinfo("Change Password", "Change password functionality goes here.")
