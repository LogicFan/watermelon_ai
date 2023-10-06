import os
from PIL import Image
from screen import ScreenAnalyzer

count = 0


def write_data(img: Image, label: int):
    global count
    ScreenAnalyzer.crop_playground(img).save(f"data/processed/{count:0>5}.png")
    with open(f"data/processed/{count:0>5}.label", "w") as f:
        f.write(str(label))

    count += 1


def read_score(path: str) -> int:
    with open(path) as f:
        return int(f.read())


os.makedirs("data/processed/", exist_ok=True)

for run in os.listdir("data/raw"):
    print(f"processing run {run}")

    # reverse ordering, so we process from newest to oldest
    images = sorted(
        (s for s in os.listdir(f"data/raw/{run}") if s.endswith(".png")), reverse=True
    )

    if len(images) == 0:
        continue

    path = f"data/raw/{run}/{images[0][:-4]}"
    image = Image.open(f"{path}.png")
    score = read_score(f"{path}.txt")

    for i in range(1, len(images)):
        path = f"data/raw/{run}/{images[i][:-4]}"

        next_score = score
        image = Image.open(f"data/raw/{run}/{images[i]}")
        score = read_score(f"{path}.txt")
        write_data(image, next_score - score)
