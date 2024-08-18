import unittest
import logging
from hermalog.customLogging import (
    CustomLogging,
    CustomLoggingConfiguration,
    BaseLoggingConfiguration,
)


class TestCustomLogging(unittest.TestCase):
    def setUp(self):
        self.configuration = CustomLoggingConfiguration(
            debug=BaseLoggingConfiguration(
                pre_handler=None,
                formatter=logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                ),
                post_handler=None,
            ),
            info=BaseLoggingConfiguration(
                pre_handler=None,
                formatter=logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                ),
                post_handler=None,
            ),
            warning=BaseLoggingConfiguration(
                pre_handler=None,
                formatter=logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                ),
                post_handler=None,
            ),
            error=BaseLoggingConfiguration(
                pre_handler=None,
                formatter=logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                ),
                post_handler=None,
            ),
            critical=BaseLoggingConfiguration(
                pre_handler=None,
                formatter=logging.Formatter(
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                ),
                post_handler=None,
                log_file="sample1.log",
            ),
        )
        self.logger = CustomLogging(
            configuration=self.configuration, log_level=logging.DEBUG, name="sample1"
        )

    def test_debug_logging(self):
        with self.assertLogs("sample1", level="DEBUG") as cm:
            self.logger.debug("Hello, World from debug!")
        self.assertIn("Hello, World from debug!", cm.output[0])

    def test_info_logging(self):
        with self.assertLogs("sample1", level="INFO") as cm:
            self.logger.info("Hello, World from info!")
        self.assertIn("Hello, World from info!", cm.output[0])

    def test_warning_logging(self):
        with self.assertLogs("sample1", level="WARNING") as cm:
            self.logger.warning("Hello, World from warning!")
        self.assertIn("Hello, World from warning!", cm.output[0])

    def test_error_logging(self):
        with self.assertLogs("sample1", level="ERROR") as cm:
            self.logger.error("Hello, World from error!")
        self.assertIn("Hello, World from error!", cm.output[0])

    def test_critical_logging(self):
        with self.assertLogs("sample1", level="CRITICAL") as cm:
            self.logger.critical("Hello, World from critical!")
        self.assertIn("Hello, World from critical!", cm.output[0])


if __name__ == "__main__":
    unittest.main()
