from abc import ABC, abstractmethod


class IFileHandler(ABC):
    @abstractmethod
    def save_to_file(self, filename: str, data: list):
        pass

    @abstractmethod
    def load_from_file(self, filename: str) -> list:
        pass