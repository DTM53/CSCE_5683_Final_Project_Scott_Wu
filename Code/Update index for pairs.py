import json
import os
import xml.etree.ElementTree as ET

def load_json_pairs(filename):
    """Load image pairs from a JSON file."""
    with open(filename, 'r') as file:
        pairs = json.load(file)
    return pairs

def load_index_data(image_path, base_path):
    """Dynamically load index data from an XML file based on image path."""
    directory = os.path.dirname(image_path)
    index_file_path = os.path.join(base_path, directory, 'index.xml')
    if os.path.exists(index_file_path):
        tree = ET.parse(index_file_path)
        root = tree.getroot()
        data = {child.tag: child.text for child in root.findall('.//tag_of_interest')}
        return data
    else:
        raise FileNotFoundError(f"No index file found at {index_file_path}")

def merge_data(pairs, base_path):
    """Merge image pairs with index data from XML files."""
    updated_pairs = []
    for pair in pairs:
        try:
            image1_info = load_index_data(pair[0], base_path)
            image2_info = load_index_data(pair[1], base_path)
            updated_pairs.append(pair + [image1_info, image2_info])
        except FileNotFoundError as e:
            print(f"Skipping pair due to error: {e}")
            continue
    return updated_pairs

def save_to_json(data, filename):
    """Save the updated data to a JSON file."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    json_pairs_path = 'C:/Users/FORMULA/OneDrive - University of Arkansas/Desktop/image_pairs.json'
    base_path = 'C:/Users/FORMULA/Data/images' 
    output_json_path = 'C:/Users/FORMULA/OneDrive - University of Arkansas/Desktop/updated_image_pairs.json'

    pairs = load_json_pairs(json_pairs_path)
    updated_pairs = merge_data(pairs, base_path)
    save_to_json(updated_pairs, output_json_path)

    print("Updated image pairs have been saved to:", output_json_path)

if __name__ == '__main__':
    main()
