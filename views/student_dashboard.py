# views/student_dashboard.py
from tkinter import *
from tkinter import messagebox

class StudentDashboard(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(bg="#f0f0f0")

        # Create a title
        self.title_label = Label(self, text="Student Dashboard", font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # View Scores
        self.view_scores_button = Button(self, text="View Scores", command=self.view_scores, font=('Arial', 12), width=25)
        self.view_scores_button.pack(pady=10)

        # Upload Files
        self.upload_files_button = Button(self, text="Upload Files", command=self.upload_files, font=('Arial', 12), width=25)
        self.upload_files_button.pack(pady=5)

    def view_scores(self):
        # Logic to view scores
        messagebox.showinfo("View Scores", "Viewing scores functionality goes here.")

    def upload_files(self):
        # Logic to upload files
        messagebox.showinfo("Upload Files", "Uploading files functionality goes here.")
