import os
from PIL import Image
import json

import capture


def validate(current_score: int, next_score: int) -> bool:
    return current_score < 4000 and current_score <= next_score


def write(path: str, score: int):
    if os.path.exists(path):
        print(f"skipping {path}")
        return

    with open(path, "w") as f:
        print(f"write {score} to {path}")
        f.write(str(score))


for run in os.listdir("data/raw"):
    print(f"processing run {run}")

    # reverse ordering, so we process from newest to oldest
    images = sorted(
        (s for s in os.listdir(f"data/raw/{run}") if s.endswith(".png")), reverse=True
    )

    if len(images) == 0:
        continue

    image = Image.open(f"data/raw/{run}/{images[0]}")
    current = capture.score(image)

    for i in range(0, len(images)):
        path = f"data/raw/{run}/{images[i][:-4]}"
        image = Image.open(f"{path}.png")

        next = current
        current = capture.score(image)

        if not validate(current, next):
            print(f"[ERROR] suspicious OCR result for data/raw/{run}/{images[0]}")

        write(f"{path}.txt", current)
