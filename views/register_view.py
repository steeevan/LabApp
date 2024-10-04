# views/register_view.py
from tkinter import *
from tkinter import messagebox
from models.student import Student
from models.parents import Parent

class RegisterView(Frame):
    def __init__(self, parent, controller, on_register_complete):
        super().__init__(parent)
        self.controller = controller
        self.on_register_complete = on_register_complete

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entries for Registration Information
        Label(self, text="Name:", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = Entry(self, font=('Arial', 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        Label(self, text="Email:", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10)
        self.email_entry = Entry(self, font=('Arial', 12))
        self.email_entry.grid(row=1, column=1, padx=10, pady=10)

        Label(self, text="Children's Names (comma-separated):", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10)
        self.children_entry = Entry(self, font=('Arial', 12))
        self.children_entry.grid(row=2, column=1, padx=10, pady=10)

        Button(self, text="Register", command=self.register, font=('Arial', 12)).grid(row=3, column=1, pady=20)

    def register(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        children_names = self.children_entry.get().strip().split(',')

        if not name or not email:
            messagebox.showerror("Error", "Please fill out all fields.")
            return

        # Create a new parent
        parent = Parent(name, email)

        # Link parent to existing students
        for child_name in children_names:
            child_name = child_name.strip()
            student = next((s for s in Student.get_students() if s.name == child_name), None)
            if student:
                parent.add_child(student)
                student.parent = parent

        messagebox.showinfo("Success", f"Parent '{name}' registered successfully.")
        self.on_register_complete()
