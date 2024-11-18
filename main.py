from logging.console_handler import ConsoleHandler
from logging.file_handler import FileHandler
from logging.db_handler import DatabaseHandler
from logging.log_level import LogLevel
from config.logger_config import LoggerConfig

if __name__ == "__main__":
    console_handler = ConsoleHandler()
    file_handler = FileHandler("app.log")
    db_handler = DatabaseHandler("logs.db")

    config = LoggerConfig(LogLevel.DEBUG, [console_handler, file_handler, db_handler])
    logger = config.configure()

    logger.log(LogLevel.DEBUG, "This is a debug message.")
    logger.log(LogLevel.INFO, "This is an info message.")
    logger.log(LogLevel.WARNING, "This is a warning message.")
    logger.log(LogLevel.ERROR, "This is an error message.")
    logger.log(LogLevel.FATAL, "This is a fatal message.")

    db_handler.close()
