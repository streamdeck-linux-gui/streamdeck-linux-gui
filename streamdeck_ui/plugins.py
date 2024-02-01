import inspect
import os
import runpy
import threading
from abc import ABC, abstractmethod

def stop_all_plugins(api, serial_number):
    state = api.state[serial_number]
    for page_id in state.buttons:
        for button_id in state.buttons[page_id]:
            plugin = api.get_button_plugin(serial_number, page_id, button_id)
            if plugin is not None:
                plugin.stop()
            api.set_button_plugin(serial_number, page_id, button_id, None)


class Plugin(ABC):
    lock: threading.Lock
    _autostart: bool = False

    def __init__(self):
        if self._autostart:
            self.start()

    def start(self):
        if self.lock is None:
            self.lock = threading.Lock()

    def stop(self):
        self.lock.acquire()
        self.lock.release()

    @abstractmethod
    def create_ui(self, pluginForm):
        pass

    @abstractmethod
    def handle_keypress(self):
        pass

    @staticmethod
    @abstractmethod
    def initialize_plugin():
        return None


def prepare_plugin(plugin_path: str) -> Plugin:
    plugin = None
    try:
        full_path = os.path.expanduser(os.path.expandvars(plugin_path))
        result = runpy.run_path(full_path)
        for name, obj in result.items():
            if inspect.isclass(obj) and issubclass(obj, Plugin) and hasattr(obj, 'initialize_plugin') and callable(getattr(obj, 'initialize_plugin')) and obj != Plugin:
                plugin = obj.initialize_plugin()
                break
        if plugin is None:
            print("No valid plugin class found in the module.")
    except Exception as e:
        print(f"Error while calling initialize_plugin in {plugin_path}: {e}")
    return plugin
