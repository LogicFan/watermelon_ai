from torch.utils.data import Dataset
import torch
import cv2
import json
import os


class WatermelonDataset(Dataset):
    def __init__(self):
        self.root_dir = "data/processed"

    def __len__(self):
        return len(os.listdir(self.root_dir)) / 2

    def __getitem__(self, idx):
        img = cv2.imread(f"data/processed/{idx:0>5}.png")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        text = json.load(f"data/processed/{idx:0>5}.json")
        label = max(0, text["next"] - text["curr"])

        return img, label
