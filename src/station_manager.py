from src.i_station_operations import IStationOperations
from src.i_dispatcher_log import IDispatcherLog
from src.abstract_train import AbstractTrain


class StationManager(IStationOperations, IDispatcherLog):
    def __init__(self):
        self.trains = []
        self.logs = []

    def add_train(self, train: AbstractTrain):
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
        for train in self.trains:
            if train.train_id == train_id:
                old_status = train.status
                train.status = new_status
                self.write_log(f"ИЗМЕНЕН СТАТУС: Поезд №{train_id} ({old_status} -> {new_status})")
                return

    def write_log(self, message: str):
        self.logs.append(message)

    def get_logs_text(self) -> str:
        return "\n".join(self.logs)