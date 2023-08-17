# Text File Organizer Script

This script organizes text files into sub-folders based on their language names.

## Usage

1. Download the text files from the provided link and place them in a directory named "files" in the same directory as the script.
2. Run the script using the command: python main.py

After running the script, the organized files will be found in a directory given or in "organized_files". Each language will have its own sub-folder containing the corresponding text files.

## Features

- Organizes text files into language-specific sub-folders.
- Automatically creates sub-folders as needed.
- Error handling for a more robust execution.

## Script Explanation

The script performs the following steps:

1. Creates the destination directory if it doesn't exist.
2. Iterates through all files in the source directory.
3. For each text file, extracts the language name and creates a sub-folder based on the language.
4. Moves the file to the appropriate sub-folder.

## Author

Mohannad Waleed 