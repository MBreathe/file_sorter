import os


# File extension list variables
# TODO: add more file extensions
pictures_extensions: list = ["png", "jpg", "jpeg", "gif", "webp"]
documents_extensions: list = ["txt", "pdf", "doc", "docx"]
music_extensions: list = ["mp3", "wav", "flac"]
public_extensions: list = ["html", "css", "js"]
video_extensions: list = ["mp4", "mkv", "avi"]

extensions: dict[str, list] = {
    "pictures": pictures_extensions,
    "documents": documents_extensions,
    "music": music_extensions,
    "public": public_extensions,
    "video": video_extensions
}

# Base path variables
root : str = os.path.expanduser("~")
downloads_path: str = root + "/Downloads/"
pictures_path: str = root + "/Pictures/"
documents_path: str = root + "/Documents/"
music_path: str = root + "/Music/"
public_path: str = root + "/Public/"
video_path: str = root + "/Videos/"

paths: dict[str, str] = {
    "root": root,
    "downloads": downloads_path,
    "pictures": pictures_path,
    "documents": documents_path,
    "music": music_path,
    "public": public_path,
    "video": video_path
}