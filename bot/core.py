from PIL import Image


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
        # TODO FIX
        if score > self.score:
            self.score = score
            self.position = position

    def get(self) -> int:
        return self.position

    def get_and_reset(self) -> int:
        result = self.position
        print(f"position {self.position} has the best score {self.score}")
        self.reset()
        return result
