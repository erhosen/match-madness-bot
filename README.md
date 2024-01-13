# Match Madness Bot

## Description

This bot will play in Duolingo's Match Madness game.
It will play the game for you and get you the maximum amount of points possible.

## How it works

Then it uses [pyautogui](https://pyautogui.readthedocs.io/en/latest/) to take screenshots and click on the game board.
And [pytesseract](https://pypi.org/project/pytesseract/) to recognize the letters on the game board.

## Installation

1. Clone the repository
2. Make virtual environment `python3 -m venv venv`
3. Activate virtual environment `source venv/bin/activate`
4. `brew install tesseract`
5. `poetry install`

## How to use

1. Open the Match Madness game in Duolingo.
    * Right now bot supports only MacOS version of [Duolingo app](https://apps.apple.com/us/app/duolingo-language-lessons/id570060128).
2. Make sure that the game window is in the top left corner of the screen and visible.
3. `make run`
