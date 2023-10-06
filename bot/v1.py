from PIL import Image
import cv2
import torch
import numpy as np
from torchvision.models import mobilenet_v3_small

from . import core


class BotV1(core.BaseBot):
    def __init__(self) -> None:
        model = mobilenet_v3_small()
        model.classifier[3] = torch.nn.Linear(
            in_features=1024, out_features=1, bias=True
        )
        model.load_state_dict(torch.load("./model_20231005_184400_40"))
        self.model = model
        self.model.eval()

    def predicate(self, img: Image) -> float:
        img = np.array(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.transpose((2, 1, 0))
        img = img.astype(np.float32) / 255.0
        img = np.expand_dims(img, axis=0)
        img = torch.tensor(img)

        return self.model(img)[0].item()
