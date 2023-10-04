import pyautogui
import cv2
from PIL import Image


# get the full screen image
def screen_image() -> Image:
    position = pyautogui.locateOnScreen("resource/locate.png", confidence=0.95)
    if position is None:
        return None
    x = position.left + position.width - 1280
    y = position.top + position.height - 720
    screenshot = pyautogui.screenshot(region=(x, y, 1280, 720))
    return screenshot


# given a full screen image, return the current score
def score(image: Image) -> int:
    image.crop((72, 100, 313, 170)).show()


screen = screen_image()
score(screen)
