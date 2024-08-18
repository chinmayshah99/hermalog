import unittest
from unittest.mock import patch, call
import logging
from example.sample2 import pre_handler, post_handler, BaseLoggingConfiguration


class TestLogging(unittest.TestCase):
    @patch("builtins.print")
    def test_pre_handler(self, mock_print):
        pre_handler("Test message")
        mock_print.assert_called_once_with("Pre-handler: Test message")

    @patch("builtins.print")
    def test_post_handler(self, mock_print):
        post_handler("Test message")
        mock_print.assert_called_once_with("Post-handler: Test message")

    @patch("example.sample2.SimpleLogging")
    def test_logging(self, MockSimpleLogging):
        configuration = BaseLoggingConfiguration(
            pre_handler=pre_handler,
            post_handler=post_handler,
            formatter=logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            log_file="sample1.log",
        )
        logger = MockSimpleLogging(
            configuration=configuration, log_level=logging.DEBUG, name="sample1"
        )

        logger.debug("Hello, World from debug!")
        logger.info("Hello, World from info!")
        logger.warning("Hello, World from warning!")
        logger.error("Hello, World from error!")
        logger.critical("Hello, World from critical!")

        expected_calls = [
            call.debug("Hello, World from debug!"),
            call.info("Hello, World from info!"),
            call.warning("Hello, World from warning!"),
            call.error("Hello, World from error!"),
            call.critical("Hello, World from critical!"),
        ]
        logger.assert_has_calls(expected_calls, any_order=False)


if __name__ == "__main__":
    unittest.main()
