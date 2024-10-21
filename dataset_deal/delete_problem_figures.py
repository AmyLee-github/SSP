import os

def delete_problem_figures(log_file_path):
    with open(log_file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            image_path = line.strip().split('\'')[1]
            if os.path.exists(image_path):
                os.remove(image_path)
                print(f"Deleted: {image_path}")
            else:
                print(f"File not found: {image_path}")

if __name__ == "__main__":
    log_file_path = '/hexp/data/genImage_filtered/error_log.txt'
    delete_problem_figures(log_file_path)