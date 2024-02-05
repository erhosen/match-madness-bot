from helpers.utils import take_screenshot
from screen._base import BaseScreen
from screen.start import StartScreen
from screen.wait_where_are_you import WaitWhereAreYouScreen


def determine_current_screen() -> type[BaseScreen]:
    screenshot = take_screenshot()
    for screen_cls in [StartScreen, WaitWhereAreYouScreen]:
        if screen_cls.is_current(screenshot):
            return screen_cls

    raise ValueError("Can't determine current screen")


def main():
    screen_cls = determine_current_screen()
    screen = screen_cls()
    while True:
        screen = screen.next()


if __name__ == "__main__":
    main()
    # profiler = Profiler()
    # profiler.start()
    #
    # try:
    #     main()
    # except (KeyboardInterrupt, FailSafeException):
    #     pass
    #
    # profiler.stop()
    # profiler.print(show_all=False)


# TODO: Сохранять всегда оригиналы, чтобы можно было писать тесты
# TODO: Если что-то идет не так, например неожиданный экран, то сделать скриншот и сохранить в screen/unexpected.png
# TODO: Таймер, который знает сколько секунд длится каждый уровень, и если прошло больше, чем должно было, то выходит на TimeoutScreen
# TODO: Rich, чтобы было красиво
# TODO: Typer, чтобы было удобно
# TODO: IntermediateScreen / ExtremeScreen collision
# TODO: Screens collision in general. Stop using pixel_matches_color, use image matching instead
# TODO: Make sure it works fine on different screens / resolutions
