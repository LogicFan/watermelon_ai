from PIL import Image
import random


class BaseBot:
    def predicate(self, img: Image) -> int:
        raise NotImplementedError()


class Optimizer:
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.position = 0
        self.score = 0

    def put(self, position: int, score: int):
        if score > self.score:
            # we pick the better strategy
            self.score = score
            self.position = position
        elif score == self.score and bool(random.getrandbits(1)):
            # avoid bias towards position 0
            self.score = score
            self.position = position

    def get(self) -> int:
        return (self.position, self.score)

    def get_and_reset(self) -> (int, int):
        """
        return (position, score)
        """
        result = (self.position, self.score)
        # print(f"position {self.position} has the best score {self.score}")
        self.reset()
        return result
