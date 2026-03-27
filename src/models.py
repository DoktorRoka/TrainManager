from abc import ABC, abstractmethod

class AbstractTrain(ABC):
    """Абстрактный класс поезда"""
    def __init__(self, train_id: str, destination: str):
        self.train_id = train_id
        self.destination = destination
        self.status = "Ожидает"  # статус который будет по умолчанию

    @abstractmethod
    def get_train_info(self) -> str:
        """Абстрактный метод получения информации о поезде"""
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """Абстрактный метод для подготовки данных к сохранению в файл"""
        pass


class PassengerTrain(AbstractTrain):
    """Класс 1: Пассажирский поезд"""
    def __init__(self, train_id: str, destination: str, passengers_count: int):
        super().__init__(train_id, destination)
        self.passengers_count = passengers_count

    def get_train_info(self) -> str:
        return f"Пассажирский №{self.train_id} -> {self.destination} (Пасс: {self.passengers_count}, Статус: {self.status})"

    def to_dict(self) -> dict:
        return {
            "type": "Passenger",
            "train_id": self.train_id,
            "destination": self.destination,
            "status": self.status,
            "passengers_count": self.passengers_count
        }


class CargoTrain(AbstractTrain):
    """Класс 2: Грузовой поезд"""
    def __init__(self, train_id: str, destination: str, cargo_weight: float):
        super().__init__(train_id, destination)
        self.cargo_weight = cargo_weight

    def get_train_info(self) -> str:
        return f"Грузовой №{self.train_id} -> {self.destination} (Груз: {self.cargo_weight}т, Статус: {self.status})"

    def to_dict(self) -> dict:
        return {
            "type": "Cargo",
            "train_id": self.train_id,
            "destination": self.destination,
            "status": self.status,
            "cargo_weight": self.cargo_weight
        }