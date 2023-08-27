import time

pynput_supported: bool = True

try:
    from pynput.keyboard import Controller, Key, KeyCode
except ImportError as pynput_error:
    Controller = None
    pynput_supported = False
    print("---------------")
    print("*** Warning ***")
    print("---------------")
    print("Virtual keyboard functionality has been disabled.")
    print("You can still run Stream Deck UI, however you will not be able to emulate key presses or text typing.")
    print("The most likely reason you are seeing this message is because you don't have an X server running")
    print("and your operating system uses Wayland.")
    print("")
    print(f"For troubleshooting purposes, the actual error is: \n{pynput_error}")


def _replace_special_keys_numpad(key):
    number_base = int(0xFFB0)
    # if numpad_{code} is a number
    if key[7:].isdigit():
        return f"{hex(int(key[7:], 16) + number_base)}"
    if key[7:] == "enter":
        return "0xff8d"
    if key[7:] == "decimal":
        return "0xffae"
    if key[7:] == "divide":
        return "0xffaf"
    if key[7:] == "multiply":
        return "0xffaa"
    if key[7:] == "subtract":
        return "0xffad"
    if key[7:] == "add":
        return "0xffab"
    if key[7:] == "equal":
        return "0xffbd"
    return key


def _replace_special_keys(key):
    """Replaces special keywords the user can use with their character equivalent."""
    if key.lower() == "plus":
        return "+"
    if key.lower() == "comma":
        return ","
    if key.lower().startswith("delay"):
        return key.lower()
    if key.lower().startswith("numpad_"):
        return _replace_special_keys_numpad(key)
    return key


class Keyboard:
    pynput_supported: bool
    keyboard: Controller

    _CONTROL_CODES = {
        '\n': Key.enter,
        '\r': Key.enter,
        '\t': Key.tab
    }

    _SPECIAL_COMMANDS = {
        'plus': '+',
        'comma': ','
    }

    def __init__(self):
        if pynput_supported:
            self.keyboard = Controller()
        self.pynput_supported = pynput_supported

    def write(self, string: str):
        """Types a string.

        This method will send all key presses and releases necessary to type
        all characters in the string.

        :param str string: The string to type.

        :raises InvalidCharacterException: if a non-typable character is encountered
        """
        if not self.pynput_supported:
            raise Exception("Virtual keyboard functionality is not supported on this system.")

        for i, character in enumerate(string):
            key = self._CONTROL_CODES.get(character, character)
            try:
                self.keyboard.press(key)
                self.keyboard.release(key)
                time.sleep(0.015)

            except (ValueError, Controller.InvalidKeyException):
                raise Controller.InvalidCharacterException(i, character)

    def keys(self, string: str):
        if not self.pynput_supported:
            raise Exception("Virtual keyboard functionality is not supported on this system.")

        sections = string.strip().replace(" ", "").split(",")

        for section in sections:
            # Since + and , are used to delimit our section and keys to press,
            # they need to be substituted with keywords.
            section_keys = [_replace_special_keys(key_name) for key_name in section.split("+")]

            # Translate string to enum, or just the string itself if not found
            section_keys = [getattr(Key, key_name.lower(), key_name) for key_name in section_keys]

            for key_name in section_keys:
                if isinstance(key_name, str) and key_name.startswith("delay"):
                    sleep_time_arg = key_name.split("delay", 1)[1]
                    if sleep_time_arg:
                        try:
                            sleep_time = float(sleep_time_arg)
                        except Exception:
                            print(f"Could not convert sleep time to float '{sleep_time_arg}'")
                            sleep_time = 0
                    else:
                        # default if not specified
                        sleep_time = 0.5

                    if sleep_time:
                        try:
                            time.sleep(sleep_time)
                        except Exception:
                            print(f"Could not sleep with provided sleep time '{sleep_time}'")
                else:
                    try:
                        if isinstance(key_name, str) and key_name.lower().startswith("0x"):
                            self.keyboard.press(KeyCode(int(key_name, 16)))
                        else:
                            self.keyboard.press(key_name)

                    except Exception:
                        print(f"Could not press key '{key_name}'")

            for key_name in section_keys:
                if not (isinstance(key_name, str) and key_name.startswith("delay")):
                    try:
                        if isinstance(key_name, str) and key_name.lower().startswith("0x"):
                            self.keyboard.release(KeyCode(int(key_name, 16)))
                        else:
                            self.keyboard.release(key_name)
                    except Exception:
                        print(f"Could not release key '{key_name}'")