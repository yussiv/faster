import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
_console_logger = logging.StreamHandler(sys.stdout)
_console_logger.setFormatter(
    logging.Formatter(
        fmt="{asctime} | {name:<15} | {levelname:^8} | {message}",
        style="{",
    )
)
logger.addHandler(_console_logger)
