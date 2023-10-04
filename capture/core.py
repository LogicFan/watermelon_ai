from PIL import Image
import pyautogui
import pytesseract
import cv2
import numpy

pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
)


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
    image = numpy.array(image.crop((72, 115, 313, 165)))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    text = pytesseract.image_to_string(
        image, lang="eng", config="--psm 8 -c tessedit_char_whitelist=0123456789"
    )
    return int(text)


screen = screen_image()
print(score(screen))
