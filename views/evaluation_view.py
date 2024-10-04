# views/evaluation_view.py
from tkinter import *
from tkinter import ttk
from utils.csv_manager import CSVFileManager
from models.student import Student

class Option:
    menu = []

    def __init__(self, root: Tk, label: str, wid: Widget):
        self.label = Label(root, text=label, font=('Arial', 12))
        self.label.grid(row=len(__class__.menu), column=0, sticky=W, padx=10, pady=5)
        self.wid = wid
        wid.grid(row=len(__class__.menu), column=1, padx=10, pady=5)
        __class__.menu.append(self)

    @staticmethod
    def getOption(name: str):
        for opt in __class__.menu:
            if opt.label.cget("text") == name:
                return opt

class OptionButton(Option):
    def __init__(self, root: Tk, label: str, wid: Widget, button: Button):
        super().__init__(root, label, wid)
        self.button = button
        button.grid(row=len(super().menu)-1, column=2, padx=10, pady=5)
class EvaluationView(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.csv_manager = CSVFileManager('student_evaluations.csv')
        self.csv_manager.create_csv(['Name', 'Level', 'Subject', 'Rating', 'Title', 'Description', 'Instructor', 'Comments'])
        
        self.create_widgets()

    def create_widgets(self):
        Option.menu = []
        
        namesBox = ttk.Combobox(self, values=Student.get_names(), font=('Arial', 12))
        Option(self, "Name", namesBox)

        levels = ttk.Combobox(self, values=Student.get_levels(), font=('Arial', 12))
        OptionButton(self, "Level", levels, Button(self, text="Filter", command=lambda: self.filter_levels(levels, namesBox), font=('Arial', 12)))
        
        Option(self, "Subject", ttk.Combobox(self, values=Student.get_subjects(), font=('Arial', 12)))
        Option(self, "Rating", Scale(self, from_=1, to_=5, orient=HORIZONTAL, font=('Arial', 12)))
        Option(self, "Title", Entry(self, font=('Arial', 12)))
        Option(self, "Description", Text(self, height=4, width=35, font=('Arial', 12)))
        Option(self, "Instructor", ttk.Combobox(self, values=Student.get_instructors(), font=('Arial', 12)))
        comment = Text(self, height=10, width=35, font=('Arial', 12))
        comment.grid(row=len(Option.menu), column=1, padx=10, pady=5)
        Option(self, "Comments", comment)

        Button(self, text="Submit", command=self.submit_button, font=('Arial', 12)).grid(row=len(Option.menu), column=0, padx=10, pady=10)
        Button(self, text="Clear", command=self.clear_button, font=('Arial', 12)).grid(row=len(Option.menu), column=1, padx=10, pady=10)

    def filter_levels(self, level_widget, namesBox):
        level = level_widget.get()
        names = [student.name for student in Student.get_students() if student.level == level]
        namesBox.configure(values=names)
        namesBox.set("")

    def submit_button(self):
        data = {}
        for opt in Option.menu:
            if isinstance(opt.wid, (Entry, ttk.Combobox, Scale)):
                data[opt.label.cget("text")] = opt.wid.get()
            elif isinstance(opt.wid, Text):
                data[opt.label.cget("text")] = opt.wid.get("1.0", END).strip()

        row = [
            data.get("Name", ""),
            data.get("Level", ""),
            data.get("Subject", ""),
            data.get("Rating", ""),
            data.get("Title", ""),
            data.get("Description", ""),
            data.get("Instructor", ""),
            data.get("Comments", "")
        ]

        self.csv_manager.add_row(row)
        print(data)

    def clear_button(self):
        for opt in Option.menu:
            if isinstance(opt.wid, Entry):
                opt.wid.delete(0, END)
            elif isinstance(opt.wid, ttk.Combobox):
                opt.wid.set("")
            elif isinstance(opt.wid, Text):
                opt.wid.delete("1.0", END)
