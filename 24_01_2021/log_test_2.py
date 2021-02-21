import logging
import os

"""
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50
"""

LOG_PATH_2 = os.path.normpath('./logs/log_2.log')

logger = logging.getLogger('my_func_2')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_PATH_2)
formatting = logging.Formatter('%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s')
file_handler.setFormatter(formatting)
logger.addHandler(file_handler)

def my_func_2(a, b, c):
    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s :: %(levelname)s :: %(funcName)s :: %(lineno)d :: %(message)s',
    #                     filename=os.path.normpath('./logs/log_2.log'))

    try:
        value = a / b * c
        logger.info(f'Value is {value}')
        return value
    except ZeroDivisionError:
        logger.error('Not allowed divide by zero.')