import keyboard
import time
from PIL import Image

import capture

KEY_RIGHT = keyboard.parse_hotkey("right")
KEY_LEFT = keyboard.parse_hotkey("left")
KEY_CONFIRM = keyboard.parse_hotkey("c")


MIN_POSITION = 0
MAX_POSITION = 372


# reset to 0 position
def zero():
    keyboard.press(KEY_LEFT)
    time.sleep(1.5)
    keyboard.release(KEY_LEFT)


# move to target position
def move(target: int, frame: Image):
    source = capture.drop_position(frame)
    if target > source:
        t = 3.5 * (target - source)
        keyboard.press(KEY_RIGHT)
        time.sleep(t / 1000.0)
        keyboard.release(KEY_RIGHT)
    elif target < source:
        t = 3.5 * (source - target)
        keyboard.press(KEY_LEFT)
        time.sleep(t / 1000.0)
        keyboard.release(KEY_LEFT)


# 1 step right
def right():
    keyboard.press(KEY_RIGHT)
    time.sleep(0.001)
    keyboard.release(KEY_RIGHT)


# 1 step left
def left():
    keyboard.press(KEY_LEFT)
    time.sleep(0.001)
    keyboard.release(KEY_LEFT)


def confirm():
    keyboard.press(KEY_CONFIRM)
    time.sleep(0.001)
    keyboard.release(KEY_CONFIRM)


def restart():
    time.sleep(1)
    confirm()
    time.sleep(1)
    left()
    time.sleep(1)
    confirm()
    time.sleep(10)
