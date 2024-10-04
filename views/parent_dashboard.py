# views/parent_dashboard.py
from tkinter import *
from tkinter import messagebox
from models.parents import Parent
from models.student import Student
from utils.dashboard_utils import add_common_dashboard_components

class ParentDashboard(Frame):
    def __init__(self, parent, controller, user, on_logout, on_account_settings):
        super().__init__(parent)
        self.controller = controller
        self.user = user
        self.configure(bg="#f0f0f0")

        # Create a title
        self.title_label = Label(self, text="Parent Dashboard", font=('Arial', 18, 'bold'), bg="#f0f0f0")
        self.title_label.pack(pady=20)

        # Children Information
        self.children_label = Label(self, text="Your Children:", font=('Arial', 14), bg="#f0f0f0")
        self.children_label.pack(pady=10)

        self.children_listbox = Listbox(self, font=('Arial', 12), width=50, height=10)
        self.children_listbox.pack(pady=10)
        self.load_children()

        # Chat with Instructor
        chat_label = Label(self, text="Chat with Instructor", font=('Arial', 14), bg="#f0f0f0")
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
        self.send_button = Button(self, text="Send", command=self.send_message, font=('Arial', 12))
        self.send_button.pack()

        # Add common components (Logout and Account Settings)
        add_common_dashboard_components(self, on_logout, on_account_settings)

    def load_children(self):
        self.children_listbox.delete(0, END)
        for child in self.user.children:
            self.children_listbox.insert(END, f"{child.name} (Level: {child.level}, Subject: {child.subject})")

    def send_message(self):
        message = self.chat_entry.get().strip()
        if message:
            self.chat_text.insert(END, f"Parent: {message}\n")
            self.chat_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Message cannot be empty.")
