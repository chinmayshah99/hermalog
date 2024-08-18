from hermalog import CustomLogging
from hermalog import CustomLoggingConfiguration, BaseLoggingConfiguration
import logging


def sample_post_handler(message: str):
    print(f"Post handler: {message}")


if __name__ == "__main__":
    configuration = CustomLoggingConfiguration(
        debug=BaseLoggingConfiguration(
            pre_handler=None,
            formatter=logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            ),
            post_handler=sample_post_handler,
            log_file="sample1.log",
        ),
    )
    logger = CustomLogging(
        configuration=configuration, log_level=logging.DEBUG, name="sample1"
    )
    logger.debug("Hello, World from debug!")
    logger.info("Hello, World from info!")
    logger.warning("Hello, World from warning!")
    logger.error("Hello, World from error!")
    logger.critical("Hello, World from critical!")
