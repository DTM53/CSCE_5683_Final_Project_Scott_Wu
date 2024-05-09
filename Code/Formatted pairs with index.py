import json

def load_image_pairs(filename):
    """Load image pairs from a JSON file."""
    with open(filename, 'r') as file:
        pairs = json.load(file)
    return pairs

def format_pairs_with_index(pairs, index_data):
    """Format each pair with the given index data."""
    formatted_lines = []
    for pair in pairs:
        line = f"{pair[0]} {pair[1]} {index_data}"
        formatted_lines.append(line)
    return formatted_lines

def save_formatted_pairs(formatted_lines, output_filename):
    """Save the formatted lines to a file."""
    with open(output_filename, 'w') as file:
        for line in formatted_lines:
            file.write(line + '\n')

def main():
    json_pairs_path = 'C:/Users/FORMULA/OneDrive - University of Arkansas/Desktop/image_pairs.json'  # Path to your JSON file
    output_path = 'C:/Users/FORMULA/OneDrive - University of Arkansas/Desktop/formatted_pairs.txt'  # Output file path

    # Index data that will be added to each line
    index_data = "0 0 1165.37 0. 650.862 0. 1166.11 488.595 0. 0. 1. 1165.37 0. 650.862 0. 1166.11 488.595 0. 0. 1. 0.15102 0.52115 -0.84 1.95984 -0.41332 0.80519 0.42525 -1.02578 0.89798 0.28297 0.337 1.24882 0. 0. 0. 1."

    # Load pairs
    pairs = load_image_pairs(json_pairs_path)

    # Format each pair with the index data
    formatted_lines = format_pairs_with_index(pairs, index_data)

    # Save the formatted pairs to a file
    save_formatted_pairs(formatted_lines, output_path)
    print(f"Formatted pairs have been saved to {output_path}")

if __name__ == '__main__':
    main()
