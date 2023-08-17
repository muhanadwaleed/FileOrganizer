from FileOrganizer import FileOrganizer

if __name__ == "__main__":
    source_directory = input("Enter source directory (default: files): ") or "files"
    destination_directory = input("Enter destination directory (default: organized_files): ") or "organized_files"

    organizer = FileOrganizer(source_directory, destination_directory)
    organizer.organize_files()
