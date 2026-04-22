from datetime import datetime

from src.i_station_operations import IStationOperations
from src.i_dispatcher_log import IDispatcherLog
from src.abstract_train import AbstractTrain


class StationManager(IStationOperations, IDispatcherLog):
    def __init__(self):
        self.trains: list[AbstractTrain] = []
        self.logs: list[str] = []

    def _find_train(self, train_id: str) -> AbstractTrain | None:
        return next((t for t in self.trains if t.train_id == train_id), None)

    def add_train(self, train: AbstractTrain):
        self.trains.append(train)
        self.write_log(f"ДОБАВЛЕН РЕЙС: {train.get_train_info()}")

    def remove_train(self, train_id: str):
        train = self._find_train(train_id)
        if train:
            self.trains.remove(train)
            self.write_log(f"УДАЛЕН РЕЙС: Поезд №{train_id}")
        else:
            self.write_log(f"ОШИБКА: Поезд №{train_id} не найден.")

    def change_status(self, train_id: str, new_status: str):
        train = self._find_train(train_id)
        if train:
            old_status = train.status
            train.status = new_status
            self.write_log(f"СТАТУС: Поезд №{train_id} ({old_status} → {new_status})")

    def write_log(self, message: str):
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{timestamp}] {message}")

    def get_logs_text(self) -> str:
        return "\n".join(self.logs)
