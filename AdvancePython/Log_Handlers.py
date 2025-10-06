"""
HANDLER OBJECTS ARE RESPONSIBLE FOR DISPATCHING THE APPROPRIATE LOG MESSAGES TO THE HANDLER'S SPECIFIC LOCATION
"""
"""
WE CAN BUILD DIFFERENT HANDLER'S TO SEND THE LOG MESSAGES TO THE STANDARD OUTPUT STREAM,THROUGH  FILE, HTTP, EMAIL,ETC
"""
import logging
logger = logging.getLogger(__name__)

# create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format for handler's
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a Warning")
logger.error("This is an Error")