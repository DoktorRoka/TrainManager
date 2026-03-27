from abc import ABC, abstractmethod


class IFileHandler(ABC):
    """Интерфейс работы с файловой системой"""

    @abstractmethod
    def save_to_file(self, filename: str, data: list):
        pass

    @abstractmethod
    def load_from_file(self, filename: str) -> list:
        pass


class IStationOperations(ABC):
    """Интерфейс управления поездами на станции"""

    @abstractmethod
    def add_train(self, train):
        pass

    @abstractmethod
    def remove_train(self, train_id: str):
        pass


class IDispatcherLog(ABC):
    """Интерфейс лога действий диспетчера"""

    @abstractmethod
    def write_log(self, message: str):
        pass
