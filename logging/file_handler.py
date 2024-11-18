from .log_handler import LogHandler


class FileHandler(LogHandler):
    def __init__(self, file_name):
        super().__init__()
        self.file_name = file_name

    def log(self, message):
        with open(self.file_name, "a") as log_file:
            log_file.write(str(message) + "\n")
        super().log(message)
