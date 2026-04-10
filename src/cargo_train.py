from src.abstract_train import AbstractTrain

class CargoTrain(AbstractTrain):
    def __init__(self, train_id: str, route: str, wagons_count: int, cargo_type: str, cargo_weight: float):
        super().__init__(train_id, route, wagons_count)
        self.cargo_type = cargo_type
        self.cargo_weight = cargo_weight

    def get_train_info(self) -> str:
        return f"Грузовой №{self.train_id} [{self.route}]. Вагонов: {self.wagons_count}. Груз: {self.cargo_type} ({self.cargo_weight}т)"

    def to_dict(self) -> dict:
        return {
            "type": "Cargo",
            "train_id": self.train_id,
            "route": self.route,
            "status": self.status,
            "wagons_count": self.wagons_count,
            "cargo_type": self.cargo_type,
            "cargo_weight": self.cargo_weight
        }