"""
WRITES LOG MESSAGES TO A FILE AND ROTATES THE FILE AT CERTAIN INTERVALS
"""

import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('time_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("Hello Wolrd!")
    time.sleep(5)
