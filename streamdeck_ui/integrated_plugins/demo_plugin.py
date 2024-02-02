from PySide6.QtWidgets import QLabel, QWidget, QPushButton

from streamdeck_ui.plugins import Plugin


class DemoPlugin(Plugin):
    toggled = False

    def __init__(self, serial_number: str, page_id: int, button_id: int):
        super().__init__(serial_number, page_id, button_id)

    def create_ui(self, plugin_form: QWidget):
        pass

    def handle_keypress(self, serial_number: str, page: int, button: int):
        if self.toggled:
            self.button_change_icon(serial_number, page, button, "")
        else:
            self.button_change_icon(serial_number, page, button, "/home/gapls/Pictures/2024-01-31_17-39.png")
        self.toggled = not self.toggled

    def handle_change_button_state(self, serial_number: str, page: int, button: int, state: int):
        pass

    @staticmethod
    def initialize_plugin(serial_number: str, page_id: int, button_id: int):
        return DemoPlugin(serial_number, page_id, button_id)