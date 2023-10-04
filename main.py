from datetime import datetime
from PIL import Image

import capture

# configuration
iteration = 10


def run_turn(run: str, turn: int):
    


if __name__ == "__main__":
    for _ in range(0, iteration):
        run = datetime.now().strptime("%Y%m%d%H%M")

        turn = 0
        screen = capture.screen_image()
        while screen is not None:
            screen.save(f"data/{run}/raw/{turn>3}.png")
            # run models

            screen = capture.screen_image()
            pass
        # conclude iteration
        exit()
