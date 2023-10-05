from datetime import datetime
from PIL import Image
import time
import os

import capture
import controller
import bot

# configuration
iteration = 10
estimator = bot.v1.BotV1()


def run_turn() -> bool:
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
    optimizer.reset()

    frame = capture.screen_image()
    controller.move(best, frame)
    return True


if __name__ == "__main__":
    for _ in range(0, iteration):
        run = datetime.now().strftime("%Y%m%d%H%M")
        os.makedirs(f"data/raw/{run}")

        turn = 0
        while True:
            try:
                run_turn()
            except capture.GameOverException:
                break

            screen = capture.screen_image()
            screen.save(f"data/raw/{run}/{turn:>3}.png")
            controller.confirm()
            time.sleep(5)

            turn += 1

        controller.restart()
