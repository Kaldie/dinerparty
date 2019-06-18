import logging

# create logger with 'spam_application'
logger = logging.getLogger('resources')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('resources.log')
fh.setLevel(logging.INFO)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG) 

# create formatter and add it to the handlers
formatter = logging.Formatter('"%(pathname)s", line %(lineno)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)