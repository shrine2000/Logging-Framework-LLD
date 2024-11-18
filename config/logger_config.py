from logging.logger import Logger
from logging.log_level import LogLevel


class LoggerConfig:
    def __init__(self, log_level: LogLevel, handlers: list):
        self.log_level = log_level
        self.handlers = handlers

    def configure(self):
        logger = Logger()
        logger.set_level(self.log_level)
        for handler in self.handlers:
            logger.add_handler(handler)
        return logger
