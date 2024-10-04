# models/user.py

class User:
    def __init__(self, username: str, password: str, role: str):
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def validate_user(username: str, password: str, users: list):
        """
        Validate the user credentials.

        Args:
            username (str): The username to validate.
            password (str): The password to validate.
            users (list): List of User objects.

        Returns:
            User: The authenticated user object if credentials match, otherwise None.
        """
        for user in users:
            if user.username == username and user.password == password:
                return user
        return None
