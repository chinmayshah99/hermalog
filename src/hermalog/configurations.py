from typing import Optional, Callable
from dataclasses import dataclass
import logging


@dataclass
class BaseLoggingConfiguration:
    pre_handler: Optional[Callable] = None
    formatter: Optional[logging.Formatter] = None
    post_handler: Optional[Callable] = None
    log_file: Optional[str] = None


# create dataclass for each log level
@dataclass
class CustomLoggingConfiguration:
    debug: Optional[BaseLoggingConfiguration] = None
    info: Optional[BaseLoggingConfiguration] = None
    warning: Optional[BaseLoggingConfiguration] = None
    error: Optional[BaseLoggingConfiguration] = None
    critical: Optional[BaseLoggingConfiguration] = None
