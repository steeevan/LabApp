# models/student.py
import os
import shutil
from utils.csv_manager import CSVFileManager

class Student:
    students = []

    def __init__(self, name: str, level: str, subject="Python", parent=None):
        self.name = name
        self.level = level
        self.subject = subject
        self.parent = parent  # Link to Parent instance
        __class__.students.append(self)
        self.create_evaluation_sheet()

    def create_evaluation_sheet(self):
        """Creates an evaluation sheet for the student based on the template."""
        student_eval_folder = "assets/student_evaluations"
        os.makedirs(student_eval_folder, exist_ok=True)
        student_eval_path = os.path.join(student_eval_folder, f"{self.name}_evaluation.csv")

        if not os.path.exists(student_eval_path):
            shutil.copy("assets/evaluation_template.csv", student_eval_path)

    @classmethod
    def get_students(cls):
        return cls.students

    @classmethod
    def get_students_by_parent(cls, parent):
        return [student for student in cls.students if student.parent == parent]

# Create predefined students without parents for now
Student("Alice", "Rookie")
Student("Bob", "Intermediate")
Student("Charlie", "Advanced")
