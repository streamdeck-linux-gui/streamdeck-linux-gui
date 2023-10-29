from fractions import Fraction
from typing import Callable, Tuple

from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pilmoji import Pilmoji

from streamdeck_ui.config import DEFAULT_FONT_FALLBACK_PATH
from streamdeck_ui.display.filter import Filter


class TextFilter(Filter):
    font_blur: ImageFilter.Kernel = None
    # Static instance - no need to create one per Filter instance

    image: Image

    def __init__(
        self, text: str, font: str, font_size: int, font_color: str, vertical_align: str, horizontal_align: str
    ):
        super(TextFilter, self).__init__()
        self.text = text
        self.vertical_align = vertical_align or "bottom"
        self.horizontal_align = horizontal_align or "center"
        self.font_color = font_color
        self.fallback_font = ImageFont.truetype(DEFAULT_FONT_FALLBACK_PATH, font_size)
        self.true_font = ImageFont.truetype(font, font_size)
        # fmt: off
        kernel = [
            0, 1, 2, 1, 0,
            1, 2, 4, 2, 1,
            2, 4, 8, 4, 1,
            1, 2, 4, 2, 1,
            0, 1, 2, 1, 0]
        # fmt: on
        TextFilter.font_blur = ImageFilter.Kernel((5, 5), kernel, scale=0.1 * sum(kernel))
        self.offset = 0.0
        self.offset_direction = 1
        self.image = None

        # Hashcode should be created for anything that makes this frame unique
        self.hashcode = hash((self.__class__, text, font, font_size, font_color, vertical_align, horizontal_align))

    def initialize(self, size: Tuple[int, int]):
        self.image = Image.new("RGBA", size)
        try:
            self.initialize_emoji(size)
        except OSError:
            self.initialize_legacy_text(size)

    def initialize_emoji(self, size: Tuple[int, int]):
        with Pilmoji(self.image) as pilmoji:
            # Split the text by newline to determine label height
            # then grab the longest word to determine label width
            text_split_newline = sorted(self.text.split("\n"), key=len)
            # Calculate the height and width of the text we're drawing, using the font itself Previously we counted
            # the number of characters to determine the width, but if the font wasn't a fixed width the horizontal
            # alignment would be off.
            label_w, _ = pilmoji.getsize(text=self.text, font=self.true_font)
            # Calculate dimensions for text that include ascender (above the line)
            # and below the line  (descender) characters. This is used to adjust the
            # font placement and should allow for button text to horizontally align
            # across buttons. Basically we want to figure out what is the tallest
            # text we will need to draw.
            _, label_h = pilmoji.getsize("\n".join(["lLpgyL|"] * len(text_split_newline)), font=self.true_font)

            label_pos = self.get_pos(
                vertical_align=self.vertical_align,
                horizontal_align=self.horizontal_align,
                size=size,
                label_h=label_h,
                label_w=label_w,
            )
            pilmoji.text(
                label_pos,
                text=self.text,
                font=self.true_font,
                fill=self.font_color,
                align=self.horizontal_align,
                spacing=0,
                stroke_fill="black",
                stroke_width=2,
            )

    def get_pos(self, vertical_align, horizontal_align, size, label_h, label_w) -> Tuple[int, int]:
        gap = (size[1] - 5 * label_h) // 4

        if vertical_align == "top":
            label_y = 0
        elif vertical_align == "middle-top":
            label_y = gap + label_h
        elif vertical_align == "middle":
            label_y = size[1] // 2 - (label_h // 2)
        elif vertical_align == "middle-bottom":
            label_y = (gap + label_h) * 3
        else:
            label_y = size[1] - label_h
            # Default or "bottom"

        if horizontal_align == "left":
            label_x = 0
        elif horizontal_align == "right":
            label_x = size[0] - label_w
        else:
            label_x = (size[0] - label_w) // 2
            # Default or "center"
        return label_x, label_y

    def initialize_legacy_text(self, size: Tuple[int, int]):
        foreground_draw = ImageDraw.Draw(self.image)
        # Split the text by newline to determine label height
        # then grab the longest word to determine label width
        text_split_newline = sorted(self.text.split("\n"), key=len)
        # Calculate the height and width of the text we're drawing, using the font itself
        # Previously we counted the number of characters to determine the width, but if the font wasn't a fixed width
        # the horizontal alignment would be off.
        _, _, label_w, _ = foreground_draw.textbbox((0, 0), self.text, font=self.true_font)
        # Calculate dimensions for text that include ascender (above the line)
        # and below the line  (descender) characters. This is used to adjust the
        # font placement and should allow for button text to horizontally align
        # across buttons. Basically we want to figure out what is the tallest
        # text we will need to draw.
        _, _, _, label_h = foreground_draw.textbbox(
            (0, 0), "\n".join(["lLpgyL|"] * len(text_split_newline)), font=self.true_font
        )

        label_pos = self.get_pos(
            vertical_align=self.vertical_align,
            horizontal_align=self.horizontal_align,
            size=size,
            label_h=label_h,
            label_w=label_w,
        )

        try:
            foreground_draw.multiline_text(
                label_pos,
                text=self.text,
                font=self.true_font,
                fill=self.font_color,
                align=self.horizontal_align,
                spacing=0,
                stroke_fill="black",
                stroke_width=2,
            )
        except OSError:
            print("Font does not render with pillow, falling back to default font.")
            foreground_draw.multiline_text(
                label_pos,
                text=self.text,
                font=self.fallback_font,
                fill=self.font_color,
                align=self.horizontal_align,
                spacing=0,
                stroke_fill="black",
                stroke_width=2,
            )

    def transform(
        self,
        get_input: Callable[[], Image.Image],
        get_output: Callable[[int], Image.Image],
        input_changed: bool,
        time: Fraction,
    ) -> Tuple[Image.Image, int]:
        """
        The transformation returns the loaded image, ando overwrites whatever came before.
        """

        if input_changed:
            image = get_output(self.hashcode)
            if image:
                return (image, self.hashcode)

            input = get_input()
            input.paste(self.image, self.image)
            return (input, self.hashcode)
        return (None, self.hashcode)


def is_a_valid_text_filter_font(font) -> bool:
    try:
        TextFilter("", font, 12, "white", "top", "left")
        return True
    except BaseException:
        return False
