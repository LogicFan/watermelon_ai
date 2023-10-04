from datetime import datetime
from PIL import Image
import time

import capture
import controller
import bot

# configuration
iteration = 10
estimator = bot.naive.NaiveBot()


def run_turn():
    controller.zero()

    optimizer = bot.core.Optimizer()

    while True:
        frame = capture.screen_image()
        position = capture.drop_position(frame)
        prediction = estimator.predicate(capture.playground(frame))
        optimizer.put(position, prediction)

        if position == controller.MAX_POSITION:
            break

        controller.right()
        time.sleep(0.1)

    best = optimizer.get()
    frame = capture.screen_image()
    controller.move(best, frame)
    controller.drop()


if __name__ == "__main__":
    for _ in range(0, iteration):
        run = datetime.now().strftime("%Y%m%d%H%M")

        turn = 0
        screen = capture.screen_image()
        while screen is not None:
            screen.save(f"data/{run}/raw/{turn>3}.png")
            run_turn()

            screen = capture.screen_image()
        # conclude iteration
        exit()
