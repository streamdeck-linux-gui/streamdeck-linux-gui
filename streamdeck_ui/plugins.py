import inspect
import os
import runpy
import threading
from abc import ABC, abstractmethod
from typing import Callable

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Slot, SIGNAL, SLOT


class Plugin(ABC):
    lock: threading.Lock
    _autostart: bool = False

    button_change_text: Callable[[str, int, int, str], None]
    """Function that gets overridden"""

    button_change_background: Callable[[str, int, int, str], None]
    """Changes the background color on the button in the format: #000000"""

    button_change_icon: Callable[[str, int, int, str], None]
    """
    Change the icon of a button on a specific page identified by its serial number.
        - serial_number (str): The serial number of the device containing the button.
        - page (int): The page number where the button is located.
        - button (int): The identifier of the button whose icon needs to be changed.
        - path (str): The path to the new icon image.
    """

    @property
    def serial_number(self):
        return self._serial_number

    @property
    def page_id(self):
        return self._page_id

    @property
    def button_id(self):
        return self._button_id

    @abstractmethod
    def __init__(self, serial_number: str, page_id: int, button_id: int):
        """Actually creates the instance of the plugin"""
        self._serial_number = serial_number
        self._page_id = page_id
        self._button_id = button_id

        if self._autostart:
            self.start()

    def start(self):
        if self.lock is None:
            self.lock = threading.Lock()

    def stop(self):
        self.lock.acquire()
        self.lock.release()

    @abstractmethod
    def create_ui(self, plugin_form: QWidget):
        """Used to define the UI that every Plugin displays"""
        pass

    @abstractmethod
    def handle_keypress(self, serial_number: str, page: int, button: int):
        """Gets called when a button gets pressed"""
        pass

    @abstractmethod
    def handle_change_button_state(self, serial_number: str, page: int, button: int, state: int):
        """Gets called when the button state changes"""
        pass

    @staticmethod
    @abstractmethod
    def initialize_plugin(serial_number: str, page_id: int, button_id: int):
        """Initializes the plugin, MUST be replaced with an override and MUST return the Plugin"""
        return None


def prepare_plugin(api, plugin_path: str, serial_number: str, page_id: int, button_id: int) -> Plugin:
    plugin = None
    try:
        full_path = os.path.expanduser(os.path.expandvars(plugin_path))
        result = runpy.run_path(full_path)
        for name, obj in result.items():
            if inspect.isclass(obj) and issubclass(obj, Plugin) and hasattr(obj, 'initialize_plugin') and callable(
                    getattr(obj, 'initialize_plugin')) and obj != Plugin:
                plugin = obj.initialize_plugin(serial_number, page_id, button_id)

                # Connects event functions to the api
                plugin.button_change_text = api.on_update_button_text
                plugin.button_change_background = api.on_update_button_background_color
                plugin.button_change_icon = api.on_update_button_icon

                break
        if plugin is None:
            print("No valid plugin class found in the module.")
    except Exception as e:
        print(f"Error while calling initialize_plugin in {plugin_path}: {e}")
    return plugin


def stop_all_plugins(api, serial_number):
    state = api.state[serial_number]
    for page_id in state.buttons:
        for button_id in state.buttons[page_id]:
            plugin = api.get_button_plugin(serial_number, page_id, button_id)
            if plugin is not None:
                plugin.stop()
            api.set_button_plugin(serial_number, page_id, button_id, None)
