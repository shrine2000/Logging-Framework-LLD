import threading

from .log_level import LogLevel
from .log_message import LogMessage


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.lock = threading.Lock()
            cls._instance.handlers = []
        return cls._instance

    def add_handler(self, handler):
        self.handlers.append(handler)

    def log(self, level, message):
        if level.value >= self.level.value:
            log_message = LogMessage(level, message)
            with self.lock:
                for handler in self.handlers:
                    handler.log(log_message)

    def set_level(self, level):
        self.level = level
