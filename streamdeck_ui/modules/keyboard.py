import time
from typing import Dict, List, Union

from evdev import InputDevice, UInput
from evdev import ecodes as e
from evdev import list_devices
from PySide6.QtCore import QStringListModel, QThread
from PySide6.QtWidgets import QCompleter

_DEFAULT_KEY_PRESS_DELAY = 0.05
_DEFAULT_KEY_SECTION_DELAY = 0.5

# As far as I know all the key syms in linux are integers below 1000
# use 2000 or above to signify a delay, and add the delay in deciseconds to this keysym value
# For example, if you would like a delay of 5 seconds --> 50 deciseconds, then the keysym would be 2050
_DELAY_KEYSYM = 2000
# Default delay to add when user uses delay keyword in deciseconds (1/10th of a second)
_DEFAULT_ADDITIONAL_DELAY = 5

# fmt: off
_SPECIAL_KEYS: Dict[str, str] = {
    "plus": "+",
    "comma": ",",
    "delay": "delay",
}
_OLD_NUMPAD_KEYS: Dict[str, int] = {
    "numpad_0": e.KEY_KP0,
    "numpad_1": e.KEY_KP1,
    "numpad_2": e.KEY_KP2,
    "numpad_3": e.KEY_KP3,
    "numpad_4": e.KEY_KP4,
    "numpad_5": e.KEY_KP5,
    "numpad_6": e.KEY_KP6,
    "numpad_7": e.KEY_KP7,
    "numpad_8": e.KEY_KP8,
    "numpad_9": e.KEY_KP9,
    "numpad_enter": e.KEY_ENTER,
    "numpad_decimal": e.KEY_KPDOT,
    "numpad_divide": e.KEY_KPSLASH,
    "numpad_multiply": e.KEY_KPASTERISK,
    "numpad_subtract": e.KEY_KPMINUS,
    "numpad_add": e.KEY_KPPLUS,
}
_OLD_PYNPUT_KEYS: Dict[str, int] = {
    "media_volume_mute": e.KEY_MUTE,
    "media_volume_down": e.KEY_VOLUMEDOWN,
    "media_volume_up": e.KEY_VOLUMEUP,
    "media_play_pause": e.KEY_PLAYPAUSE,
    "media_previous_track": e.KEY_PREVIOUSSONG,
    "media_previous": e.KEY_PREVIOUSSONG,
    "media_next_track": e.KEY_NEXTSONG,
    "media_next": e.KEY_NEXTSONG,
    "media_stop": e.KEY_STOPCD,
    "num_lock": e.KEY_NUMLOCK,
    "caps_lock": e.KEY_CAPSLOCK,
    "scroll_lock": e.KEY_SCROLLLOCK,
}
_MODIFIER_KEYS: Dict[str, int] = {
    "ctrl": e.KEY_LEFTCTRL,
    "alt": e.KEY_LEFTALT,
    "alt_gr": e.KEY_RIGHTALT,
    "shift": e.KEY_LEFTSHIFT,
    "meta": e.KEY_LEFTMETA,
    "super": e.KEY_LEFTMETA,
    "win": e.KEY_LEFTMETA,
}

_BAD_ECODES = ['KEY_MAX', 'KEY_CNT']
_KEY_MAPPING: Dict[str, int] = {
    'a': e.KEY_A,
    'b': e.KEY_B,
    'c': e.KEY_C,
    'd': e.KEY_D,
    'e': e.KEY_E,
    'f': e.KEY_F,
    'g': e.KEY_G,
    'h': e.KEY_H,
    'i': e.KEY_I,
    'j': e.KEY_J,
    'k': e.KEY_K,
    'l': e.KEY_L,
    'm': e.KEY_M,
    'n': e.KEY_N,
    'o': e.KEY_O,
    'p': e.KEY_P,
    'q': e.KEY_Q,
    'r': e.KEY_R,
    's': e.KEY_S,
    't': e.KEY_T,
    'u': e.KEY_U,
    'v': e.KEY_V,
    'w': e.KEY_W,
    'x': e.KEY_X,
    'y': e.KEY_Y,
    'z': e.KEY_Z,
    'A': e.KEY_A,
    'B': e.KEY_B,
    'C': e.KEY_C,
    'D': e.KEY_D,
    'E': e.KEY_E,
    'F': e.KEY_F,
    'G': e.KEY_G,
    'H': e.KEY_H,
    'I': e.KEY_I,
    'J': e.KEY_J,
    'K': e.KEY_K,
    'L': e.KEY_L,
    'M': e.KEY_M,
    'N': e.KEY_N,
    'O': e.KEY_O,
    'P': e.KEY_P,
    'Q': e.KEY_Q,
    'R': e.KEY_R,
    'S': e.KEY_S,
    'T': e.KEY_T,
    'U': e.KEY_U,
    'V': e.KEY_V,
    'W': e.KEY_W,
    'X': e.KEY_X,
    'Y': e.KEY_Y,
    'Z': e.KEY_Z,
    '1': e.KEY_1,
    '2': e.KEY_2,
    '3': e.KEY_3,
    '4': e.KEY_4,
    '5': e.KEY_5,
    '6': e.KEY_6,
    '7': e.KEY_7,
    '8': e.KEY_8,
    '9': e.KEY_9,
    '0': e.KEY_0,
    '-': e.KEY_MINUS,
    '=': e.KEY_EQUAL,
    '[': e.KEY_LEFTBRACE,
    ']': e.KEY_RIGHTBRACE,
    '\\': e.KEY_BACKSLASH,
    ';': e.KEY_SEMICOLON,
    "'": e.KEY_APOSTROPHE,
    ',': e.KEY_COMMA,
    '.': e.KEY_DOT,
    '/': e.KEY_SLASH,
    ' ': e.KEY_SPACE,
    '\n': e.KEY_ENTER,
    '\t': e.KEY_TAB,
    '`': e.KEY_GRAVE,
    '!': e.KEY_1,
    '@': e.KEY_2,
    '#': e.KEY_3,
    '$': e.KEY_4,
    '%': e.KEY_5,
    '^': e.KEY_6,
    '&': e.KEY_7,
    '*': e.KEY_8,
    '(': e.KEY_9,
    ')': e.KEY_0,
    '_': e.KEY_MINUS,
    '+': e.KEY_EQUAL,
    '{': e.KEY_LEFTBRACE,
    '}': e.KEY_RIGHTBRACE,
    '|': e.KEY_BACKSLASH,
    ':': e.KEY_SEMICOLON,
    '"': e.KEY_APOSTROPHE,
    '<': e.KEY_COMMA,
    '>': e.KEY_DOT,
    '?': e.KEY_SLASH,
    '~': e.KEY_GRAVE,
}
_SHIFT_KEY_MAPPING: Dict[str, int] = {
    '!': e.KEY_1,
    '@': e.KEY_2,
    '#': e.KEY_3,
    '$': e.KEY_4,
    '%': e.KEY_5,
    '^': e.KEY_6,
    '&': e.KEY_7,
    '*': e.KEY_8,
    '(': e.KEY_9,
    ')': e.KEY_0,
    '_': e.KEY_MINUS,
    '+': e.KEY_EQUAL,
    '{': e.KEY_LEFTBRACE,
    '}': e.KEY_RIGHTBRACE,
    '|': e.KEY_BACKSLASH,
    ':': e.KEY_SEMICOLON,
    '"': e.KEY_APOSTROPHE,
    '<': e.KEY_COMMA,
    '>': e.KEY_DOT,
    '?': e.KEY_SLASH,
    '~': e.KEY_GRAVE,
    'A': e.KEY_A,
    'B': e.KEY_B,
    'C': e.KEY_C,
    'D': e.KEY_D,
    'E': e.KEY_E,
    'F': e.KEY_F,
    'G': e.KEY_G,
    'H': e.KEY_H,
    'I': e.KEY_I,
    'J': e.KEY_J,
    'K': e.KEY_K,
    'L': e.KEY_L,
    'M': e.KEY_M,
    'N': e.KEY_N,
    'O': e.KEY_O,
    'P': e.KEY_P,
    'Q': e.KEY_Q,
    'R': e.KEY_R,
    'S': e.KEY_S,
    'T': e.KEY_T,
    'U': e.KEY_U,
    'V': e.KEY_V,
    'W': e.KEY_W,
    'X': e.KEY_X,
    'Y': e.KEY_Y,
    'Z': e.KEY_Z,
}
# we remove KEY_ from the key names to make it easier to type
_SUPPORTED_KEYS = [key.replace("KEY_", "").lower() for key in dir(e) if key.startswith("KEY_") and key not in _BAD_ECODES]
_SUPPORTED_KEY_CONSTANTS = [value for name, value in vars(e).items() if name.startswith('KEY_') and name not in _BAD_ECODES]
# fmt: on


# Initialize UInput in a global variable so that we don't initialize each time a key is pressed
class UInputWrapper:
    def __init__(self):
        self.initialized = False
        self.device = None

    def initialize(self):
        if not self.initialized:
            print("Initializing UInput...")
            self.device = UInput({e.EV_KEY: _SUPPORTED_KEY_CONSTANTS})
            self.initialized = True


_UINPUT = UInputWrapper()


def parse_delay(key: Union[str, int]) -> Union[str, int]:
    if isinstance(key, int) or not key.startswith("delay"):
        return key
    key = key.replace("delay", "")
    if len(key) == 0:
        return _DELAY_KEYSYM + _DEFAULT_ADDITIONAL_DELAY
    delay = _DEFAULT_ADDITIONAL_DELAY
    try:
        delay = int(float(key) * 10)
    except ValueError:
        print("Cannot parse delay amount, using default delay")
    return _DELAY_KEYSYM + delay


def parse_keys(
        key: Union[str, int], key_type: Union[Dict[str, int], Dict[str, str]]) -> Union[str, int]:  # fmt: skip
    if isinstance(key, int):
        return key
    return key_type.get(key, key)


def parse_keys_as_keycodes(keys: str) -> List[List[Union[str, int]]]:
    stripped = keys.strip().replace(" ", "").lower()
    if not stripped:
        return []
    # split by , for sections
    sections = stripped.split(",")
    parsed_keys = []
    for section in sections:
        # split by + for individual keys
        individual = section.split("+")
        # filter empty strings
        individual = list(filter(None, individual))
        # replace any string with e.KEY_<string>
        individual = [getattr(e, f"KEY_{key.upper()}", key) for key in individual]
        # check if delay
        parsed: List[Union[str, int]] = [parse_delay(key) for key in individual]
        # replace special keys
        parsed = [parse_keys(key, _SPECIAL_KEYS) for key in parsed]
        # replace old numpad keys
        parsed = [parse_keys(key, _OLD_NUMPAD_KEYS) for key in parsed]
        # replace old media keys
        parsed = [parse_keys(key, _OLD_PYNPUT_KEYS) for key in parsed]
        # replace modifier keys
        parsed = [parse_keys(key, _MODIFIER_KEYS) for key in parsed]
        # replace key names with key codes
        parsed = [parse_keys(key, _KEY_MAPPING) for key in parsed]

        # if any value is not an int, raise an error
        if not all(isinstance(key, int) for key in parsed):
            invalid_keys = [key for key in parsed if not isinstance(key, int)]
            raise ValueError(f"Invalid keys: {invalid_keys}")

        if len(parsed) > 0:
            parsed_keys.append(parsed)

    return parsed_keys


def keyboard_write(string: str):
    _UINPUT.initialize()
    _ui = _UINPUT.device
    caps_lock_is_on = check_caps_lock()
    for char in string:
        is_unicode = False
        unicode_bytes = char.encode("unicode_escape")
        # '\u' or '\U' for unicode, or '\x' for UTF-8
        if unicode_bytes[0] == 92 and unicode_bytes[1] in [85, 117, 120]:
            is_unicode = True

        if char in _KEY_MAPPING:
            keycode = _KEY_MAPPING[char]
            need_shift = False

            if char in _SHIFT_KEY_MAPPING:
                need_shift = True

            if char.isalpha() and caps_lock_is_on:
                need_shift = not need_shift

            if need_shift:
                _ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)

            _ui.write(e.EV_KEY, keycode, 1)
            _ui.write(e.EV_KEY, keycode, 0)

            if need_shift:
                _ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)

            # send keys
            _ui.syn()
            time.sleep(_DEFAULT_KEY_PRESS_DELAY)
        elif is_unicode:
            unicode_hex = hex(int(unicode_bytes[2:], 16))
            unicode_hex_keys = unicode_hex[2:]

            # hold shift + ctrl
            _ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 1)
            _ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 1)

            # press 'U' to initiate unicode sequence
            _ui.write(e.EV_KEY, e.KEY_U, 1)
            _ui.write(e.EV_KEY, e.KEY_U, 0)

            # press unicode codepoint keys
            for hex_char in unicode_hex_keys:
                keycode = _KEY_MAPPING[hex_char]
                _ui.write(e.EV_KEY, keycode, 1)
                _ui.write(e.EV_KEY, keycode, 0)

            # release shift + ctrl
            _ui.write(e.EV_KEY, e.KEY_LEFTSHIFT, 0)
            _ui.write(e.EV_KEY, e.KEY_LEFTCTRL, 0)

            # send keys
            _ui.syn()
        else:
            print(f"Unsupported character: {char}")


_PRESS_KEY_THREADS: List[QThread] = []


class KeyboardThread(QThread):
    def __init__(self, keys):
        super().__init__()
        self.keys = keys

    def run(self):
        _UINPUT.initialize()
        _ui = _UINPUT.device
        sections = parse_keys_as_keycodes(self.keys)
        for section_of_keycodes in sections:
            for keycode in section_of_keycodes:
                if keycode > _DELAY_KEYSYM:
                    # if it is a delay, subtract the delay keysym from the keycode to get the delay in seconds
                    time.sleep((keycode - _DELAY_KEYSYM) / 10.0)
                    continue
                _ui.write(e.EV_KEY, keycode, 1)
                _ui.syn()
            time.sleep(_DEFAULT_KEY_PRESS_DELAY)

            for keycode in reversed(section_of_keycodes):
                _ui.write(e.EV_KEY, keycode, 0)
                _ui.syn()

            # add some delay between sections, only if there are more than one
            if len(section_of_keycodes) > 1:
                time.sleep(_DEFAULT_KEY_SECTION_DELAY)


def cleanup_keyboard_thread():
    global _PRESS_KEY_THREADS
    # Remove threads that are not running anymore
    _PRESS_KEY_THREADS = [t for t in _PRESS_KEY_THREADS if t.isRunning()]


def keyboard_press_keys(keys: str):
    global _PRESS_KEY_THREADS
    thread = KeyboardThread(keys)
    thread.finished.connect(cleanup_keyboard_thread)
    _PRESS_KEY_THREADS.append(thread)
    thread.start()


def get_valid_key_names() -> List[str]:
    """Returns a list of valid key names."""
    key_names = [key for key in _SUPPORTED_KEYS]
    key_names.extend(_SPECIAL_KEYS.keys())
    key_names.extend(_OLD_NUMPAD_KEYS.keys())
    key_names.extend(_OLD_PYNPUT_KEYS.keys())
    key_names.extend(_MODIFIER_KEYS.keys())
    return sorted(key_names)


def check_caps_lock() -> bool:
    """Returns True if Caps Lock is on, False if it is off, and False if it cannot be determined."""
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        if device.capabilities().get(e.EV_LED):
            return e.LED_CAPSL in device.leds()
    return False


class KeyPressAutoComplete(QCompleter):
    special_keys = _SPECIAL_KEYS.values()
    allowed_keys = get_valid_key_names()

    def __init__(self, parent=None):
        super(KeyPressAutoComplete, self).__init__(parent)
        model = QStringListModel()
        model.setStringList(self.allowed_keys)
        self.setModel(model)
        self.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)

    def update_prefix(self, text: str):
        """Update the prefix for the autocompletion."""
        # space " " is considered a special key in case user types, for example, "ctrl + "
        # we still can autocomplete after the space
        last_special_index = max(text.rfind(","), text.rfind("+"), text.rfind(" "))
        # if there is a special key, update model to allow autocomplete for further keys
        if last_special_index != -1:
            prefix = text[: last_special_index + 1]
            allowed_keys = [prefix + key for key in self.allowed_keys]
            self.model().setStringList(allowed_keys)  # type: ignore [attr-defined]
        # otherwise, reset model to allow autocomplete for all keys
        else:
            self.model().setStringList(self.allowed_keys)  # type: ignore [attr-defined]
        self.complete()
