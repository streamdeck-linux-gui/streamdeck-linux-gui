from typing import Dict

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QLayout

from streamdeck_ui.api import StreamDeckServer

NAME: str = "Plugin Template"


def get_name() -> str:
    """
    The friendly name of this plugin which will be displayed in the UI.<br /><br />
    @return: the plugin name
    """
    return NAME


def get_icon():
    """
    The icon to be displayed in the UI menu next to the name. Optional.<br /><br />
    @return: the plugin icon
    """
    return None


def get_settings_layout(parent, old_settings: Dict[str, str]):
    """
    If the plugin needs extra settings (like credentials), they can be entered with this Layout. In the plugin-menu,
    each plugin has an entry and if this function returns a layout, it is embedded in a dialog where the user can change
    the settings and either cancel or confirm the dialog.<br /><br />
    Important: The layout must define a function <code>get_settings()</code> which will be called if the settings were
    changed, and the result sent to the <code>apply_settings()</code> function.<br /><br />
    @param parent: the parent dialog<br />
    @param old_settings: the current plugin settings to be displayed<br />
    @return: the plugin's settings layout
    """
    return None


def apply_settings(settings: Dict[str, str]) -> None:
    """
    The settings entered in the plugin's settings layout are sent here to be processed. If the plugin does not provide a
     settings layout, this function doesn't need to do anything.
    """
    pass


def get_button_settings_layout(parent, old_settings: Dict[str, str]) -> QLayout:
    """
    Returns the layout to provide a dialog to configure settings for a single button with this plugin.<br /><br />
    Important: The layout must define a function <code>get_settings()</code> which will be called if the button
    settings were changed, and the result sent to the <code>apply_button_settings()</code> function.<br /><br />
    @param parent: the parent dialog<br />
    @param old_settings: the current plugin button settings to be displayed<br />
    @return: the plugin's button settings layout
    """
    return QLayout(parent)


def apply_button_settings(deck_id: str, page_id: int, button_id: int, button_settings: Dict[str, str]) -> None:
    """
    The settings entered in the plugin's button settings layout are sent here to be processed.
    """
    pass


def button_pressed(deck_id: str, page_id: int, button_id: int, button_settings: Dict[str, str]) -> None:
    """
    This function is called when a button (key) on the Stream Deck is pressed and button settings were provided for this
    plugin.
    """
    pass


def initialize(api: StreamDeckServer, settings: Dict[str, str]) -> None:
    """
    This function is called right after the application is started. The settings previously entered for this plugin are
    provided and the plugin may store the api reference for future callbacks.
    """
    pass
