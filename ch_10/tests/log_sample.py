"""
Python 3 Object-Oriented Programming

Chapter 10. The iterator pattern

This builds a fixture data for other tests.
"""
import argparse
import datetime
import logging
import os
from pathlib import Path
import sys
from textwrap import dedent
import time

## Patch time.time() so the logger sees timestamps advancing

from unittest.mock import Mock, patch

class ClockLike:
    default_start = 1617667409.0  # For non-multiline
    # Use 1617667501.0 for multiline
    def __init__(self, start: float | None = None) -> None:
        self.now = start or ClockLike.default_start
    def update_time(self, amount: float) -> None:
        self.now += amount
    def get_time(self) -> float:
        return self.now
    def get_time_ns(self) -> float:
        return self.now * 1e9

def make_log_messages(base_delay: float = 6, multiline: bool = True) -> None:
    logger = logging.getLogger("sample")
    logger.debug("This is a debugging message.")
    time.sleep(base_delay*2)
    logger.info("This is an information method.")
    time.sleep(base_delay*2)
    logger.warning("This is a warning. It could be serious.")
    time.sleep(base_delay)
    logger.warning("Another warning sent.")
    time.sleep(base_delay)
    logger.info("Here's some information.")

    if multiline:
        time.sleep(base_delay/2)
        logger.info(
            dedent("""
                This is a multi-line information
                message, with misleading content including WARNING
                and it spans lines of the log file WARNING used in a confusing way
            """
            ).strip()
        )

    time.sleep(base_delay*2)
    logger.debug("Debug messages are only useful if you want to figure something out.")
    time.sleep(base_delay*2)
    logger.info("Information is usually harmless, but helpful.")
    time.sleep(base_delay)
    logger.warning("Warnings should be heeded.")
    time.sleep(base_delay)
    logger.warning("Watch for warnings.")


def get_options(argv: list[str] = sys.argv[1:]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--multiline", action="store_const", const=True, default=False)
    parser.add_argument("-d", "--delay", action="store", type=float, default=6)
    parser.add_argument("-o", "--output", action="store", type=Path, default=None)
    parser.add_argument("-f", "--force", action="store_true", default=False)
    parser.add_argument("-s", "--start", action="store", type=float, default=None)
    parser.add_argument("-r", "--randomseed", action="store", type=str, default=os.environ.get("RANDOMSEED", None))
    return parser.parse_args(argv)


if __name__ == "__main__":
    datefmt = "%b %d, %Y %X"
    format = "%(asctime)s %(levelname)s %(message)s"
    options = get_options()
    if options.output is None:
        logging.basicConfig(
            level=logging.DEBUG, format=format, datefmt=datefmt)
    else:
        if options.output.exists() and not options.force:
            print(f"output file {options.output} already exists")
            sys.exit(0)
        logging.basicConfig(filename=options.output, filemode='w',
                            level=logging.DEBUG, format=format, datefmt=datefmt)

    mocked_clock = ClockLike(options.start)

    mock_time = Mock(
        wraps=time,
        sleep=Mock(side_effect=mocked_clock.update_time),
        time=Mock(side_effect=mocked_clock.get_time),
        time_ns=Mock(side_effect=mocked_clock.get_time_ns),
        now=Mock(side_effect=mocked_clock.now),
    )

    with patch('logging.time', mock_time), patch('__main__.time', mock_time):
        print(f"Writing {options.output} times start from {datetime.datetime.fromtimestamp(mock_time.time())}")
        make_log_messages(
            base_delay=options.delay,
            multiline=options.multiline)
