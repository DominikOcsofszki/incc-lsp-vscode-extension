import logging


def prep_logger(file_name: str):
    parent_dir = "/Users/dominik/HOME/BA/DEV/MAIN/logging/"
    logging.basicConfig(filename=f"{parent_dir}{file_name}", level=logging.INFO)
    # logging.basicConfig(filename=f"{parent_dir}{file_name}", level=logging.NOTSET)
    logger = logging.getLogger(__name__)
    return logger


file_name = "log_10_12_24.txt"
LOGGING = prep_logger(file_name)
