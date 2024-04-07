import pytest
from evdev import ecodes as e

from streamdeck_ui.modules.keyboard import _DEFAULT_ADDITIONAL_DELAY, _DELAY_KEYSYM, parse_keys_as_keycodes


@pytest.mark.parametrize(
    "keys, expected",
    [
        ("", []),
        (" ", []),
        ("a", [[e.KEY_A]]),
        ("A", [[e.KEY_A]]),
        ("CTRL+s", [[e.KEY_LEFTCTRL, e.KEY_S]]),
        ("CTRL+plus", [[e.KEY_LEFTCTRL, e.KEY_EQUAL]]),  # plus is equal with shift
        ("CTRL+comma", [[e.KEY_LEFTCTRL, e.KEY_COMMA]]),
        ("CTRL+,", [[e.KEY_LEFTCTRL]]),
        ("CTRL++", [[e.KEY_LEFTCTRL]]),
        ("CTRL+numpad_add", [[e.KEY_LEFTCTRL, e.KEY_KPPLUS]]),
        ("CTRL+numpad_0", [[e.KEY_LEFTCTRL, e.KEY_KP0]]),
        ("CTRL+0", [[e.KEY_LEFTCTRL, e.KEY_0]]),
        ("CTRL+KP0", [[e.KEY_LEFTCTRL, e.KEY_KP0]]),
        ("CTRL + ", [[e.KEY_LEFTCTRL]]),
        ("CTRL + 1, 1", [[e.KEY_LEFTCTRL, e.KEY_1], [e.KEY_1]]),
        (
            "CTRL + 1, delay, a",
            [
                [e.KEY_LEFTCTRL, e.KEY_1],
                [_DELAY_KEYSYM + _DEFAULT_ADDITIONAL_DELAY],
                [e.KEY_A],
            ],
        ),
        (
            "delay 5.1, CTRL+delay0.6+a",
            [[_DELAY_KEYSYM + 51], [e.KEY_LEFTCTRL, _DELAY_KEYSYM + 6, e.KEY_A]],
        ),
    ],
)
def test_parse_keys_as_keycodes(keys, expected):
    assert parse_keys_as_keycodes(keys) == expected


def test_parse_keys_as_keycodes_with_invalid_key():
    with pytest.raises(ValueError):
        parse_keys_as_keycodes("invalid_key")
