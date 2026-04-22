from abc import ABC, abstractmethod


class IDispatcherLog(ABC):
    @abstractmethod
    def write_log(self, message: str): ...

    @abstractmethod
    def get_logs_text(self) -> str: ...
