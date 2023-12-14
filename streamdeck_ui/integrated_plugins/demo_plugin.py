from streamdeck_ui.plugins import BasePlugin


class DemoPlugin(BasePlugin):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def handle_keypress(self, **kwargs):
        print("I'm Just a demo plugin")


def initialize_plugin(**kwargs) -> DemoPlugin:
    return DemoPlugin(**kwargs)
