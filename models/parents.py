# models/parent.py
from models.student import Student

class Parent:
    parents = []

    def __init__(self, name: str, email: str, children=None):
        if children is None:
            children = []
        self.name = name
        self.email = email
        self.children = children  # List of Student instances
        __class__.parents.append(self)

    def add_child(self, student: Student):
        if student not in self.children:
            self.children.append(student)

    @classmethod
    def get_parents(cls):
        return cls.parents

    @classmethod
    def get_parent_by_email(cls, email):
        for parent in cls.parents:
            if parent.email == email:
                return parent
        return None
