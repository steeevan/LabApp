# controllers/user_controller.py
from models.user import User
from database.database_manager import DatabaseManager

class UserController:
    def __init__(self):
        self.db_manager = DatabaseManager('assets/users.db')
        self.db_manager.create_connection()
        self.db_manager.create_user_table()

    def add_user(self, username: str, password: str, role: str):
        if self.db_manager.get_user(username):
            print("User already exists.")
        else:
            if self.db_manager.add_user(username, password, role):
                print(f"User '{username}' added successfully.")
            else:
                print(f"Failed to add user '{username}'.")

    def login(self, username: str, password: str):
        user_data = self.db_manager.get_user(username)
        if user_data and user_data[2] == password:
            user = User(username=user_data[1], password=user_data[2], role=user_data[3])
            print(f"Welcome {user.username}! You have logged in as {user.role}.")
            return user
        else:
            print("Invalid username or password.")
            return None
