from abc import ABC, abstractmethod

class AbstractTrain(ABC):
    def __init__(self, train_id: str, route: str, wagons_count: int):
        self.train_id = train_id
        self.route = route
        self.wagons_count = wagons_count
        self.status = "Ожидает"

    @abstractmethod
    def get_train_info(self) -> str:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass