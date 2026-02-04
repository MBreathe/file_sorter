import os
from vars import paths
from match_file import match_file


def main():
    """
    Sorting script that moves files from the Downloads folder to
    corresponding folders based on their extension.

    :return: None
    """

    # TODO: add CLI interactions
    # TODO: package and make it executable via terminal

    # Iterate through files in Downloads
    for file in os.listdir(paths["downloads"]):
        match_file(file)


if __name__ == "__main__":
    main()