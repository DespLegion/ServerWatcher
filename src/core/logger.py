import logging


class CustomLogger:

    def __init__(
            self,
            logger_name,
            log_level="error",
            log_format="%(name)s %(asctime)s %(levelname)s %(message)s",
            logfile_path="./logs/",
            logfile_name=None,
    ):
        self.logger_name = logger_name
        self.log_level = log_level
        self.log_format = log_format
        self.logfile_path = logfile_path
        self.logfile_name = logfile_name

    def create_logger(self):
        custom_logger = logging.getLogger(self.logger_name)
        return self.create_logger_format(custom_logger)

    def create_logger_format(self, custom_logger):

        if self.log_level == "error":
            custom_logger.setLevel(logging.ERROR)
        elif self.log_level == "debug":
            custom_logger.setLevel(logging.DEBUG)
        elif self.log_level == "info":
            custom_logger.setLevel(logging.INFO)

        return self.create_logger_file_handler(custom_logger)

    def create_logger_file_handler(self, custom_logger):

        log_format = logging.Formatter(self.log_format)

        if self.logfile_name:
            file_handler = logging.FileHandler(f'{self.logfile_path}{self.logfile_name}')
        else:
            file_handler = logging.FileHandler(f'{self.logfile_path}{self.logger_name}.log')

        file_handler.setFormatter(log_format)
        custom_logger.addHandler(file_handler)

        return custom_logger
