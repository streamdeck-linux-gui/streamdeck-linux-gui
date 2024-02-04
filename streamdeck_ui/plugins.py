import inspect
import os
import runpy
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Union

from PySide6.QtWidgets import QWidget


@dataclass
class PluginConfig(ABC):
    @property
    @abstractmethod
    def json(self):
        pass

    @classmethod
    @abstractmethod
    def from_json(cls, json_str):
        pass


class Plugin(ABC):
    lock: threading.Lock
    config: PluginConfig = None

    _button_change_text_callback: Callable[[str, int, int, str], None] = None
    _button_change_background_callback: Callable[[str, int, int, str], None] = None
    _button_change_icon_callback: Callable[[str, int, int, str], None] = None
    _plugin_change_config_callback: Callable[[str, int, int], None] = None

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

        #self.start()

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
    def initialize_plugin(serial_number: str, page_id: int, button_id: int, plugin_config: str = ""):
        """Initializes the plugin, MUST be replaced with an override and MUST return the Plugin"""
        return None

    # === Event Properties ===
    # These events are going out from the Plugin and get handled by the api
    @property
    def change_text_callback(self) -> Callable[[str, int, int, str], None]:
        if self._button_change_text_callback is None:
            return lambda _, __, ___, ____: None
        return self._button_change_text_callback

    @change_text_callback.setter
    def change_text_callback(self, callback: Callable[[str, int, int, str], None]) -> None:
        if self._button_change_text_callback is None:
            self._button_change_text_callback = callback

    @property
    def change_background_callback(self) -> Callable[[str, int, int, str], None]:
        if self._button_change_background_callback is None:
            return lambda _, __, ___, ____: None
        return self._button_change_background_callback

    @change_background_callback.setter
    def change_background_callback(self, callback: Callable[[str, int, int, str], None]) -> None:
        if self._button_change_background_callback is None:
            self._button_change_background_callback = callback

    @property
    def change_icon_callback(self) -> Callable[[str, int, int, str], None]:
        if self._button_change_icon_callback is None:
            return lambda _, __, ___, ____: None
        return self._button_change_icon_callback

    @change_icon_callback.setter
    def change_icon_callback(self, callback: Callable[[str, int, int, str], None]) -> None:
        if self.change_icon_callback is None:
            self._button_change_icon_callback = callback

    @property
    def change_config_callback(self) -> Callable[[str, int, int], None]:
        if self._plugin_change_config_callback is None:
            return lambda _, __, ___: None
        return self._plugin_change_config_callback

    @change_config_callback.setter
    def change_config_callback(self, callback: Callable[[str, int, int], None]) -> None:
        if self.change_config_callback is None:
            self._plugin_change_config_callback = callback


def stop_all_plugins(api, serial_number):
    state = api.state[serial_number]
    for page_id in state.buttons:
        for button_id in state.buttons[page_id]:
            plugin = api.get_button_plugin(serial_number, page_id, button_id)
            if plugin is not None:
                plugin.stop()
            api.set_button_plugin(serial_number, page_id, button_id, None)
