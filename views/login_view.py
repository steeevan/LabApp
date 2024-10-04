# views/login_view.py
from tkinter import *
from tkinter import messagebox
from controllers.user_controller import UserController

class LoginView(Frame):
    def __init__(self, parent, controller, on_login, on_register):
        super().__init__(parent)
        self.controller = controller
        self.user_controller = UserController()
        self.on_login = on_login
        self.on_register = on_register

        self.create_widgets()

    def create_widgets(self):
        # Set the frame background color
        self.configure(bg="#f0f0f0")

        # Title of the app
        self.title_label = Label(self, text="Welcome to Student Management System", font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=(20, 10))

        # Login frame to center input widgets
        login_frame = Frame(self, bg="#f0f0f0")
        login_frame.pack(expand=True)

        # Username label and entry
        Label(login_frame, text="Username:", font=('Arial', 12), bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.username_entry = Entry(login_frame, font=('Arial', 12), width=25)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        # Password label and entry
        Label(login_frame, text="Password:", font=('Arial', 12), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky=E)
        self.password_entry = Entry(login_frame, font=('Arial', 12), show='*', width=25)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # User role selection
        Label(login_frame, text="Role:", font=('Arial', 12), bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky=E)
        self.role_var = StringVar()
        self.role_var.set("Select Role")
        self.role_dropdown = OptionMenu(login_frame, self.role_var, "Student", "Parent", "Instructor", "Manager")
        self.role_dropdown.config(font=('Arial', 12), width=20)
        self.role_dropdown.grid(row=2, column=1, padx=10, pady=10)

        # Buttons frame
        buttons_frame = Frame(self, bg="#f0f0f0")
        buttons_frame.pack(pady=(10, 20))

        # Login button
        self.login_button = Button(buttons_frame, text="Login", font=('Arial', 12), command=self.login, width=12)
        self.login_button.grid(row=0, column=0, padx=10)

        # Register button
        self.register_button = Button(buttons_frame, text="Register", font=('Arial', 12), command=self.on_register, width=12)
        self.register_button.grid(row=0, column=1, padx=10)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        role = self.role_var.get()

        # Validate the form
        if not username or not password or role == "Select Role":
            messagebox.showerror("Error", "Please fill out all fields and select a role.")
            return

        user = self.user_controller.login(username, password)
        if user and user.role == role:
            self.on_login(user)
        else:
            messagebox.showerror("Login Failed", "Invalid username, password, or role.")
