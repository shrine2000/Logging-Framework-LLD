from abc import ABC, abstractmethod


class LogHandler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def set_next(self, next_handler):
        self.next_handler = next_handler

    @abstractmethod
    def log(self, message):
        if self.next_handler:
            self.next_handler.log(message)
