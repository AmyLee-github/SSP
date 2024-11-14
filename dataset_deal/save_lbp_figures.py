import os
import cv2
import numpy as np
from skimage.feature import local_binary_pattern

def process_lbp(image_path):
    print(f"Processing LBP for image: {image_path}")
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    radius = 1
    n_points = 8 * radius
    lbp = local_binary_pattern(image, n_points, radius, method='uniform')
    return lbp

def save_lbp_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                
                if not os.path.exists(output_path):
                    os.makedirs(output_path)
                    print(f"Created directory: {output_path}")
                
                output_file = os.path.join(output_path, file.replace('.', '_b.'))
                
                if os.path.exists(output_file):
                    print(f"Skipping already processed image: {output_file}")
                    continue
                
                lbp_image = process_lbp(input_path)
                cv2.imwrite(output_file, lbp_image)
                print(f"Saved LBP image to: {output_file}")

input_dir = '/hexp/data/genImage_examples'
output_dir = '/hexp/data/genImage_examples_lbp'
save_lbp_images(input_dir, output_dir)