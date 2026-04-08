from abc import ABC, abstractmethod

class IDispatcherLog(ABC):
    @abstractmethod
    def write_log(self, message: str):
        pass