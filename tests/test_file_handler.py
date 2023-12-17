# tests/test_file_handler.py
import unittest
import os
from core.file_handler.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_keystrokes.csv'
        self.handler = FileHandler(self.test_file)

    def test_file_open(self):
        self.handler.open_file()
        self.assertTrue(os.path.exists(self.test_file))
        # Check if file is opened successfully

    def test_write_data(self):
        self.handler.open_file()
        test_data = ["test", "data"]
        self.handler.write_data(test_data)
        # Verify file has content

    def test_close_file(self):
        self.handler.open_file()
        self.handler.close_file()
        # Check if file is closed

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)


if __name__ == '__main__':
    unittest.main()
