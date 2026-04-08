from abc import ABC, abstractmethod


class IStationOperations(ABC):
    @abstractmethod
    def add_train(self, train):
        pass

    @abstractmethod
    def remove_train(self, train_id: str):
        pass