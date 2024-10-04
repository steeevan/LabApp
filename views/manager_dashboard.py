# views/manager_dashboard.py
from tkinter import *
from tkinter import messagebox, ttk
from utils.csv_manager import CSVFileManager
from models.student import Student
from utils.dashboard_utils import add_common_dashboard_components
import pandas as pd
import os

class ManagerDashboard(Frame):
    def __init__(self, parent, controller, on_logout, on_account_settings):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        # CSV Manager for evaluations
        self.csv_folder = 'assets/student_evaluations'
        os.makedirs(self.csv_folder, exist_ok=True)

        # Create a title
        self.title_label = Label(self, text="Manager Dashboard", font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Student List
        self.students_listbox = Listbox(self, font=('Arial', 12), width=50, height=10)
        self.students_listbox.pack(pady=10)
        self.load_students()

        # Edit Student Evaluation Button
        self.edit_eval_button = Button(self, text="Edit Student Evaluation", command=self.edit_student_evaluation, font=('Arial', 12), width=25)
        self.edit_eval_button.pack(pady=5)

        # Treeview for CSV Data
        self.tree_frame = Frame(self)
        self.tree_frame.pack(pady=10)
        self.tree = None

        # Add common components (Logout and Account Settings)
        add_common_dashboard_components(self, on_logout, on_account_settings)

    def load_students(self):
        self.students_listbox.delete(0, END)
        for student in Student.get_students():
            self.students_listbox.insert(END, student.name)

    def edit_student_evaluation(self):
        selected_student = self.students_listbox.get(ACTIVE)

        if not selected_student:
            messagebox.showwarning("Edit Student Evaluation", "No student selected.")
            return

        student_eval_path = os.path.join(self.csv_folder, f"{selected_student}_evaluation.csv")

        if not os.path.exists(student_eval_path):
            messagebox.showerror("Error", f"Evaluation sheet for {selected_student} not found.")
            return

        # Display the evaluation sheet in the tree view
        self.display_csv(student_eval_path)

    def display_csv(self, csv_file):
        # Load CSV data into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Clear previous Treeview
        if self.tree:
            self.tree.destroy()

        # Create a new Treeview to display CSV data
        self.tree = ttk.Treeview(self.tree_frame, columns=list(df.columns), show='headings')
        for col in df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)

        # Insert data into Treeview
        for _, row in df.iterrows():
            self.tree.insert('', 'end', values=list(row))

        self.tree.pack()

        # Add Save Changes button
        save_button = Button(self.tree_frame, text="Save Changes", command=lambda: self.save_changes(csv_file), font=('Arial', 12))
        save_button.pack(pady=10)

    def save_changes(self, csv_file):
        # Convert Treeview data back to DataFrame
        rows = []
        for item in self.tree.get_children():
            rows.append(self.tree.item(item)['values'])
        df = pd.DataFrame(rows, columns=[self.tree.heading(col)['text'] for col in self.tree['columns']])

        # Save DataFrame back to CSV
        df.to_csv(csv_file, index=False)
        messagebox.showinfo("Success", "Changes saved successfully.")
