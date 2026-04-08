from src.abstract_train import AbstractTrain

class PassengerTrain(AbstractTrain):
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