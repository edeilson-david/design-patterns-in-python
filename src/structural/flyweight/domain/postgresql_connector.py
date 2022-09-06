from src.structural.flyweight.core.database_connector import DatabaseConnector


class PostgreSQLConnector(DatabaseConnector):

    def __init__(self):
        super().__init__("postgresql")
