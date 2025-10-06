import logging
"""import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('SimpleExample')
logger.debug("this is a debug message")
"""
import traceback
try:
    a = [1, 2, 3]
    val = a[4]
except:
    logging.error('The error is %s', traceback.format_exc())
"""except IndexError as e:
    logging.error(e, exc_info=True)
"""


