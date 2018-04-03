from src.lib.inputparser import InputParser
import sys
import logging
from logging.config import dictConfig


logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(levelname)-5s [%(name)s] %(message)s'}
        },
    handlers = {
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root = {
        'handlers': ['h'],
        'level': logging.INFO,
        },
)
dictConfig(logging_config)
logger = logging.getLogger(__name__)

filename = sys.argv[1]
logger.info("Parsing file %s" % filename)
parser = InputParser(filename)

results = parser.strategymanager.executeStrategies(parser.originalfield)
print(results[0])
field = results[1].getFieldStrings()
for x in range(0, len(field)):
    for y in range(0, len(field[x])):
        print(field[x][y], end="")
    print("")
