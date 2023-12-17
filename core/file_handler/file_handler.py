import csv


class FileHandler:
    """
    Class to handle file operations for keylogging data.
    """

    def __init__(self, file_path):
        """
        Initializes the file handler with a specified file path.
        :param file_path: Path to the file where data will be written.
        """
        self.file_path = file_path
        self.file = None

    def open_file(self):
        """
        Opens the file for writing. Creates the file if it does not exist.
        """
        try:
            self.file = open(self.file_path, 'a', newline='')
        except IOError as e:
            print(f"Error opening file: {e}")
            raise

    def write_data(self, data):
        """
        Writes data to the file.
        :param data: Data to be written to the file.
        """
        if self.file is not None:
            try:
                writer = csv.writer(self.file)
                writer.writerow(data)
            except csv.Error as e:
                print(f"Error writing to file: {e}")
                raise

    def close_file(self):
        """
        Closes the file.
        """
        if self.file is not None:
            try:
                self.file.close()
            except IOError as e:
                print(f"Error closing file: {e}")
                raise
            finally:
                self.file = None
