from screen import StartScreen


def main():
    screen = StartScreen()
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
# TODO: RateUsScreen, (после FinishScreen, перед StartScreen, sort of IntermediateScreen)
# TODO: IntermediateScreen / ExtremeScreen collision
# TODO: Screens collision in general. Stop using pixel_matches_color, use image matching instead
# TODO: Make sure it works fine on different screens / resolutions
