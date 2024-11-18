from abc import ABC, abstractmethod

from logging.log_level import LogLevel


class Observer(ABC):
    @abstractmethod
    def update(self, level, message):
        pass


class LogObserver(Observer):
    def update(self, level, message):
        if level >= LogLevel.ERROR:
            print(f"Observer notified: {message}")
