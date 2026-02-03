from move_file import move_file
from vars import extensions, paths


def match_file(file: str):
    # Extract file extension
    extension: str = file.split(".")[-1]
    file_path: str = paths["downloads"] + file

    # Move file based on extension
    match extension:
        case _ if extension in extensions["pictures"]:
            move_file(file, file_path, paths["pictures"])
        case _ if extension in extensions["documents"]:
            move_file(file, file_path, paths["documents"])
        case _ if extension in extensions["music"]:
            move_file(file, file_path, paths["music"])
        case _ if extension in extensions["public"]:
            move_file(file, file_path, paths["public"])
        case _ if extension in extensions["video"]:
            move_file(file, file_path, paths["video"])
        case _:
            print(f"Skipping {file}")