import json
import os
from src.interfaces import IStationOperations, IFileHandler, IDispatcherLog
from src.models import AbstractTrain, PassengerTrain, CargoTrain

class FileManager(IFileHandler):
    """Менеджер файлов который сохраняет и загружает файлы"""
    def save_to_file(self, filename: str, data: list):
        dict_data = [train.to_dict() for train in data]

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dict_data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename: str) -> list:
        # Создаем папку, если ее нет (чтобы не было ошибки FileNotFoundError)
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Если файла еще нет, создаем его пустым и возвращаем пустой список
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False)
            return []

        with open(filename, 'r', encoding='utf-8') as f:
            try:
                dict_data = json.load(f)
            except json.JSONDecodeError:
                return []  # Если файл пустой или поврежден

        # Восстанавливаем объекты из словарей
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

class StationManager(IStationOperations, IDispatcherLog):
    """Управление самой станцией"""

    def __init__(self):
        self.trains = []
        self.logs = []

    def add_train(self, train:AbstractTrain):
        self.trains.append(train)
        self.write_log(f"ДОБАВЛЕН РЕЙС: {train.get_train_info()}")

    def remove_train(self, train_id: str):
        for train in self.trains:
            if train.train_id == train_id:
                self.trains.remove(train)
                self.write_log(f"УДАЛЕН РЕЙС: Поезд №{train_id}")
                return
        self.write_log(f"ОШИБКА: Поезд №{train_id} не найден.")

    def change_status(self, train_id: str, new_status: str):
        """Дополнительный метод для смены статуса поезда (Отправлен/Прибыл и т.д.)"""
        for train in self.trains:
            if train.train_id == train_id:
                old_status = train.status
                train.status = new_status
                self.write_log(f"ИЗМЕНЕН СТАТУС: Поезд №{train_id} ({old_status} -> {new_status})")
                return

    def write_log(self, message: str):
        self.logs.append(message)
        print(f"[ДИСПЕТЧЕР]: {message}")  # отладка

    def get_logs_text(self) -> str:
        """Возвращает все логи одним текстом для вывода в графическом интерфейсе"""
        return "\n".join(self.logs)