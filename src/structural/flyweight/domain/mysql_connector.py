from src.structural.flyweight.core.database_connector import DatabaseConnector


class MySQLConnector(DatabaseConnector):

    def __init__(self):
        super().__init__("mysql")
