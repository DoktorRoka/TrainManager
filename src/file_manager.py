import json
import os
from src.i_file_handler import IFileHandler
from src.passenger_train import PassengerTrain
from src.cargo_train import CargoTrain
from src.abstract_train import AbstractTrain


class FileManager(IFileHandler):
    def save_to_file(self, filename: str, data: list[AbstractTrain]):
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

        dict_data = [train.to_dict() for train in data]
        tmp_path = filename + ".tmp"
        with open(tmp_path, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, ensure_ascii=False, indent=4)
        os.replace(tmp_path, filename)

    def load_from_file(self, filename: str) -> list[AbstractTrain]:
        folder = os.path.dirname(filename)
        if folder and not os.path.exists(folder):
            os.makedirs(folder, exist_ok=True)

        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)
            return []

        with open(filename, 'r', encoding='utf-8') as f:
            try:
                dict_data = json.load(f)
            except json.JSONDecodeError:
                return []

        trains: list[AbstractTrain] = []
        for item in dict_data:
            train_type = item.get("type")
            try:
                if train_type == "Passenger":
                    train = PassengerTrain(
                        item["train_id"], item["route"], item["wagons_count"],
                        item.get("wagon_types", ""), item.get("services", "")
                    )
                    train.status = item.get("status", "Ожидает")
                    trains.append(train)
                elif train_type == "Cargo":
                    train = CargoTrain(
                        item["train_id"], item["route"], item["wagons_count"],
                        item.get("cargo_type", ""), item.get("cargo_weight", 0.0)
                    )
                    train.status = item.get("status", "Ожидает")
                    trains.append(train)
            except (KeyError, ValueError):
                continue

        return trains
