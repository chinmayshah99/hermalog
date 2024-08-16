import logging
from typing import Optional, Callable
from dataclasses import dataclass




@dataclass
class CustomNotificationHandlerBase:
    pre_handler: Optional[Callable] = None
    formatter: Optional[logging.Formatter] = None
    post_handler: Optional[Callable] = None

# create dataclass for each log level
@dataclass
class CustomNotificationHandler:
    debug: CustomNotificationHandlerBase
    info: CustomNotificationHandlerBase
    warning: CustomNotificationHandlerBase
    error: CustomNotificationHandlerBase
    critical: CustomNotificationHandlerBase
    
class CustomNotification(logging.Logger):
    def __init__(self, name: str, log_level, custom_handler: Optional[CustomNotificationHandler] = None, log_debug_file=None, log_info_file=None, log_warning_file=None, log_error_file=None, log_critical_file=None, common_handler: Optional[CustomNotificationHandlerBase] = None):
        # if both custom_handler and common_handler are set, raise an error
        if custom_handler is not None and common_handler is not None:
            raise ValueError("Both custom_handler and common_handler cannot be set")
        
        # Configure loggers for each log level
        if custom_handler is None:
            custom_handler = CustomNotificationHandler(
                debug=CustomNotificationHandlerBase(
                    pre_handler=None,
                    formatter=None,
                    post_handler=None
                ),
                info=CustomNotificationHandlerBase(
                    pre_handler=None,
                    formatter=None,
                    post_handler=None
                ),
                warning=CustomNotificationHandlerBase(
                    pre_handler=None,
                    formatter=None,
                    post_handler=None
                ),
                error=CustomNotificationHandlerBase(
                    pre_handler=None,
                    formatter=None,
                    post_handler=None
                ),
                critical=CustomNotificationHandlerBase(
                    pre_handler=None,
                    formatter=None,
                    post_handler=None
                )
            )
        if common_handler is not None:
            custom_handler = CustomNotificationHandler(
                debug=common_handler,
                info=common_handler,
                warning=common_handler,
                error=common_handler,
                critical=common_handler
            )
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        if common_handler is None:
            self._configure_logger(log_debug_file, logging.DEBUG, custom_handler.debug.formatter)
            self._configure_logger(log_info_file, logging.INFO, custom_handler.info.formatter)
            self._configure_logger(log_warning_file, logging.WARNING, custom_handler.warning.formatter)
            self._configure_logger(log_error_file, logging.ERROR, custom_handler.error.formatter)
            self._configure_logger(log_critical_file, logging.CRITICAL, custom_handler.critical.formatter)
        else:
            self._configure_logger(formatter=common_handler.formatter, level=log_level)
        print('custom_handler', custom_handler)
        # Store the custom handler function
        self.custom_handler = {
            logging.DEBUG: {
                'pre_handler': custom_handler.debug.pre_handler if custom_handler.debug.pre_handler is not None else None,
                'post_handler': custom_handler.debug.post_handler if custom_handler.debug.post_handler is not None else None
            },
            logging.INFO: {
                'pre_handler': custom_handler.info.pre_handler if custom_handler.info.pre_handler is not None else None,
                'post_handler': custom_handler.info.post_handler if custom_handler.info.post_handler is not None else None
            },
            logging.WARNING: {
                'pre_handler': custom_handler.warning.pre_handler if custom_handler.warning.pre_handler is not None else None,
                'post_handler': custom_handler.warning.post_handler if custom_handler.warning.post_handler is not None else None
            },
            logging.ERROR: {
                'pre_handler': custom_handler.error.pre_handler if custom_handler.error.pre_handler is not None else None,
                'post_handler': custom_handler.error.post_handler if custom_handler.error.post_handler is not None else None
            },
            logging.CRITICAL: {
                'pre_handler': custom_handler.critical.pre_handler if custom_handler.critical.pre_handler is not None else None,
                'post_handler': custom_handler.critical.post_handler if custom_handler.critical.post_handler is not None else None
            }
        }

    def _configure_logger(self, log_file=None, level=logging.DEBUG, formatter: Optional[logging.Formatter] = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')) -> None:
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        normal_handler = logging.StreamHandler()
        normal_handler.setLevel(level)
        normal_handler.setFormatter(formatter)
        self.logger.addHandler(normal_handler)
        print('logger', self.logger)
        # return self.logger

    def debug(self, message):
        print('debug', message)
        pre_handler = self.custom_handler[logging.DEBUG]['pre_handler']
        if pre_handler:
            pre_handler(message)
        self.logger.debug(message)
        post_handler = self.custom_handler[logging.DEBUG]['post_handler']
        if post_handler:
            post_handler(message)

    def info(self, message):
        pre_handler = self.custom_handler[logging.INFO]['pre_handler']
        if pre_handler:
            pre_handler(message)
        self.logger.info(message)
        post_handler = self.custom_handler[logging.INFO]['post_handler']
        if post_handler:
            post_handler(message)

    def warning(self, message):
        pre_handler = self.custom_handler[logging.WARNING]['pre_handler']
        if pre_handler:
            pre_handler(message)
        self.logger.warning(message)
        post_handler = self.custom_handler[logging.WARNING]['post_handler']
        if post_handler:
            post_handler(message)
        

    def error(self, message):
        pre_handler = self.custom_handler[logging.ERROR]['pre_handler']
        if pre_handler:
            pre_handler(message)
        self.logger.error(message)
        post_handler = self.custom_handler[logging.ERROR]['post_handler']
        if post_handler:
            post_handler(message)

    def critical(self, message):
        pre_handler = self.custom_handler[logging.CRITICAL]['pre_handler']
        if pre_handler:
            pre_handler(message)
        self.logger.critical(message)
        post_handler = self.custom_handler[logging.CRITICAL]['post_handler']
        if post_handler:
            post_handler(message)

# # Define a custom handling function (replace this with your custom logic)
# def custom_handler(level, message):
#     print(f"Custom Handling ({level}): {message}")


# class HermaLog(CustomNotification):
#     def __init__(self, name: str) -> None:
#         super().__init__(name)