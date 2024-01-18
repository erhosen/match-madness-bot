from pyautogui import FailSafeException
from pyinstrument import Profiler

from screen import StartScreen


def main():
    screen = StartScreen()
    while True:
        screen = screen.next()

        # try:
        #     start(game_screen)
        #     time.sleep(4)
        # except ValueError:
        #     print("ValueError occurred, restarting...")
        #     click_no_thanks_button()
        #     time.sleep(2)
        #     click_left_next_button()
        #     time.sleep(9)
        #     click_next_button()
        #     time.sleep(2)


if __name__ == "__main__":
    profiler = Profiler()
    profiler.start()

    try:
        main()
    except (KeyboardInterrupt, FailSafeException):
        pass

    profiler.stop()
    profiler.print(show_all=False)


# TODO: loguru instead of print
# TODO: Не хотите вернуться на уровень 1?
# TODO: КАЧЕСТВО
# TODO: Сохранять всегда оригиналы, чтобы можно было писать тесты
# TODO: Если что-то идет не так, например неожиданный экран, то сделать скриншот и сохранить в screen/unexpected.png
# TODO: Rich, чтобы было красиво
# TODO: Typer, чтобы было удобно
# TODO: Сделать проверку на FinishedScreen, порой он пояляется долго. Сейчас проверки нет, и мы якобы находимся на StartScreen, хотя на самом деле на FinishedScreen
