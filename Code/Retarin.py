import os
import cv2
from random import sample, seed
import json

def load_images_from_folder(base_folder):
    images = []
    print(f"Searching for images in the base folder: {base_folder}")
    for root, dirs, files in os.walk(base_folder):
        print(f"Entering directory: {root} with {len(files)} files")
        for filename in files:
            file_path = os.path.join(root, filename)
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img = cv2.imread(file_path)
                if img is not None:
                    images.append(file_path)
                    print(f"Loaded image: {file_path}")
                else:
                    print(f"Failed to load image at {file_path}. It may be corrupted or in an unsupported format.")
            else:
                print(f"Skipped non-image file: {file_path}")
    print(f"Total loaded images: {len(images)}")
    return images

def create_pairs(image_list):
    print("Creating image pairs...")
    if len(image_list) < 2:
        raise ValueError("Need at least two images to create a pair")
    seed(42)  # For reproducibility
    pairs = []
    pair_count = min(100, len(image_list) // 2)
    for _ in range(pair_count):
        pair = sample(image_list, 2)
        pairs.append((pair[0], pair[1]))
        print(f"Pair created: {pair[0]} and {pair[1]}")
    print(f"Created {len(pairs)} pairs.")
    return pairs

def save_pairs_to_json(pairs, filename):
    print(f"Saving pairs to JSON file: {filename}")
    with open(filename, 'w') as f:
        json.dump(pairs, f)
    print("Pairs saved successfully.")

# Example usage:
base_dir = 'D:/DATA/images'  # Adjust this path as needed
image_list = load_images_from_folder(base_dir)
if image_list:
    image_pairs = create_pairs(image_list)
    save_pairs_to_json(image_pairs, 'image_pairs.json')
else:
    print("No images to process.")
