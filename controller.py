import keyboard
import time
from PIL import Image

import capture

KEY_RIGHT = keyboard.parse_hotkey("right")
KEY_LEFT = keyboard.parse_hotkey("left")


MIN_POSITION = 0
MAX_POSITION = 372


# move to target position
def move_to(target: int, frame: Image):
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
def step_right():
    keyboard.press(KEY_RIGHT)
    time.sleep(0.001)
    keyboard.release(KEY_RIGHT)


# 1 step left
def step_left():
    keyboard.press(KEY_LEFT)
    time.sleep(0.001)
    keyboard.release(KEY_LEFT)
