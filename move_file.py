import shutil


def move_file(file: str, file_path: str, destination_path: str):
    print(f"Moving {file} to {destination_path}")
    shutil.move(file_path, destination_path)