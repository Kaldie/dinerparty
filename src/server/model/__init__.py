import logging

# create logger with 'spam_application'
logger = logging.getLogger('model')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
fh = logging.FileHandler('model.log')
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

from .party_participation import PartyParticipationModel
from .user import UserModel
from .party import PartyModel