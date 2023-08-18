# Text File Organizer Script
This script organizes text files into sub-folders based on their language names.

Text files example:
- arabic-1.txt
- arabic-2.txt
- english-1.txt
- english-2.txt

language : english  
sequence : 2

## Usage

1. Run the script using the command: 
    ```bash
    python main.py
   ```
2. Enter the source directory for files you want to organize
    ```bash
   Enter source directory (default: files): ./samplefiles
   ```

3. Enter the destination directory for files you want to organize files into
     ```bash
   Enter destination directory (default: organized_files): ./sampleDestination
   ```
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