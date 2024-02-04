import json
from dataclasses import dataclass, asdict

from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QLabel, QWidget, QSizePolicy, QFormLayout, QComboBox, QHBoxLayout, \
    QRadioButton, QSlider, QVBoxLayout

from streamdeck_ui.plugins import Plugin, PluginConfig


@dataclass
class DemoPluginConfig(PluginConfig):
    last_checked: str = ""

    @property
    def json(self):
        return json.dumps(asdict(self))

    @classmethod
    def from_json(cls, json_str):
        try:
            json_data = json.loads(json_str)
            return cls(**json_data)
        except:
            return None


class DemoPlugin(Plugin):
    toggled = False
    config: DemoPluginConfig

    def __init__(self, serial_number: str, page_id: int, button_id: int, plugin_config: str = ""):
        super().__init__(serial_number, page_id, button_id)
        self.config = DemoPluginConfig.from_json(plugin_config)
        if self.config is None:
            self.config = DemoPluginConfig()

    def create_ui(self, plugin_form: QWidget):
        # Creates a vertical layout for the plugin_form so that everything stretches nicely
        label = QLabel(plugin_form)
        label.setText("DEMO PLUGIN")

    def handle_keypress(self, serial_number: str, page: int, button: int):
        print("DEMO PLUGIN")
        self.toggled = not self.toggled

    def handle_change_button_state(self, serial_number: str, page: int, button: int, state: int):
        print(state)

    @staticmethod
    def initialize_plugin(serial_number: str, page_id: int, button_id: int, plugin_config: str = ""):
        return DemoPlugin(serial_number, page_id, button_id, plugin_config)
