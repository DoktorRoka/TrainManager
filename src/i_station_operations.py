from abc import ABC, abstractmethod
from src.abstract_train import AbstractTrain


class IStationOperations(ABC):
    @abstractmethod
    def add_train(self, train: AbstractTrain): ...

    @abstractmethod
    def remove_train(self, train_id: str): ...

    @abstractmethod
    def change_status(self, train_id: str, new_status: str): ...
