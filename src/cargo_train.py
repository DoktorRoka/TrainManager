from src.abstract_train import AbstractTrain

class CargoTrain(AbstractTrain):
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