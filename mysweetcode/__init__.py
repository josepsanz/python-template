from ._version import __version__

import logging

logging.basicConfig(
    level=logging.INFO,
    format='{asctime} - {levelname:>9} - {funcName} - {message}', style='{'
)
