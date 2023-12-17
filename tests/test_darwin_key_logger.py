# Import necessary testing modules
import unittest
from unittest.mock import patch

# Import the DarwinKeyLogger class to be tested
from core.key_capture.darwin_key_logger import DarwinKeyLogger


# Define the test class, inheriting from unittest.TestCase
class TestDarwinKeyLogger(unittest.TestCase):

    # Test the initialization of the DarwinKeyLogger
    @patch('core.key_capture.darwin_key_logger.FileHandler')
    def test_initialization(self, MockFileHandler):
        # Create a DarwinKeyLogger instance with a mock FileHandler
        keylogger = DarwinKeyLogger('test_keystrokes.csv')

        # Assert that the FileHandler was instantiated with the correct file path
        MockFileHandler.assert_called_with('test_keystrokes.csv')

        # Assert that the listener attribute is initialized as None
        self.assertIsNone(keylogger.listener)

    # Test the start_capture method of DarwinKeyLogger
    @patch('core.key_capture.darwin_key_logger.FileHandler')
    @patch('pynput.keyboard.Listener')
    def test_start_capture(self, MockListener, MockFileHandler):
        # Create mock instances for FileHandler and Listener
        mock_file_handler = MockFileHandler.return_value

        # Create a DarwinKeyLogger instance
        keylogger = DarwinKeyLogger('test_keystrokes.csv')

        # Call the start_capture method
        keylogger.start_capture()

        # Assert that open_file was called once in FileHandler
        mock_file_handler.open_file.assert_called_once()

        # Assert that Listener constructor was called correctly
        MockListener.assert_called_once_with(on_press=keylogger.on_press)

    # Test the stop_capture method of DarwinKeyLogger
    @patch('core.key_capture.darwin_key_logger.FileHandler')
    @patch('pynput.keyboard.Listener')
    def test_stop_capture(self, MockListener, MockFileHandler):
        # Create mock instances for FileHandler and Listener
        mock_listener_instance = MockListener.return_value
        mock_file_handler = MockFileHandler.return_value

        # Create a DarwinKeyLogger instance
        keylogger = DarwinKeyLogger('test_keystrokes.csv')

        # Start and then stop the keylogger
        keylogger.start_capture()
        keylogger.stop_capture()

        # Assert that close_file was called once in FileHandler
        mock_file_handler.close_file.assert_called_once()

        # Assert that stop was called once in the Listener instance
        mock_listener_instance.stop.assert_called_once()


# Standard boilerplate to run the test suite
if __name__ == '__main__':
    unittest.main()
