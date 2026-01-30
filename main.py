import os, shutil


def main():
    """
    This script moves files from the Downloads folder to the Pictures or Documents folder based on the file extension.
    :return:
    """
    # File extension list variables
    pictures_extensions: list = ["png", "jpg", "jpeg", "gif", "webp"]
    documents_extensions: list = ["txt", "pdf", "doc", "docx"]

    # Base path variables
    root : str = os.path.expanduser("~")
    downloads_path: str = root + "/Downloads/"
    pictures_path: str = root + "/Pictures/"
    documents_path: str = root + "/Documents/"

    # Iterate through files in Downloads
    for file in os.listdir(downloads_path):
        # Extract file extension
        extension: str = file.split(".")[-1]
        file_path: str = downloads_path + file

        # Move file based on extension
        if extension in pictures_extensions:
            print(f"Moving {file} to {pictures_path}")
            shutil.move(file_path, pictures_path)

        if extension in documents_extensions:
            print(f"Moving {file} to {documents_path}")
            shutil.move(file_path, documents_path)


if __name__ == "__main__":
    main()