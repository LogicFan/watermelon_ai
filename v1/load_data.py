from torch.utils.data import Dataset
import torch
import cv2
import os
import numpy as np


class WatermelonDataset(Dataset):
    def __init__(self):
        self.root_dir = "data/processed"

    def __len__(self):
        return sum(1 for x in os.listdir(self.root_dir) if x.endswith(".png"))

    def __getitem__(self, idx):
        img = cv2.imread(f"data/processed/{idx:0>5}.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = img.transpose((2, 1, 0))
        img = img.astype(np.float32) / 255.0

        with open(f"data/processed/{idx:0>5}.label") as f:
            label = [float(f.read())]

        return torch.tensor(img), torch.tensor(label)
