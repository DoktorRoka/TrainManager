from src.abstract_train import AbstractTrain

class PassengerTrain(AbstractTrain):
    def __init__(self, train_id: str, route: str, wagons_count: int, wagon_types: str, services: str):
        super().__init__(train_id, route, wagons_count)
        self.wagon_types = wagon_types
        self.services = services

    def get_train_info(self) -> str:
        return f"Пассажирский №{self.train_id} [{self.route}]. Вагонов: {self.wagons_count} ({self.wagon_types}). Сервис: {self.services}"

    def to_dict(self) -> dict:
        return {
            "type": "Passenger",
            "train_id": self.train_id,
            "route": self.route,
            "status": self.status,
            "wagons_count": self.wagons_count,
            "wagon_types": self.wagon_types,
            "services": self.services
        }