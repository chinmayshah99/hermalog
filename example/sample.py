from logging import Formatter
from hermalog.hermalog import CustomNotification
from hermalog.hermalog import CustomNotificationHandler, CustomNotificationHandlerBase
# Example usage:
if __name__ == "__main__":

    common_handler = CustomNotificationHandlerBase(
        formatter=Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )

    custom_notifier = CustomNotification(
        name="sample",
        custom_handler=None,
        log_level='DEBUG',
        # log_debug_file='debug.log',
        # log_info_file='info.log',
        # log_warning_file='warning.log',
        # log_error_file='error.log',
        # log_critical_file='critical.log',
        # custom_handler=custom_handler
        common_handler=common_handler
    )

    custom_notifier.debug("This is a debug message.")
    custom_notifier.info("This is an info message.")
    custom_notifier.warning("This is a warning message.")
    custom_notifier.error("This is an error message.")
    custom_notifier.critical("This is a critical message.")

