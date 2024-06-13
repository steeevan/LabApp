from tkinter import *
from tkinter import ttk
#TODO maybe read csv file to get all names
class Student:
    students=[]
    def __init__(self,name: str,level: str,subject="Python"):
        self.name=name
        self.level=level
        self.subject=subject
        __class__.students.append(self)
#add some random students
#TODO make this based on reading some weird file or something
def makeStudents():
    Student("Bobina","Rookie")
    Student("Bobby","Rookie")
    Student("Guy","Rookie")
    Student("Jiafei","Advanced")
    Student("Candice","Intermediate")
    Student("Joe Mama","Intermediate")
makeStudents()
def getNames():
    names=[]
    for stu in Student.students:
        names.append(stu.name)
    return names
def getSubject():
    return ["Python","VEX"]
def getInstructors():
    return ["Estevan","Aiden"]

#TODO fix
def getLevels():
    return ["Rookie","Intermediate","Advanced"]

class Option:
    menu=[]
    def __init__(self, root: Tk, label: str, wid: Widget):
        self.label=Label(root,text=label)
        self.label.grid(row=len(__class__.menu),column=0)
        self.wid=wid
        wid.grid(row=len(__class__.menu),column=1)
        __class__.menu.append(self)
    @staticmethod
    def getOption(name: str):
        for opt in __class__.menu:
            if opt.label.cget("text")==name:
                return opt

class OptionButton(Option):
    def __init__(self, root: Tk, label: str, wid: Widget, button: Button):
        super().__init__(root,label,wid)
        self.button=button
        button.grid(row=len(super().menu)-1,column=2)
    
root = Tk()
root.geometry("600x600")
root.resizable(0, 0)
root.title("Evaluation menu")
root.grid_columnconfigure(0, weight=1)
namesBox=ttk.Combobox(root, values=getNames())
Option(root,"Name", namesBox)
levels=ttk.Combobox(root, values=getLevels())
def filterLevels():
    level=levels.get()
    names=[]
    for stu in Student.students:
        if(stu.level==level):
            names.append(stu.name)
    namesBox.configure(values=names)
    namesBox.set("")
OptionButton(root,"Levels", levels, Button(root,text="Filter",command=filterLevels))
Option(root,"Subject",ttk.Combobox(root, values=getSubject()))
Option(root,"Rating", Scale(root,from_=1,to_=5,orient=HORIZONTAL))
Option(root,"Title", Entry(root))
Option(root,"Description",Text(root,height=4,width=35))
Option(root,"Instructor", ttk.Combobox(root,values=getInstructors()))
comment=Text(root,height=10,width=35)
comment.grid(padx=20)
Option(root,"Comments",comment)

#TODO send to csv stuff
def submitButton():
    data={}
    for opt in Option.menu:
        if(isinstance(opt.wid,Entry) or isinstance(opt.wid,Scale)):
            data[opt.label.cget("text")]=opt.wid.get()
        elif(isinstance(opt.wid,ttk.Combobox)):
            data[opt.label.cget("text")]=opt.wid.widget.get()
        elif(isinstance(opt.wid,Text)):
            data[opt.label.cget("text")]=opt.wid.get("1.0",END)
    print(data)
def clearButton():
    for opt in Option.menu:
        #print(type(opt.wid))
        if(isinstance(opt.wid,Entry)):
            opt.wid.delete(0,END)
        elif(isinstance(opt.wid,ttk.Combobox)):
            opt.wid.set("")
        elif(isinstance(opt.wid,Text)):
            opt.wid.delete("1.0",END)
submit=Button(root,text="Submit",command=submitButton).grid(row=len(Option.menu),column=0)
clear=Button(root,text="Clear",command=clearButton).grid(row=len(Option.menu),column=1)
root.mainloop()

