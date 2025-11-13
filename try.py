from logger import custom_logger
logger = custom_logger.CustomLogger().get_logger(__file__)
logger.info("This is an info log message from try.py")
logger.error("This is an error log message from try.py")
logger.debug("This is a debug log message from try.py")
logger.warning("This is a warning log message from try.py")
logger.critical("This is a critical log message from try.py")
