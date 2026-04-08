import json
import os
from src.i_file_handler import IFileHandler
from src.passenger_train import PassengerTrain
from src.cargo_train import CargoTrain


class FileManager(IFileHandler):
    def save_to_file(self, filename: str, data: list):
        dict_data = [train.to_dict() for train in data]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename: str) -> list:
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

        trains = []
        for item in dict_data:
            if item["type"] == "Passenger":
                train = PassengerTrain(item["train_id"], item["destination"], item["passengers_count"])
                train.status = item["status"]
                trains.append(train)
            elif item["type"] == "Cargo":
                train = CargoTrain(item["train_id"], item["destination"], item["cargo_weight"])
                train.status = item["status"]
                trains.append(train)
        return trains