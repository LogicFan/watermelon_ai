from PIL import Image
import pyautogui
import pytesseract
import cv2
import numpy

pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


class GameOverException(Exception):
    pass


# get the full screen image
def screen_image() -> Image:
    pos = pyautogui.locateOnScreen("resource/locate.png", confidence=0.95)
    if pos is None:
        raise GameOverException()
    x = pos.left + pos.width - 1280
    y = pos.top + pos.height - 720
    screenshot = pyautogui.screenshot(region=(x, y, 1280, 720))
    return screenshot


# given a full screen image, return the current score
def score(img: Image) -> int:
    img = numpy.array(img.crop((72, 115, 313, 165)))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text: str = pytesseract.image_to_string(
        img, lang="eng", config="--psm 8 -c tessedit_char_whitelist=0123456789"
    )

    # some hacky post processing
    if int(text) > 4000:
        text.replace("71", "7")

    if int(text) > 4000 and text[0] == "7":
        text[0] = "1"

    return int(text)


def playground(img: Image) -> Image:
    return img.crop((404, 0, 876, 687))


# return a value between 0 and 327
def drop_position(img: Image) -> int:
    pos = pyautogui.locate("resource/drop.png", img, confidence=0.8)
    pos = pos.left - 491
    return pos
