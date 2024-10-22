import os
import pandas as pd

def find_deepest_paths(root_dir):
    deepest_paths = []
    max_depth = 0

    for dirpath, _, filenames in os.walk(root_dir):
        depth = dirpath.count(os.sep)
        if depth > max_depth:
            max_depth = depth
            deepest_paths = [dirpath]
        elif depth == max_depth:
            deepest_paths.append(dirpath)

    return deepest_paths

def count_images_in_paths(paths):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.JPG', '.JPEG', '.PNG', '.GIF', '.BMP', '.TIFF'}
    counts = []

    for path in paths:
        count = sum(1 for f in os.listdir(path) if os.path.splitext(f)[1].lower() in image_extensions)
        counts.append((path, count))

    return counts

def main():
    root_dir = '/hexp/data/genImage'
    deepest_paths = find_deepest_paths(root_dir)
    image_counts = count_images_in_paths(deepest_paths)

    df = pd.DataFrame(image_counts, columns=['Path', 'Image Count'])
    print(df)

if __name__ == "__main__":
    main()