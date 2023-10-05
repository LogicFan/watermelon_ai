import os
from PIL import Image
import json

import capture

count = 0


def write(img: Image, final, next, curr):
    global count
    capture.playground(img).save(f"data/processed/{count:0>5}.png")
    with open(f"data/processed/{count:0>5}.json", "w") as f:
        json.dump({"final": final, "next": next, "curr": curr}, f)
    count += 1


os.makedirs("data/processed/", exist_ok=True)

for run in os.listdir("data/raw"):
    print(f"processing run {run}")
    filename = sorted(os.listdir(f"data/raw/{run}"), reverse=True)

    if len(filename) == 0:
        continue

    img = Image.open(f"data/raw/{run}/{filename[0]}")

    final = capture.score(img)
    next = final
    curr = final

    if final > 4000:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(f"[ERROR] incorrect OCR data for the last file of {run}")
        continue

    write(img, final, next, curr)

    for i in range(1, len(filename)):
        img = Image.open(f"data/raw/{run}/{filename[i]}")
        next = curr
        curr = capture.score(img)
        if curr > final:
            print(f"[WARN]  incorrect OCR data for data/raw/{run}/{filename[i]}")
            curr = next
            continue
        write(img, final, next, curr)
