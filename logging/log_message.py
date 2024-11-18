from datetime import datetime


class LogMessage:
    def __init__(self, level, message):
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.level = level
        self.message = message

    def __str__(self):
        return f"[{self.timestamp}] [{self.level.name}] {self.message}"
