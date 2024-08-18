import logging
from .loggingBasic import LoggingBasic
from .configurations import CustomLoggingConfiguration
from typing import Optional


class CustomLogging(LoggingBasic, logging.Logger):
    def __init__(
        self,
        name: str,
        log_level,
        configuration: Optional[CustomLoggingConfiguration] = None,
    ):
        # Configure loggers for each log level
        if configuration is None:
            raise ValueError("Configuration is required")
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        self.configuration = {}
        if configuration.debug:
            self._configure_logger(
                configuration.debug.log_file,
                logging.DEBUG,
                configuration.debug.formatter,
            )
            self.configuration[logging.DEBUG] = {
                "pre_handler": configuration.debug.pre_handler
                if configuration.debug.pre_handler
                else None,
                "post_handler": configuration.debug.post_handler
                if configuration.debug.post_handler
                else None,
            }
        if configuration.info:
            self._configure_logger(
                configuration.info.log_file, logging.INFO, configuration.info.formatter
            )
            self.configuration[logging.INFO] = {
                "pre_handler": configuration.info.pre_handler
                if configuration.info.pre_handler
                else None,
                "post_handler": configuration.info.post_handler
                if configuration.info.post_handler
                else None,
            }
        if configuration.warning:
            self._configure_logger(
                configuration.warning.log_file,
                logging.WARNING,
                configuration.warning.formatter,
            )
            self.configuration[logging.WARNING] = {
                "pre_handler": configuration.warning.pre_handler
                if configuration.warning.pre_handler
                else None,
                "post_handler": configuration.warning.post_handler
                if configuration.warning.post_handler
                else None,
            }
        if configuration.error:
            self._configure_logger(
                configuration.error.log_file,
                logging.ERROR,
                configuration.error.formatter,
            )
            self.configuration[logging.ERROR] = {
                "pre_handler": configuration.error.pre_handler
                if configuration.error.pre_handler
                else None,
                "post_handler": configuration.error.post_handler
                if configuration.error.post_handler
                else None,
            }
        if configuration.critical:
            self._configure_logger(
                configuration.critical.log_file,
                logging.CRITICAL,
                configuration.critical.formatter,
            )
            self.configuration[logging.CRITICAL] = {
                "pre_handler": configuration.critical.pre_handler
                if configuration.critical.pre_handler
                else None,
                "post_handler": configuration.critical.post_handler
                if configuration.critical.post_handler
                else None,
            }

    def debug(self, message):
        if logging.DEBUG in self.configuration:
            pre_handler = self.configuration[logging.DEBUG]["pre_handler"]
            if pre_handler:
                pre_handler(message)
        self.logger.debug(message)
        if logging.DEBUG in self.configuration:
            post_handler = self.configuration[logging.DEBUG]["post_handler"]
            if post_handler:
                post_handler(message)

    def info(self, message):
        if logging.INFO in self.configuration:
            pre_handler = self.configuration[logging.INFO]["pre_handler"]
            if pre_handler:
                pre_handler(message)
        self.logger.info(message)
        if logging.INFO in self.configuration:
            post_handler = self.configuration[logging.INFO]["post_handler"]
            if post_handler:
                post_handler(message)

    def warning(self, message):
        if logging.WARNING in self.configuration:
            pre_handler = self.configuration[logging.WARNING]["pre_handler"]
            if pre_handler:
                pre_handler(message)
        self.logger.warning(message)

        if logging.WARNING in self.configuration:
            post_handler = self.configuration[logging.WARNING]["post_handler"]
            if post_handler:
                post_handler(message)

    def error(self, message):
        if logging.ERROR in self.configuration:
            pre_handler = self.configuration[logging.ERROR]["pre_handler"]
            if pre_handler:
                pre_handler(message)
        self.logger.error(message)
        if logging.ERROR in self.configuration:
            post_handler = self.configuration[logging.ERROR]["post_handler"]
            if post_handler:
                post_handler(message)

    def critical(self, message):
        if logging.CRITICAL in self.configuration:
            pre_handler = self.configuration[logging.CRITICAL]["pre_handler"]
            if pre_handler:
                pre_handler(message)
        self.logger.critical(message)
        if logging.CRITICAL in self.configuration:
            post_handler = self.configuration[logging.CRITICAL]["post_handler"]
            if post_handler:
                post_handler(message)
