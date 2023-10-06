import keyboard
import time
from PIL import Image

KEY_RIGHT = keyboard.parse_hotkey("right")
KEY_LEFT = keyboard.parse_hotkey("left")
KEY_CONFIRM = keyboard.parse_hotkey("c")


MIN_POSITION = 0
MAX_POSITION = 372


class Controller:
    @staticmethod
    def move_to_zero():
        keyboard.press(KEY_LEFT)
        time.sleep(1.5)
        keyboard.release(KEY_LEFT)

    @staticmethod
    def move_to_position(source: int, target: int):
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

    @staticmethod
    def is_left_edge(position: int) -> bool:
        return abs(position - MIN_POSITION) < 7

    @staticmethod
    def is_right_edge(position: int) -> bool:
        return abs(position - MAX_POSITION) < 7

    @staticmethod
    def click_left():
        keyboard.press(KEY_LEFT)
        time.sleep(0.001)
        keyboard.release(KEY_LEFT)

    @staticmethod
    def click_right():
        keyboard.press(KEY_RIGHT)
        time.sleep(0.001)
        keyboard.release(KEY_RIGHT)

    @staticmethod
    def click_confirm():
        keyboard.press(KEY_CONFIRM)
        time.sleep(0.001)
        keyboard.release(KEY_CONFIRM)

    @staticmethod
    def restart():
        time.sleep(1)
        Controller.click_confirm()
        time.sleep(1)
        Controller.click_left()
        time.sleep(1)
        Controller.click_confirm()
        time.sleep(10)
