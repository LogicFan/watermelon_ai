from datetime import datetime
from PIL import Image
import time
import os

from screen import ScreenAnalyzer, GameOverException
from controller import Controller
import bot

# configuration
iteration = 10
estimator = bot.v1.BotV1()


def run_one_turn():
    Controller.move_to_zero()
    optimizer = bot.core.Optimizer()

    while True:
        frame = ScreenAnalyzer.get_screen()
        current_position = ScreenAnalyzer.recognize_drop_position(frame)
        prediction = estimator.predicate(ScreenAnalyzer.crop_playground(frame))
        print(
            f"[DEBUG] position {current_position} has estimated score {prediction:.2f}"
        )
        optimizer.put(current_position, prediction)

        if Controller.is_right_edge(current_position):
            # complete scan all possible drop position
            break

        Controller.click_right()
        time.sleep(0.1)

    optimal_position, best_score = optimizer.get_and_reset()
    print(f"[INFO]  pick {optimal_position} with the best score {best_score:.2f}")
    Controller.move_to_position(current_position, optimal_position)


if __name__ == "__main__":
    for _ in range(0, iteration):
        run = datetime.now().strftime("%Y%m%d%H%M")
        os.makedirs(f"data/raw/{run}")
        print(f"[INFO]  start {run}")

        turn = 0
        while True:
            try:
                print(f"[INFO]  turn {turn}")
                run_one_turn()
            except GameOverException:
                break

            screen = ScreenAnalyzer.get_screen()
            screen.save(f"data/raw/{run}/{turn:0>3}.png")
            Controller.click_confirm()
            time.sleep(5)

            turn += 1

        print(f"[INFO]  complete {run}")
        Controller.restart()
