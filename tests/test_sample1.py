import unittest
import logging
from example.sample1 import SimpleLogging, BaseLoggingConfiguration


class TestSample1Logging(unittest.TestCase):
    def setUp(self):
        self.configuration = BaseLoggingConfiguration(
            pre_handler=None,
            post_handler=None,
            formatter=logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            log_file="test_sample1.log",
        )
        self.logger = SimpleLogging(
            configuration=self.configuration,
            log_level=logging.INFO,
            name="test_sample1",
        )

    def test_debug_logging(self):
        with self.assertLogs("test_sample1", level="DEBUG") as cm:
            self.logger.debug("Test debug message")
        self.assertIn("Test debug message", cm.output[0])

    def test_info_logging(self):
        with self.assertLogs("test_sample1", level="INFO") as cm:
            self.logger.info("Test info message")
        self.assertIn("Test info message", cm.output[0])

    def test_warning_logging(self):
        with self.assertLogs("test_sample1", level="WARNING") as cm:
            self.logger.warning("Test warning message")
        self.assertIn("Test warning message", cm.output[0])

    def test_error_logging(self):
        with self.assertLogs("test_sample1", level="ERROR") as cm:
            self.logger.error("Test error message")
        self.assertIn("Test error message", cm.output[0])

    def test_critical_logging(self):
        with self.assertLogs("test_sample1", level="CRITICAL") as cm:
            self.logger.critical("Test critical message")
        self.assertIn("Test critical message", cm.output[0])


if __name__ == "__main__":
    unittest.main()
