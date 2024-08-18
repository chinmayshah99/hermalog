import pytest
from unittest.mock import patch
from example.sample5 import (
    CustomLogging,
    CustomLoggingConfiguration,
    BaseLoggingConfiguration,
)
import logging


@pytest.fixture
def custom_logger():
    configuration = CustomLoggingConfiguration(
        debug=BaseLoggingConfiguration(
            pre_handler=None,
            formatter=logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            post_handler=lambda msg: None,
            log_file="test.log",
        ),
    )
    return CustomLogging(
        configuration=configuration, log_level=logging.DEBUG, name="test_logger"
    )


def test_custom_logger_levels(custom_logger, caplog):
    messages = [
        "Hello, World from debug!",
        "Hello, World from info!",
        "Hello, World from warning!",
        "Hello, World from error!",
        "Hello, World from critical!",
    ]

    for level, message in zip(
        ["debug", "info", "warning", "error", "critical"], messages
    ):
        getattr(custom_logger, level)(message)

    assert len(caplog.records) == 5
    for record, expected_message in zip(caplog.records, messages):
        assert expected_message in record.message


@patch("builtins.print")
def test_post_handler(mock_print):
    configuration = CustomLoggingConfiguration(
        debug=BaseLoggingConfiguration(
            pre_handler=None,
            formatter=logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            post_handler=lambda msg: print(f"Post handler: {msg}"),
            log_file=None,
        ),
    )
    custom_logger = CustomLogging(
        configuration=configuration, log_level=logging.DEBUG, name="test_logger"
    )

    custom_logger.debug("Test message")

    mock_print.assert_called_once_with("Post handler: Test message")


def test_log_file_creation(tmp_path):
    log_file = tmp_path / "test.log"
    configuration = CustomLoggingConfiguration(
        debug=BaseLoggingConfiguration(
            pre_handler=None,
            formatter=logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            post_handler=lambda msg: None,
            log_file=str(log_file),
        ),
    )
    custom_logger = CustomLogging(
        configuration=configuration, log_level=logging.DEBUG, name="test_logger"
    )

    custom_logger.debug("Test log file message")

    assert log_file.exists()
    assert "Test log file message" in log_file.read_text()
