from PySide6.QtWidgets import QLabel

from streamdeck_ui.plugins import Plugin


class DemoPlugin(Plugin):
    def create_ui(self, pluginForm):
        label = QLabel(pluginForm)
        label.setText("THIS IF FINALLY WORKING!!!")

    def handle_keypress(self):
        pass

    @staticmethod
    def initialize_plugin():
        return DemoPlugin()
