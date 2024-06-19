from tkinter import *
from tkinter import ttk
from main import CSVFileManager
from database_manager import DatabaseManager
# Initialize the CSV manager
csv_manager = CSVFileManager('student_evaluations.csv')
csv_manager.create_csv(['Name', 'Level', 'Subject', 'Rating', 'Title', 'Description', 'Instructor', 'Comments'])

class Student:
    students = []

    def __init__(self, name: str, level: str, subject="Python"):
        self.name = name
        self.level = level
        self.subject = subject
        __class__.students.append(self)

# Add some random students
def makeStudents():
    d=DatabaseManager("school.db")
    d.create_connection()
    users = d.execute_read_query("SELECT name FROM students")
    print(users)
    levels=d.execute_read_query("SELECT level FROM students")
    for i in range(len(users)):
        Student(users[i][0],levels[i][0])
    d.close_connection()
makeStudents()

def getNames():
    names = []
    for stu in Student.students:
        names.append(stu.name)
    return names

def getSubject():
    return ["Python", "VEX"]

def getInstructors():
    return ["Estevan", "Aiden"]

def getLevels():
    return ["Rookie", "Intermediate", "Advanced"]

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

root = Tk()
root.geometry("600x600")
root.resizable(0, 0)
root.title("Evaluation Menu")
root.configure(bg="#f0f0f0")

namesBox = ttk.Combobox(root, values=getNames(), font=('Arial', 12))
Option(root, "Name", namesBox)

levels = ttk.Combobox(root, values=getLevels(), font=('Arial', 12))

def filterLevels():
    level = levels.get()
    names = []
    for stu in Student.students:
        if stu.level == level:
            names.append(stu.name)
    namesBox.configure(values=names)
    namesBox.set("")

OptionButton(root, "Level", levels, Button(root, text="Filter", command=filterLevels, font=('Arial', 12)))
Option(root, "Subject", ttk.Combobox(root, values=getSubject(), font=('Arial', 12)))
Option(root, "Rating", Scale(root, from_=1, to_=5, orient=HORIZONTAL, font=('Arial', 12)))
Option(root, "Title", Entry(root, font=('Arial', 12)))
Option(root, "Description", Text(root, height=4, width=35, font=('Arial', 12)))
Option(root, "Instructor", ttk.Combobox(root, values=getInstructors(), font=('Arial', 12)))
comment = Text(root, height=10, width=35, font=('Arial', 12))
comment.grid(row=len(Option.menu), column=1, padx=10, pady=5)
Option(root, "Comments", comment)

def submitButton():
    data = {}
    for opt in Option.menu:
        if isinstance(opt.wid, Entry) or isinstance(opt.wid, Scale):
            data[opt.label.cget("text")] = opt.wid.get()
        elif isinstance(opt.wid, ttk.Combobox):
            data[opt.label.cget("text")] = opt.wid.get()
        elif isinstance(opt.wid, Text):
            data[opt.label.cget("text")] = opt.wid.get("1.0", END).strip()
    
    # Convert data to a list in the correct order
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
    
    # Add the row to the CSV
    csv_manager.add_row(row)

    #print(data)

def clearButton():
    for opt in Option.menu:
        if isinstance(opt.wid, Entry):
            opt.wid.delete(0, END)
        elif isinstance(opt.wid, ttk.Combobox):
            opt.wid.set("")
        elif isinstance(opt.wid, Text):
            opt.wid.delete("1.0", END)

submit = Button(root, text="Submit", command=submitButton, font=('Arial', 12))
submit.grid(row=len(Option.menu), column=0, padx=10, pady=10)
clear = Button(root, text="Clear", command=clearButton, font=('Arial', 12))
clear.grid(row=len(Option.menu), column=1, padx=10, pady=10)

root.mainloop()
