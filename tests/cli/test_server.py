import os
import stat
import subprocess  # nosec - test only runs a fixed command
import time
from unittest.mock import MagicMock

import pytest

from streamdeck_ui.cli import server
from streamdeck_ui.cli.server import CLIStreamDeckServer

USER_UMASK = 0o022


def _current_umask() -> int:
    umask = os.umask(0)
    os.umask(umask)
    return umask


def _wait_until_listening(cli: CLIStreamDeckServer, timeout: float = 5.0) -> None:
    # The timeout is set after bind() and listen(), so it marks the end of setup
    deadline = time.monotonic() + timeout
    while cli.sock.gettimeout() is None:
        if time.monotonic() > deadline:
            pytest.fail("CLI server did not start listening")
        time.sleep(0.01)


@pytest.fixture
def user_umask():
    saved_umask = os.umask(USER_UMASK)
    yield USER_UMASK
    os.umask(saved_umask)


@pytest.fixture
def cli(tmp_path, monkeypatch, user_umask):
    monkeypatch.setattr(server.tempfile, "gettempdir", lambda: str(tmp_path))
    cli_server = CLIStreamDeckServer(MagicMock(), MagicMock())
    yield cli_server
    cli_server.stop()
    cli_server.sock.close()


def test_server_restores_umask_while_running(cli, user_umask):
    cli.start()
    _wait_until_listening(cli)

    assert _current_umask() == user_umask


def test_server_socket_is_private(cli, tmp_path):
    cli.start()
    _wait_until_listening(cli)

    mode = os.stat(tmp_path / "streamdeck_ui.sock").st_mode
    assert stat.S_ISSOCK(mode)
    assert mode & 0o077 == 0


def test_commands_started_while_running_inherit_user_umask(cli, user_umask):
    cli.start()
    _wait_until_listening(cli)

    output = subprocess.check_output(["sh", "-c", "umask"], text=True)  # nosec - fixed command

    assert int(output.strip(), 8) == user_umask


def test_server_exits_when_socket_cannot_be_bound(tmp_path, monkeypatch, user_umask):
    monkeypatch.setattr(server.tempfile, "gettempdir", lambda: str(tmp_path / "missing"))
    cli_server = CLIStreamDeckServer(MagicMock(), MagicMock())

    cli_server.start()
    cli_server.cli_thread.join(timeout=5)

    assert not cli_server.cli_thread.is_alive()
    assert _current_umask() == user_umask
    cli_server.sock.close()
