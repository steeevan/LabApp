# main.py
from tkinter import Tk
from views.login_view import LoginView
from views.register_view import RegisterView
from views.manager_dashboard import ManagerDashboard
from views.instructor_dashboard import InstructorDashboard
from views.parent_dashboard import ParentDashboard
from views.student_dashboard import StudentDashboard
from views.account_settings import AccountSettings

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.current_user = None

        self.show_login_view()

    def show_login_view(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = LoginView(self.root, None, self.on_login, self.show_register_view)
        self.current_frame.pack(expand=True, fill="both")

    def show_register_view(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = RegisterView(self.root, None, self.show_login_view)
        self.current_frame.pack(expand=True, fill="both")

    def on_login(self, user):
        self.current_user = user
        if user.role == "Manager":
            self.show_manager_dashboard()
        elif user.role == "Instructor":
            self.show_instructor_dashboard()
        elif user.role == "Parent":
            self.show_parent_dashboard()
        elif user.role == "Student":
            self.show_student_dashboard()

    def show_manager_dashboard(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = ManagerDashboard(self.root, None, self.logout, self.show_account_settings)
        self.current_frame.pack(expand=True, fill="both")

    def show_instructor_dashboard(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = InstructorDashboard(self.root, None, self.logout, self.show_account_settings)
        self.current_frame.pack(expand=True, fill="both")

    def show_parent_dashboard(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = ParentDashboard(self.root, None, self.logout, self.show_account_settings)
        self.current_frame.pack(expand=True, fill="both")

    def show_student_dashboard(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = StudentDashboard(self.root, None, self.logout, self.show_account_settings)
        self.current_frame.pack(expand=True, fill="both")

    def show_account_settings(self):
        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = AccountSettings(self.root, None, self.current_user, self.go_back_to_dashboard)
        self.current_frame.pack(expand=True, fill="both")

    def go_back_to_dashboard(self):
        # Redirect to the correct dashboard based on the current user's role
        if self.current_user.role == "Manager":
            self.show_manager_dashboard()
        elif self.current_user.role == "Instructor":
            self.show_instructor_dashboard()
        elif self.current_user.role == "Parent":
            self.show_parent_dashboard()
        elif self.current_user.role == "Student":
            self.show_student_dashboard()

    def logout(self):
        # Logout the user and redirect to login view
        self.current_user = None
        self.show_login_view()

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x600")
    root.resizable(0, 0)
    root.title("Student Management System")
    root.configure(bg="#f0f0f0")

    app = MainApplication(root)
    root.mainloop()
