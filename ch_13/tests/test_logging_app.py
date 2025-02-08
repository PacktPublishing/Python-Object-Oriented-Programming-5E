"""
Python 3 Object-Oriented Programming

Chapter 13.  Testing Object-Oriented Programs.
"""
from collections.abc import Iterator
import logging
from pathlib import Path
import signal
import subprocess
import sys
import time

import pytest

import remote_logging_app

# This is an integration test, and works by starting a log_catcher
# We can call it the "Catcher in the Sky".


@pytest.fixture(scope="session")
def log_catcher() -> Iterator[None]:
    server_path = Path("src") / "log_catcher.py"
    print(f"Starting server {server_path}")
    p = subprocess.Popen(
        [sys.executable, str(server_path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    time.sleep(0.25)
    yield
    p.terminate()
    p.wait()
    if p.stdout:
        print(p.stdout.read())
    assert (
        p.returncode == 1 if sys.platform == "win32" else -signal.SIGTERM.value
    ), f"Error in watcher, returncode={p.returncode}"


@pytest.fixture
def logging_config() -> Iterator[None]:
    HOST, PORT = "localhost", 18842
    socket_handler = logging.handlers.SocketHandler(HOST, PORT)
    remote_logging_app.logger.addHandler(socket_handler)
    yield
    socket_handler.close()
    remote_logging_app.logger.removeHandler(socket_handler)


def test_1(log_catcher: None, logging_config: None) -> None:
    for i in range(10):
        remote_logging_app.work(i)


def test_2(log_catcher: None, logging_config: None) -> None:
    for i in range(1, 10):
        remote_logging_app.work(52 * i)
