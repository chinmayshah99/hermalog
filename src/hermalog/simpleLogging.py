from .loggingBasic import LoggingBasic
from .configurations import BaseLoggingConfiguration


class SimpleLogging(LoggingBasic):
    def __init__(
        self, name: str, log_level: int, configuration: BaseLoggingConfiguration
    ):
        super().__init__(name, log_level)
        self._configure_logger(
            formatter=configuration.formatter,
            level=log_level,
            log_file=configuration.log_file,
        )
        self.configuration = configuration

    def debug(self, message):
        if self.configuration.pre_handler:
            self.configuration.pre_handler(message)
        self.logger.debug(message)
        if self.configuration.post_handler:
            self.configuration.post_handler(message)

    def info(self, message):
        if self.configuration.pre_handler:
            self.configuration.pre_handler(message)
        self.logger.info(message)
        if self.configuration.post_handler:
            self.configuration.post_handler(message)

    def warning(self, message):
        if self.configuration.pre_handler:
            self.configuration.pre_handler(message)
        self.logger.warning(message)
        if self.configuration.post_handler:
            self.configuration.post_handler(message)

    def error(self, message):
        if self.configuration.pre_handler:
            self.configuration.pre_handler(message)
        self.logger.error(message)
        if self.configuration.post_handler:
            self.configuration.post_handler(message)

    def critical(self, message):
        if self.configuration.pre_handler:
            self.configuration.pre_handler(message)
        self.logger.critical(message)
        if self.configuration.post_handler:
            self.configuration.post_handler(message)
