import platform


class OSDetector:
    """
    Class for detecting the operating system.
    """

    def __init__(self):
        pass

    @staticmethod
    def detect_os():
        """
        Detects the current operating system and raises an exception if it cannot be determined.
        """
        try:
            os_name = platform.system()
            if os_name in ["Linux", "Windows", "Darwin"]:
                return os_name
            else:
                raise ValueError("Unsupported or unknown operating system.")
        except Exception as e:
            raise e
