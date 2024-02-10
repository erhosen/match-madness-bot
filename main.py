from helpers.screenshot import Screenshot
from screen._base import BaseScreen
from screen.start import StartScreen
from screen.wait_where_are_you import WaitWhereAreYouScreen


def determine_current_screen() -> type[BaseScreen]:
    screenshot = Screenshot.take()
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


# TODO: Таймер, который знает сколько секунд длится каждый уровень, и если прошло больше, чем должно было, то выходит на TimeoutScreen
# TODO: Rich, чтобы было красиво
# TODO: Typer, чтобы было удобно
# TODO: Screen collisions in general: worth to consider?
