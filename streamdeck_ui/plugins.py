import os.path
import runpy
import threading
import traceback
from abc import ABC, abstractmethod
from typing import List, Type

from streamdeck_ui.display.filter import Filter


def prepare_plugin(**kwargs):
    api = kwargs.get("api", None)
    serial_number = kwargs.get('serial_number', None)
    page = kwargs.get('page', None)
    button_id = kwargs.get('button_id', None)
    plugin_path = kwargs.get('plugin_path', None)
    plugin: Type[BasePlugin] = None

    if api.get_button_plugin_path(serial_number, page, button_id) is not None:
        try:
            full_path = os.path.expanduser(os.path.expandvars(plugin_path))
            result = runpy.run_path(full_path)
            if 'initialize_plugin' in result and callable(result['initialize_plugin']):
                api.set_button_plugin_path(serial_number, page, button_id, plugin_path)
                plugin = result['initialize_plugin'](**kwargs)
                api.set_button_plugin(serial_number, page, button_id, plugin)
            elif kwargs.get('non_optional', False):
                print(f"Function initialize_plugin not found in {plugin_path}")
        except Exception as error:
            print(f"Error while calling initialize_plugin in {plugin_path}: {error}")
            return None
    return api.get_button_plugin(serial_number, page, button_id)


def stop_all_plugins(api, serial_number):
    state = api.state[serial_number]
    for page_id in state.buttons:
        for button_id in state.buttons[page_id]:
            plugin = api.get_button_plugin(serial_number, page_id, button_id)
            if plugin is not None:
                plugin.stop()
            api.set_button_plugin(serial_number, page_id, button_id, None)


class BasePlugin(ABC):
    lock: threading.Lock = threading.Lock()

    def __init__(self, **kwargs):
        self.api = kwargs.get("api", None)
        self.page = kwargs.get("page", None)
        self.serial_number = kwargs.get("serial_number", None)
        self.button_id = kwargs.get("button_id", None)
        self.filters: List[Filter] = []
        self.actions = []

    def stop(self):
        self.lock.acquire()
        self.lock.release()

    def get_button_state(self):
        return self.api.get_button_state(self.serial_number, self.page, self.button_id)

    def synchronize(self, button_state):
        self.api._update_button_filters(button_state, self.serial_number, self.page, self.button_id)

    def handle_keypress(self, **kwargs):
        pass

    def get_filters(self, **kwargs) -> List[Filter]:
        return self.filters

    def get_actions(self, **kwargs):
        return self.actions