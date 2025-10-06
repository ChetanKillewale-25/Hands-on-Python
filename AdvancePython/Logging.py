import logging
logging.basicConfig(level = logging.DEBUG,format = '%(asctime)s-%(levelname)s-%(message)s',
                    datefmt = '%m/%d/%Y%H:%M:%S')
logging.debug("This is a debug message")
logging.info("This is aa Info Message")
logging.warning("This is a Warning Message")
logging.error("This is an Error Message")
logging.critical("This is a ritical Message")
