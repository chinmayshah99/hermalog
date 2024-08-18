import logging
from hermalog import SimpleLogging
from hermalog import BaseLoggingConfiguration


def pre_handler(message):
    print(f"Pre-handler: {message}")


def post_handler(message):
    print(f"Post-handler: {message}")


if __name__ == "__main__":
    configuration = BaseLoggingConfiguration(
        pre_handler=pre_handler,
        post_handler=post_handler,
        formatter=logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        ),
        log_file="sample1.log",
    )
    logger = SimpleLogging(
        configuration=configuration, log_level=logging.DEBUG, name="sample1"
    )

    logger.debug("Hello, World from debug!")
    logger.info("Hello, World from info!")
    logger.warning("Hello, World from warning!")
    logger.error("Hello, World from error!")
    logger.critical("Hello, World from critical!")
