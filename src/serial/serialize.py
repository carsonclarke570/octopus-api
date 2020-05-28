from abc import ABC
from abc import abstractmethod

class Serializable(ABC):

    @abstractmethod
    def encode(self):
        pass

    @classmethod
    @abstractmethod
    def decode(cls, data):
        pass