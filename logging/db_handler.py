import sqlite3
from .log_handler import LogHandler


class DatabaseHandler(LogHandler):
    def __init__(self, db_name: str):
        super().__init__()
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                """
                CREATE TABLE IF NOT EXISTS logs (
                    timestamp TEXT,
                    level TEXT,
                    message TEXT
                )
            """
            )

    def log(self, message):
        with self.connection:
            self.connection.execute(
                """
                INSERT INTO logs (timestamp, level, message)
                VALUES (?, ?, ?)
            """,
                (message.timestamp, message.level.name, message.message),
            )
        super().log(message)

    def close(self):
        self.connection.close()
