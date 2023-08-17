import os

class FileOrganizer:

    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def __move_text_file(self, filename):
        try:
            if filename.endswith(".txt"):
                language, sequence = filename.replace(".txt", "").split("-")

                # Create sub-folder and move file depends on file name
                sub_folder_path = os.path.join(self.destination_dir, language)
                if not os.path.exists(sub_folder_path):
                    os.makedirs(sub_folder_path)

                new_file_path = os.path.join(sub_folder_path, os.path.basename(filename))
                os.rename(os.path.join(self.source_dir, filename), new_file_path)
        except Exception as err:
            print(" __move_text_file An error occurred while moving file {filename} , error : {err}".format(
                filename=filename, err=err))

    def organize_files(self):
        try:
            # Create the destination directory if it doesn't exist
            if not os.path.exists(self.destination_dir):
                os.makedirs(self.destination_dir)

            all_files = os.listdir(self.source_dir)
            for filename in all_files:
                self.__move_text_file(filename)

            print("Files organized successfully!")
        except Exception as err:
            print("organize_files An error occurred:", str(err))


if __name__ == "__main__":
    source_directory = input("Enter source directory (default: files): ") or "files"
    destination_directory = input("Enter destination directory (default: organized_files): ") or "organized_files"

    organizer = FileOrganizer(source_directory, destination_directory)
    organizer.organize_files()
