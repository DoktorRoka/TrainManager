from abc import ABC, abstractmethod


class AbstractTrain(ABC):
    def __init__(self, train_id: str, route: str, wagons_count: int):
        if wagons_count <= 0:
            raise ValueError("Количество вагонов должно быть положительным")
        self.train_id = train_id
        self.route = route
        self.wagons_count = wagons_count
        self.status = "Ожидает"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AbstractTrain):
            return NotImplemented
        return self.train_id == other.train_id

    def __hash__(self) -> int:
        return hash(self.train_id)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id={self.train_id!r}, route={self.route!r})"

    @abstractmethod
    def get_train_info(self) -> str: ...

    @abstractmethod
    def to_dict(self) -> dict: ...
