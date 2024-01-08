import time

from PIL.Image import Image

from helpers.utils import get_image_pixel, click


class ExtremeScreen:
    LOGO_PIXEL = 530, 345
    START_BUTTON = 666, 746

    DUOLINGO_ORANGE = (247, 114, 35)
    DUOLINGO_WHITE = (255, 255, 255)

    @classmethod
    def is_current(cls, screenshot: Image):
        logo_color = get_image_pixel(screenshot, *cls.LOGO_PIXEL)
        start_button_color = get_image_pixel(screenshot, *cls.START_BUTTON)
        # print(f"logo_color: {logo_color}, start_button_color: {start_button_color}")
        # should have an orange logo in the middle and a white start button
        if (
            logo_color == cls.DUOLINGO_ORANGE
            and start_button_color == cls.DUOLINGO_WHITE
        ):
            return True

        return False

    def next(self):
        from screen.start import StartScreen

        print("Extreme screen found, clicking start button")
        click(*self.START_BUTTON)
        time.sleep(6)

        return StartScreen()
