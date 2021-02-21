import logging
import os

from log_test_2 import my_func_2
LOG_PATH_1 = os.path.normpath('./logs/log_1.log')

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s -- %(levelname)s -- %(funcName)s -- %(lineno)d -- %(message)s',
#                     filename=LOG_PATH_1)

"""
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50
"""

logger = logging.getLogger('my_func')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_PATH_1)
formatting = logging.Formatter('%(asctime)s -- %(levelname)s -- %(funcName)s -- %(lineno)d -- %(message)s')
file_handler.setFormatter(formatting)
logger.addHandler(file_handler)


def my_func(a, b, c):
    try:
        value = a * b / c
        logger.info(f'Value is {value}')
        return value
    except ZeroDivisionError:
        logger.error('Not allowed divide by zero.')


my_func(1, 3, 5)
my_func_2(1, 3, 5)
my_func(1, 3, 0)
my_func_2(1, 0, 1)