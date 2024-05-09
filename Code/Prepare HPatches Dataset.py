from torch.utils.data import Dataset, DataLoader
import os
import cv2
import numpy as np

class HPatches(Dataset):
    def __init__(self, directory, transform=None):
        self.directory = directory
        self.transform = transform
        self.pairs = self._load_pairs()

    def _load_pairs(self):
        pairs = []
        # Assume a simple structure: each subdir in the directory is a sequence
        for sequence in os.listdir(self.directory):
            sequence_path = os.path.join(self.directory, sequence)
            images = [os.path.join(sequence_path, img) for img in sorted(os.listdir(sequence_path)) if img.endswith('.ppm')]
            # Generate pairs: (Iref, I)
            for img in images[1:]:  # Assuming the first image is the reference
                pairs.append((images[0], img))
        return pairs

    def __len__(self):
        return len(self.pairs)

    def __getitem__(self, idx):
        img_path1, img_path2 = self.pairs[idx]
        img1 = cv2.imread(img_path1, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)
        if self.transform:
            img1 = self.transform(img1)
            img2 = self.transform(img2)
        return img1, img2

# Usage
dataset = HPatches('path_to_hpatches_dataset', transform=None)
dataloader = DataLoader(dataset, batch_size=8, shuffle=True)
