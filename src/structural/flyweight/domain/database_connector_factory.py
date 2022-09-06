from __future__ import annotations

from src.structural.flyweight.core.database_connector import DatabaseConnector
from src.structural.flyweight.domain.mysql_connector import MySQLConnector
from src.structural.flyweight.domain.oracle_connector import OracleConnector
from src.structural.flyweight.domain.postgresql_connector import PostgreSQLConnector


class DatabaseConnectorFactory:

    def __init__(self):
        self._connectors = {}
        self._register("oracle", OracleConnector())

    def _register(self, key: str, connector: DatabaseConnector) -> DatabaseConnector:
        self._connectors[key] = connector
        return connector

    def _get_exist_instance(self, connector: str) -> DatabaseConnector | None:
        try:
            instance = self._connectors[connector]
            print("Warning ->> Using existing connector.")
            return instance
        except:
            return None

    def get(self, connector: str) -> DatabaseConnector:
        if connector is None or connector == "":
            raise Exception("Connector is not defined.")

        instance = self._get_exist_instance(connector)
        if instance is not None:
            return instance

        if connector == "postgresql":
            return self._register("postgresql", PostgreSQLConnector())

        if connector == "mysql":
            return self._register("mysql", MySQLConnector())

        raise Exception("Connector couldn't initialyze.")
