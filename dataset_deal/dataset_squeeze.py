import os
import random
import shutil

def get_all_image_paths(root_dir):
    image_paths = []
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_paths.append(os.path.join(subdir, file))
    return image_paths

def create_squeezed_dataset(src_dir, dest_dir, percentage=0.1):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    total_files_copied = 0
    for subdir, _, files in os.walk(src_dir):
        image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
        if image_files:
            selected_files = random.sample(image_files, max(1, int(len(image_files) * percentage)))
            relative_path = os.path.relpath(subdir, src_dir)
            dest_subdir = os.path.join(dest_dir, relative_path)
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
            for file in selected_files:
                src_file_path = os.path.join(subdir, file)
                dest_file_path = os.path.join(dest_subdir, file)
                shutil.copy2(src_file_path, dest_file_path)
                total_files_copied += 1
                print(f"Copied {total_files_copied} files so far...")

    print(f"Total files copied: {total_files_copied}")

if __name__ == "__main__":
    src_dataset_path = '/hexp/data/genImage'
    dest_dataset_path = '/hexp/data/genImage_squeeze'
    create_squeezed_dataset(src_dataset_path, dest_dataset_path)