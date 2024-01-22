import logging


def create_logger(logger_name: str = __name__):
    """
    Create a logger for the module

    Args:
        logger_name: The name of the logger

    Returns:
        The logger
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)  # Log messages at INFO level and above
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
