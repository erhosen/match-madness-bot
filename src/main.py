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
    main()


# Todo: make counter for long sleep
# TODO: loguru instead of print
# Todo: Не хотите вернуться на уровень 1?
