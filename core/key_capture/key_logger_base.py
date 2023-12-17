from abc import ABC, abstractmethod


class KeyLoggerBase(ABC):
    @abstractmethod
    def start_capture(self):
        """
        Start capturing keystrokes.
        """
        pass

    @abstractmethod
    def stop_capture(self):
        """
        Stop capturing keystrokes.
        """
        pass
