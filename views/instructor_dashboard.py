# views/instructor_dashboard.py
from tkinter import *
from tkinter import messagebox, ttk
import os
import pandas as pd
from models.student import Student
from utils.dashboard_utils import add_common_dashboard_components

class InstructorDashboard(Frame):
    def __init__(self, parent, controller, on_logout, on_account_settings):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        # Create title
        self.title_label = Label(self, text="Instructor Dashboard", font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Student List
        self.students_listbox = Listbox(self, font=('Arial', 12), width=50, height=10)
        self.students_listbox.pack(pady=10)
        self.load_students()

        # Month Selection
        self.month_var = StringVar()
        self.month_var.set("Select Month")
        self.month_dropdown = OptionMenu(self, self.month_var, *["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.month_dropdown.config(font=('Arial', 12), width=20)
        self.month_dropdown.pack(pady=5)

        # Open Evaluation Sheet Button
        self.open_eval_button = Button(self, text="Open Evaluation Sheet", command=self.open_evaluation_sheet, font=('Arial', 12), width=25)
        self.open_eval_button.pack(pady=10)

        # Chat Area for Instructor
        chat_label = Label(self, text="Parent-Instructor Chat", font=('Arial', 14, 'bold'), bg="#f0f0f0")
        chat_label.pack(pady=10)

        self.chat_frame = Frame(self, bg="#f0f0f0")
        self.chat_frame.pack(pady=10)
        self.chat_text = Text(self.chat_frame, font=('Arial', 12), width=40, height=10)
        self.chat_text.pack(side=LEFT, padx=10, pady=10)
        self.chat_scroll = Scrollbar(self.chat_frame, command=self.chat_text.yview)
        self.chat_scroll.pack(side=RIGHT, fill=Y)
        self.chat_text['yscrollcommand'] = self.chat_scroll.set

        self.chat_entry = Entry(self, font=('Arial', 12), width=50)
        self.chat_entry.pack(pady=5)
        self.reply_button = Button(self, text="Reply", command=self.reply_to_message, font=('Arial', 12))
        self.reply_button.pack()

        # Add common components (Logout and Account Settings)
        add_common_dashboard_components(self, on_logout, on_account_settings)

    def load_students(self):
        self.students_listbox.delete(0, END)
        for student in Student.get_students():
            self.students_listbox.insert(END, student.name)

    def open_evaluation_sheet(self):
        selected_student = self.students_listbox.get(ACTIVE)
        selected_month = self.month_var.get()

        if not selected_student or selected_month == "Select Month":
            messagebox.showwarning("Incomplete Selection", "Please select both a student and a month.")
            return

        student_eval_path = f"assets/student_evaluations/{selected_student}_evaluation.csv"

        if os.path.exists(student_eval_path):
            self.append_to_evaluation_sheet(student_eval_path, selected_student, selected_month)
        else:
            messagebox.showerror("Error", f"Evaluation sheet for {selected_student} not found.")

    def append_to_evaluation_sheet(self, file_path, student_name, month):
        # Load CSV data
        df = pd.read_csv(file_path)

        if month in df['Month'].values:
            messagebox.showinfo("Edit Evaluation", f"Editing existing evaluation for {student_name} in {month}.")
        else:
            messagebox.showinfo("New Evaluation", f"Creating new evaluation for {student_name} in {month}.")
            # Append a new row
            new_row = {
                "Name": student_name,
                "Month": month,
                "Subject": "",
                "Rating": "",
                "Title": "",
                "Description": "",
                "Instructor": "Instructor's Name",
                "Comments": ""
            }
            df = df.append(new_row, ignore_index=True)

        # Update CSV and display evaluation form
        df.to_csv(file_path, index=False)
        self.show_evaluation_entry_form(df, file_path)

    def show_evaluation_entry_form(self, df, file_path):
        eval_window = Toplevel(self)
        eval_window.title("Student Evaluation")
        eval_window.geometry("600x400")

        # Field Labels and Entries
        fields = ["Subject", "Rating", "Title", "Description", "Instructor", "Comments"]
        entries = {}

        for idx, field in enumerate(fields):
            label = Label(eval_window, text=f"{field}:", font=('Arial', 12))
            label.grid(row=idx, column=0, padx=10, pady=10, sticky=W)

            entry = Entry(eval_window, font=('Arial', 12), width=40)
            entry.grid(row=idx, column=1, padx=10, pady=10)
            entries[field] = entry

        submit_button = Button(eval_window, text="Submit", font=('Arial', 12), command=lambda: self.submit_evaluation(df, file_path, entries))
        submit_button.grid(row=len(fields), column=1, pady=20)

    def submit_evaluation(self, df, file_path, entries):
        row_index = df.index[df['Month'] == self.month_var.get()][0]
        for field, entry in entries.items():
            df.at[row_index, field] = entry.get()

        df.to_csv(file_path, index=False)
        messagebox.showinfo("Success", "Evaluation updated successfully.")

    def reply_to_message(self):
        message = self.chat_entry.get()
        if message.strip():
            self.chat_text.insert(END, f"Instructor: {message}\n")
            self.chat_entry.delete(0, END)
        else:
            messagebox.showwarning("Empty Message", "Cannot send an empty message.")
