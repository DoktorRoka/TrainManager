from abc import ABC, abstractmethod

class AbstractTrain(ABC):
    def __init__(self, train_id: str, destination: str):
        self.train_id = train_id
        self.destination = destination
        self.status = "Ожидает"

    @abstractmethod
    def get_train_info(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass