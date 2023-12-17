# tests/test_os_detector.py
import unittest
import platform
from core.os_detector.os_detector import OSDetector


class TestOSDetector(unittest.TestCase):
    def setUp(self):
        self.detector = OSDetector()

    def test_detect_linux(self):
        if platform.system() == "Linux":
            self.assertEqual(self.detector.detect_os(), "Linux")

    def test_detect_windows(self):
        if platform.system() == "Windows":
            self.assertEqual(self.detector.detect_os(), "Windows")

    def test_detect_darwin(self):
        if platform.system() == "Darwin":
            self.assertEqual(self.detector.detect_os(), "Darwin")

    def test_detect_unknown(self):
        original_platform_system = platform.system
        platform.system = lambda: "UnknownOS"
        with self.assertRaises(ValueError):
            self.detector.detect_os()
        platform.system = original_platform_system


if __name__ == '__main__':
    unittest.main()
