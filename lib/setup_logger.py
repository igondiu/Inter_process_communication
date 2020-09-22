import os
import logging
from logging import handlers

BLUE = "\033[0;34m"
YELLOW = "\033[0;33m"
GREEN = "\033[0;32m"
RED = "\033[0;31m"
NC = "\033[0m"


def setup_logger(log_folder, micro_service_name, debug_verbosity=1):
    """ setup a logger and catch exception if failure """
    log_file_name = micro_service_name + ".log"
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file = os.path.join(log_folder, log_file_name)
    formatter = logging.Formatter(
        "[%(asctime)s] - {%(pathname)s:%(lineno)d} - " "%(levelname)s - %(message)s",
        "%m-%d %H:%M:%S",
    )
    handler = handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1)
    handler.setFormatter(formatter)
    handler.suffix = "%Y%d%m"

    root_logger = logging.getLogger()
    if debug_verbosity:
        root_logger.setLevel(logging.DEBUG)
        root_logger.info("Setting LOG verbosity to DEBUG")
    else:
        root_logger.setLevel(logging.INFO)
    # Display logs in docker-container as well
    logging.basicConfig(level=root_logger.getEffectiveLevel())
    root_logger.addHandler(handler)
    root_logger.info("Logger has been set up")

    return [True, root_logger]
