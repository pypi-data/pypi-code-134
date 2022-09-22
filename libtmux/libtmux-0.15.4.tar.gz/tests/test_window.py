"""Test for libtmux Window object."""
import logging
import typing as t

import pytest

from libtmux import exc
from libtmux.common import has_gte_version
from libtmux.pane import Pane
from libtmux.server import Server
from libtmux.session import Session
from libtmux.window import Window

logger = logging.getLogger(__name__)


def test_select_window(session: Session) -> None:
    window_count = len(session._windows)
    # to do, get option for   base-index from tmux
    # for now however, let's get the index from the first window.
    assert window_count == 1

    window_base_index = int(session.attached_window.index)

    window = session.new_window(window_name="testing 3")

    # self.assertEqual(2,
    # int(session.attached_window.index))
    assert int(window_base_index) + 1 == int(window.index)

    session.select_window(str(window_base_index))
    assert window_base_index == int(session.attached_window.index)

    session.select_window("testing 3")
    assert int(window_base_index) + 1 == int(session.attached_window.index)

    assert len(session._windows) == 2


def test_zfresh_window_data(session: Session) -> None:
    attached_window = session.attached_window
    assert attached_window is not None
    pane_base_idx = attached_window.show_window_option("pane-base-index", g=True)
    assert pane_base_idx is not None
    pane_base_index = int(pane_base_idx)

    assert len(session.windows) == 1

    assert len(session.attached_window.panes) == 1
    current_windows = len(session._windows)
    assert session.get("session_id") != "@0"
    assert current_windows == 1

    assert len(session.attached_window.panes) == 1
    assert isinstance(session.server, Server)
    # len(session.attached_window.panes))

    assert len(session.windows), 1
    assert len(session.attached_window.panes) == 1
    for w in session.windows:
        assert isinstance(w, Window)
    window = session.attached_window
    assert isinstance(window, Window)
    assert len(session.attached_window.panes) == 1
    window.split_window()

    attached_window = session.attached_window
    assert attached_window is not None
    attached_window.select_pane(pane_base_index)

    attached_pane = session.attached_pane
    assert attached_pane is not None
    attached_pane.send_keys("cd /srv/www/flaskr")

    attached_window.select_pane(pane_base_index + 1)
    attached_pane = session.attached_pane
    assert attached_pane is not None
    attached_pane.send_keys("source .venv/bin/activate")
    session.new_window(window_name="second")
    current_windows += 1
    assert current_windows == len(session._windows)
    session.new_window(window_name="hey")
    current_windows += 1
    assert current_windows == len(session._windows)

    session.select_window("1")
    session.kill_window(target_window="hey")
    current_windows -= 1
    assert current_windows == len(session._windows)


def test_newest_pane_data(session: Session) -> None:
    window = session.new_window(window_name="test", attach=True)
    assert isinstance(window, Window)
    assert len(window.panes) == 1
    window.split_window(attach=True)

    assert len(window.panes) == 2
    # note: the below used to accept -h, removing because split_window now
    # has attach as its only argument now
    window.split_window(attach=True)
    assert len(window.panes) == 3


def test_attached_pane(session: Session) -> None:
    """Window.attached_window returns active Pane."""

    window = session.attached_window  # current window
    assert isinstance(window.attached_pane, Pane)


def test_split_window(session: Session) -> None:
    """Window.split_window() splits window, returns new Pane, vertical."""
    window_name = "test split window"
    window = session.new_window(window_name=window_name, attach=True)
    pane = window.split_window()
    assert len(window.panes) == 2
    assert isinstance(pane, Pane)
    assert float(window.panes[0].height) <= ((float(window.width) + 1) / 2)


def test_split_window_shell(session: Session) -> None:
    """Window.split_window() splits window, returns new Pane, vertical."""
    window_name = "test split window"
    cmd = "sleep 1m"
    window = session.new_window(window_name=window_name, attach=True)
    pane = window.split_window(shell=cmd)
    assert len(window.panes) == 2
    assert isinstance(pane, Pane)
    assert float(window.panes[0].height) <= ((float(window.width) + 1) / 2)
    if has_gte_version("3.2"):
        assert pane.get("pane_start_command", "").replace('"', "") == cmd
    else:
        assert pane.get("pane_start_command") == cmd


def test_split_window_horizontal(session: Session) -> None:
    """Window.split_window() splits window, returns new Pane, horizontal."""
    window_name = "test split window"
    window = session.new_window(window_name=window_name, attach=True)
    pane = window.split_window(vertical=False)
    assert len(window.panes) == 2
    assert isinstance(pane, Pane)
    assert float(window.panes[0].width) <= ((float(window.width) + 1) / 2)


@pytest.mark.parametrize(
    "window_name_before,window_name_after",
    [("test", "ha ha ha fjewlkjflwef"), ("test", "hello \\ wazzup 0")],
)
def test_window_rename(
    session: Session, window_name_before: str, window_name_after: str
) -> None:
    """Window.rename_window()."""
    window_name_before = "test"
    window_name_after = "ha ha ha fjewlkjflwef"

    session.set_option("automatic-rename", "off")
    window = session.new_window(window_name=window_name_before, attach=True)

    assert window == session.attached_window
    assert window.get("window_name") == window_name_before

    window.rename_window(window_name_after)

    window = session.attached_window

    assert window.get("window_name") == window_name_after

    window = session.attached_window

    assert window.get("window_name") == window_name_after


def test_kill_window(session: Session) -> None:
    session.new_window()
    # create a second window to not kick out the client.
    # there is another way to do this via options too.

    w = session.attached_window

    w.get("window_id")

    w.kill_window()
    with pytest.raises(IndexError):
        w.get("window_id")


def test_show_window_options(session: Session) -> None:
    """Window.show_window_options() returns dict."""
    window = session.new_window(window_name="test_window")

    options = window.show_window_options()
    assert isinstance(options, dict)


def test_set_show_window_options(session: Session) -> None:
    """Set option then Window.show_window_options(key)."""
    window = session.new_window(window_name="test_window")

    window.set_window_option("main-pane-height", 20)
    assert window.show_window_option("main-pane-height") == 20

    window.set_window_option("main-pane-height", 40)
    assert window.show_window_option("main-pane-height") == 40
    assert window.show_window_options()["main-pane-height"] == 40

    if has_gte_version("2.3"):
        window.set_window_option("pane-border-format", " #P ")
        assert window.show_window_option("pane-border-format") == " #P "


def test_empty_window_option_returns_None(session: Session) -> None:
    window = session.new_window(window_name="test_window")
    assert window.show_window_option("alternate-screen") is None


def test_show_window_option(session: Session) -> None:
    """Set option then Window.show_window_option(key)."""
    window = session.new_window(window_name="test_window")

    window.set_window_option("main-pane-height", 20)
    assert window.show_window_option("main-pane-height") == 20

    window.set_window_option("main-pane-height", 40)
    assert window.show_window_option("main-pane-height") == 40
    assert window.show_window_option("main-pane-height") == 40


def test_show_window_option_unknown(session: Session) -> None:
    """Window.show_window_option raises UnknownOption for bad option key."""
    window = session.new_window(window_name="test_window")

    cmd_exception: t.Type[exc.OptionError] = exc.UnknownOption
    if has_gte_version("3.0"):
        cmd_exception = exc.InvalidOption
    with pytest.raises(cmd_exception):
        window.show_window_option("moooz")


def test_show_window_option_ambiguous(session: Session) -> None:
    """show_window_option raises AmbiguousOption for ambiguous option."""
    window = session.new_window(window_name="test_window")

    with pytest.raises(exc.AmbiguousOption):
        window.show_window_option("clock-mode")


def test_set_window_option_ambiguous(session: Session) -> None:
    """set_window_option raises AmbiguousOption for ambiguous option."""
    window = session.new_window(window_name="test_window")

    with pytest.raises(exc.AmbiguousOption):
        window.set_window_option("clock-mode", 12)


def test_set_window_option_invalid(session: Session) -> None:
    """Window.set_window_option raises ValueError for invalid option key."""

    window = session.new_window(window_name="test_window")

    if has_gte_version("2.4"):
        with pytest.raises(exc.InvalidOption):
            window.set_window_option("afewewfew", 43)
    else:
        with pytest.raises(exc.UnknownOption):
            window.set_window_option("afewewfew", 43)


def test_move_window(session: Session) -> None:
    """Window.move_window results in changed index"""

    window = session.new_window(window_name="test_window")
    new_index = str(int(window.index) + 1)
    window.move_window(new_index)
    assert window.index == new_index


def test_move_window_to_other_session(server: Server, session: Session) -> None:
    window = session.new_window(window_name="test_window")
    new_session = server.new_session("test_move_window")
    window.move_window(session=new_session.get("session_id"))
    window_id = window.get("window_id")
    assert window_id is not None
    assert new_session.get_by_id(window_id) == window


def test_select_layout_accepts_no_arg(server: Server, session: Session) -> None:
    """tmux allows select-layout with no arguments, so let's allow it here."""

    window = session.new_window(window_name="test_window")
    window.select_layout()
