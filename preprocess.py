import os

# for run in os.listdir("data/raw"):
#     print(f"processing run {run}")
#     images = sorted(os.listdir(f"data/raw/{run}"), key=lambda x: int(x[:-4]))
#     print(images)

for i in range(31, 52):
    os.rename(f"data/raw/202310041908/{i:>3}.png", f"data/raw/202310041908/{i:0>3}.png")
