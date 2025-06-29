import os
import numpy as np
from tqdm import tqdm

def convert_segmentation_to_detection(labels_dir):
    """
    Converts YOLO segmentation labels to detection labels.
    Handles line breaks correctly, without adding an empty line at the end of the file.

    Args:
        labels_dir (str): Path to the folder with label files (.txt).
    """
    label_files = [f for f in os.listdir(labels_dir) if f.endswith('.txt')]
    
    if not label_files:
        return

    converted_count = 0
    skipped_count = 0

    for filename in tqdm(label_files, desc="Processing files"):
        filepath = os.path.join(labels_dir, filename)
        
        with open(filepath, 'r') as f:
            lines = f.readlines()

        if not lines:
            continue

        output_lines = []
        needs_conversion = False

        for line in lines:
            clean_line = line.strip()
            if not clean_line:
                continue

            parts = clean_line.split()
            
            if len(parts) > 5:
                needs_conversion = True
                class_id = parts[0]
                
                seg_coords = np.array([float(p) for p in parts[1:]]).reshape(-1, 2)
                
                x_min = np.min(seg_coords[:, 0])
                y_min = np.min(seg_coords[:, 1])
                x_max = np.max(seg_coords[:, 0])
                y_max = np.max(seg_coords[:, 1])
                
                x_center = (x_min + x_max) / 2.0
                y_center = (y_min + y_max) / 2.0
                width = x_max - x_min
                height = y_max - y_min
                
                new_line_content = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
                output_lines.append(new_line_content)
            elif len(parts) == 5:
                output_lines.append(clean_line)

        if needs_conversion or len(output_lines) != len(lines):
            final_content = "\n".join(output_lines)
            
            with open(filepath, 'w') as f:
                f.write(final_content)
            converted_count += 1
        else:
            skipped_count += 1

if __name__ == '__main__':
    test_labels_path = 'labels/test'
    valid_labels_path = 'labels/valid'
    train_labels_path = 'labels/train'
    convert_segmentation_to_detection(test_labels_path)
    convert_segmentation_to_detection(valid_labels_path)
    convert_segmentation_to_detection(train_labels_path)
