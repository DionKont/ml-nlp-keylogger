# main.py
from core.os_detector.os_detector import OSDetector


def main():
    detector = OSDetector()
    os_type = detector.detect_os()
    print(f"The detected operating system is: {os_type}")


if __name__ == "__main__":
    main()
