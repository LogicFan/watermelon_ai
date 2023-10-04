from PIL import Image
import random
from . import core


class NaiveBot(core.BaseBot):
    def predicate(self, img: Image) -> int:
        return random.randint(0, 100)
