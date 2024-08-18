import logging
from typing import Optional


class LoggingBasic(logging.Logger):
    def __init__(self, name: str, log_level: int):
        super().__init__(name=name)
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

    def _configure_logger(
        self,
        log_file: Optional[str] = None,
        level=logging.DEBUG,
        formatter: Optional[logging.Formatter] = None,
    ):
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        normal_handler = logging.StreamHandler()
        normal_handler.setLevel(level=level)
        normal_handler.setFormatter(formatter)
        self.logger.addHandler(normal_handler)
