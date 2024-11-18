from .log_handler import LogHandler


class ConsoleHandler(LogHandler):
    def log(self, message):
        print(message)
