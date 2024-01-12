import time

from PIL.Image import Image

from helpers.utils import get_image_pixel, click


class ExtremeScreen:
    LOGO_PIXEL = 550, 370
    START_BUTTON = 666, 746

    DUOLINGO_ORANGE_1 = (232, 127, 35)
    DUOLINGO_ORANGE_2 = (232, 127, 48)
    DUOLINGO_WHITE = (255, 255, 255)

    @classmethod
    def is_current(cls, screenshot: Image):
        logo_color = get_image_pixel(screenshot, *cls.LOGO_PIXEL)
        start_button_color = get_image_pixel(screenshot, *cls.START_BUTTON)

        # should have an orange logo in the middle and a white start button
        return (
            logo_color in [cls.DUOLINGO_ORANGE_1, cls.DUOLINGO_ORANGE_2]
            and start_button_color == cls.DUOLINGO_WHITE
        )

    def next(self):
        from screen.start import StartScreen

        print("Extreme screen found, clicking start button")
        click(*self.START_BUTTON)
        time.sleep(6)

        return StartScreen()
