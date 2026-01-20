from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseSensor(ABC):
    """
    Base class for all sensors.
    """

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def read(self) -> Dict[str, Any]:
        """
        Read sensor values and return them as a dict.
        """
        raise NotImplementedError

    def health_check(self) -> bool:
        """
        Optional: override if sensor supports self-test.
        """
        return True
