# File Sorting Linux

A simple Python script to automatically organize your `Downloads` folder by moving files to `Pictures` or `Documents` based on their file extensions.

## Features

- Scans the `~/Downloads` directory.
- Automatically moves image files to `~/Pictures`.
- Automatically moves document files to `~/Documents`.
- Supported image extensions: `png`, `jpg`, `jpeg`, `gif`, `webp`.
- Supported document extensions: `txt`, `pdf`, `doc`, `docx`.

## Requirements

- Python 3.x
- Linux environment (uses standard `~/Downloads`, `~/Pictures`, and `~/Documents` paths).

## Usage

1. Ensure you have Python installed.
2. Run the script:

   ```bash
   python main.py
   ```

The script will iterate through all files in your `Downloads` folder and move them to the respective directories if they match the supported extensions.

## How it works

The script uses the `os` and `shutil` modules to:
1. Identify the user's home directory.
2. List all files in `~/Downloads`.
3. Check the extension of each file.
4. Move the file to the target directory using `shutil.move`.
