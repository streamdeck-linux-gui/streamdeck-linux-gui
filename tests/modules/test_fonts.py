import json
from unittest.mock import patch

from streamdeck_ui.modules.fonts import get_fonts, reorder_font_styles

mock_fallback_fonts = {"FallbackFamily": {"Regular": "fallback_regular.ttf", "Bold": "fallback_bold.ttf"}}


def test_get_fonts_with_empty_system_fonts():
    with patch("streamdeck_ui.modules.fonts.get_system_fonts", return_value={}):
        with patch("streamdeck_ui.modules.fonts.get_fallback_fonts", return_value=mock_fallback_fonts):
            fonts_dict = get_fonts()

            # Assert that the fonts dictionary contains fallback fonts
            assert fonts_dict["FallbackFamily"]["Regular"] == "fallback_regular.ttf"
            assert fonts_dict["FallbackFamily"]["Bold"] == "fallback_bold.ttf"


def test_get_fonts_with_partial_system_fonts():
    with patch("streamdeck_ui.modules.fonts.get_system_fonts", return_value={"a": {"b": "c.ttf"}}):
        with patch("streamdeck_ui.modules.fonts.get_fallback_fonts", return_value=mock_fallback_fonts):
            fonts_dict = get_fonts()

            # Assert that the fonts dictionary contains fallback fonts
            assert fonts_dict["a"]["b"] == "c.ttf"
            assert fonts_dict["FallbackFamily"]["Regular"] == "fallback_regular.ttf"
            assert fonts_dict["FallbackFamily"]["Bold"] == "fallback_bold.ttf"


def test_reorder():
    # fmt: off
    test_fonts_1 = {
        "Font1": {
            "Regular": "path_regular.ttf",
            "A": "path_A.ttf",
            "a": "path_a.ttf",
            "B": "path_B.ttf",
            "Italic": "path_italic.ttf"
        },
        "Font2": {
            "x": "path_x.ttf",
            "Bold": "path_bold.ttf",
            "Bold Italic": "path_bold_italic.ttf",
            "Italic": "path_italic.ttf"
        },
        "Font3": {
            "Regular": "path_regular.ttf",
            "Bold": "path_bold.ttf",
            "Italic": "path_italic.ttf",
            "Bold Italic": "path_bold_italic.ttf"
        }
    }
    expected_fonts_1 = {
        "Font1": {
            "Regular": "path_regular.ttf",
            "Italic": "path_italic.ttf",
            "A": "path_A.ttf",
            "B": "path_B.ttf",
            "a": "path_a.ttf"
        },
        "Font2": {
            "Bold": "path_bold.ttf",
            "Italic": "path_italic.ttf",
            "Bold Italic": "path_bold_italic.ttf",
            "x": "path_x.ttf"
        },
        "Font3": {
            "Regular": "path_regular.ttf",
            "Bold": "path_bold.ttf",
            "Italic": "path_italic.ttf",
            "Bold Italic": "path_bold_italic.ttf"
        }
    }
    # fmt: on
    test_fonts_1_sorted = reorder_font_styles(test_fonts_1)
    assert json.dumps(test_fonts_1_sorted) == json.dumps(expected_fonts_1)
