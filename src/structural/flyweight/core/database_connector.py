
class DatabaseConnector:

    def __init__(self, prefix: str):
        self.prefix = prefix

    def connect(self, username: str, password: str):
        print("Connecting to database...")
        print(f"Prefix: {self.prefix}")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print("Database connection established.")
