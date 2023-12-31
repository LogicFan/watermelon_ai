import os
from PIL import Image
import json

from screen import ScreenAnalyzer


def validate(current_score: int, next_score: int) -> bool:
    return current_score < 4000 and current_score <= next_score


def write_score(path: str, score: int):
    with open(path, "w") as f:
        print(f"write {score} to {path}")
        f.write(str(score))


def read_score(path: str) -> int:
    with open(path) as f:
        return int(f.read())


blacklist = [
    "202310041817",
    "202310041908",
    "202310050020",
    "202310050032",
    "202310050034",
    "202310050037",
    "202310050212",
    "202310050254",
    "202310050518",
    "202310050737",
    "202310050919",
    "202310051055",
]

for run in os.listdir("data/raw"):
    print(f"processing run {run}")
    if run in blacklist:
        print("skipping")
        continue

    # reverse ordering, so we process from newest to oldest
    images = sorted(
        (s for s in os.listdir(f"data/raw/{run}") if s.endswith(".png")), reverse=True
    )

    if len(images) == 0:
        continue

    image = Image.open(f"data/raw/{run}/{images[0]}")
    current = ScreenAnalyzer.recognize_score(image)

    for i in range(0, len(images)):
        path = f"data/raw/{run}/{images[i][:-4]}"
        image = Image.open(f"{path}.png")

        next = current
        if os.path.exists(f"{path}.txt"):
            current = read_score(f"{path}.txt")
            print(f"skipping {path} with score {current}")
            continue
        else:
            current = ScreenAnalyzer.recognize_score(image)

        if not validate(current, next):
            print(
                f"[ERROR] suspicious OCR result {current} for data/raw/{run}/{images[i]}"
            )
            raise Exception("human labeling required")

        write_score(f"{path}.txt", current)
