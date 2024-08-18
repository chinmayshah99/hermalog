import unittest
from unittest.mock import patch, MagicMock
import logging
from io import StringIO

from example.sample4 import (
    CustomLogging,
    CustomLoggingConfiguration,
    BaseLoggingConfiguration,
    sample_post_handler,
)


class TestSample4(unittest.TestCase):
    def setUp(self):
        self.configuration = CustomLoggingConfiguration(
            debug=BaseLoggingConfiguration(
                formatter=logging.Formatter("DEBUG: %(message)s"),
            ),
            info=BaseLoggingConfiguration(
                formatter=logging.Formatter("INFO: %(message)s"),
            ),
            warning=BaseLoggingConfiguration(
                formatter=logging.Formatter("WARNING: %(message)s"),
            ),
            error=BaseLoggingConfiguration(
                formatter=logging.Formatter("ERROR: %(message)s"),
            ),
            critical=BaseLoggingConfiguration(
                formatter=logging.Formatter("CRITICAL: %(message)s"),
                post_handler=sample_post_handler,
                log_file="test.log",
            ),
        )
        self.logger = CustomLogging(
            configuration=self.configuration,
            log_level=logging.DEBUG,
            name="test_logger",
        )

    def test_logging_levels(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.logger.debug("Debug message")
            self.logger.info("Info message")
            self.logger.warning("Warning message")
            self.logger.error("Error message")
            self.logger.critical("Critical message")

            output = fake_out.getvalue().strip().split("\n")
            self.assertEqual(output[0], "DEBUG: Debug message")
            self.assertEqual(output[1], "INFO: Info message")
            self.assertEqual(output[2], "WARNING: Warning message")
            self.assertEqual(output[3], "ERROR: Error message")
            self.assertEqual(output[4], "CRITICAL: Critical message")
            self.assertEqual(output[5], "Post handler: Critical message")

    def test_log_file_creation(self):
        with patch("builtins.open", MagicMock()) as mock_open:
            self.logger.critical("Test log file")
            mock_open.assert_called_once_with("test.log", "a")

    @patch("example.sample4.sample_post_handler")
    def test_post_handler_called(self, mock_post_handler):
        self.logger.critical("Test post handler")
        mock_post_handler.assert_called_once_with("Test post handler")


if __name__ == "__main__":
    unittest.main()
