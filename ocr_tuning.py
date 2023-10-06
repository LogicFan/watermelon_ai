from PIL import Image
import cv2
import numpy
import os
from screen import ScreenAnalyzer

count = 0


os.makedirs("data/num-ground-truth/", exist_ok=True)


def write(img: Image, score: int):
    global count

    img.save(f"data/num-ground-truth/{count:0>5}.png")
    with open(f"data/num-ground-truth/{count:0>5}.gt.txt", "w") as f:
        f.write(str(score))

    count += 1


def read_score(path: str) -> int:
    with open(path) as f:
        return int(f.read())


for run in os.listdir("data/raw"):
    print(f"processing run {run}")

    # reverse ordering, so we process from newest to oldest
    images = sorted(
        (s for s in os.listdir(f"data/raw/{run}") if s.endswith(".png")), reverse=True
    )

    if len(images) == 0:
        continue

    for i in range(0, len(images)):
        path = f"data/raw/{run}/{images[i][:-4]}"
        image = Image.open(f"{path}.png")
        score = read_score(f"{path}.txt")

        write(ScreenAnalyzer.crop_score_image(image), score)
