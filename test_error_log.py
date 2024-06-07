import logger

try:
    a = 1/0
except ZeroDivisionError as e:
    logger.error(e)