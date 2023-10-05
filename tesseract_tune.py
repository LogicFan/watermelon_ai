from PIL import Image
import pyautogui
import pytesseract
import cv2
import numpy
import os
import capture

count = 0


os.makedirs("data/num-ground-truth/", exist_ok=True)


def write(img: Image, score: int):
    global count

    img = numpy.array(img.crop((72, 115, 313, 165)))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    Image.fromarray(img).save(f"data/num-ground-truth/{count:0>5}.png")
    with open(f"data/num-ground-truth/{count:0>5}.gt.txt", "w") as f:
        f.write(str(score))

    count += 1


for run in os.listdir("data/raw"):
    print(f"processing run {run}")
    for filename in os.listdir(f"data/raw/{run}"):
        img = Image.open(f"data/raw/{run}/{filename}")
        score = capture.score(img)
        write(img, score)
