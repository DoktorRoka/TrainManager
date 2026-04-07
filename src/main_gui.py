import os
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from src.design import Ui_MainWindow
from src.logic import StationManager, FileManager
from src.models import PassengerTrain, CargoTrain


class DispatchWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.station = StationManager()
        self.file_manager = FileManager()
        self.data_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'trains.json')

        # Привязка кнопок
        self.btn_refresh.clicked.connect(self.update_table)
        self.btn_delete.clicked.connect(self.delete_train)
        self.btn_add.clicked.connect(self.add_train)
        self.btn_change_status.clicked.connect(self.change_status)

        # Кнопки ручного сохранения/загрузки
        self.btn_save.clicked.connect(lambda: self.save_data(silent=False))
        self.btn_load.clicked.connect(lambda: self.load_data(silent=False))

        # === АВТОЗАГРУЗКА ПРИ ЗАПУСКЕ ===
        self.load_data(silent=True)

    def update_table(self):
        self.table_trains.setRowCount(0)
        self.combo_trains.clear()

        for row, train in enumerate(self.station.trains):
            self.table_trains.insertRow(row)
            self.table_trains.setItem(row, 0, QTableWidgetItem(train.train_id))

            train_type = "Пассажирский" if isinstance(train, PassengerTrain) else "Грузовой"
            self.table_trains.setItem(row, 1, QTableWidgetItem(train_type))
            self.table_trains.setItem(row, 2, QTableWidgetItem(train.destination))

            param = f"Пасс: {train.passengers_count}" if train_type == "Пассажирский" else f"Вес: {train.cargo_weight}т"
            self.table_trains.setItem(row, 3, QTableWidgetItem(param))
            self.table_trains.setItem(row, 4, QTableWidgetItem(train.status))

            self.combo_trains.addItem(train.train_id)

        self.update_logs()

    def add_train(self):
        t_id = self.input_train_id.text()
        dest = self.input_destination.text()
        param_str = self.input_param.text()
        t_type = self.combo_type.currentText()

        if not t_id or not dest or not param_str:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля!")
            return

        try:
            if t_type == "Пассажирский":
                train = PassengerTrain(t_id, dest, int(param_str))
            else:
                train = CargoTrain(t_id, dest, float(param_str))

            self.station.add_train(train)

            self.input_train_id.clear()
            self.input_destination.clear()
            self.input_param.clear()

            self.update_table()

            # === АВТОСОХРАНЕНИЕ ===
            self.save_data(silent=True)
            QMessageBox.information(self, "Успех", "Рейс успешно добавлен!")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Параметр (Пассажиры/Вес) должен быть числом!")

    def delete_train(self):
        selected_row = self.table_trains.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите поезд в таблице для удаления!")
            return

        train_id = self.table_trains.item(selected_row, 0).text()
        self.station.remove_train(train_id)
        self.update_table()

        # === АВТОСОХРАНЕНИЕ ===
        self.save_data(silent=True)

    def change_status(self):
        train_id = self.combo_trains.currentText()
        new_status = self.combo_status.currentText()

        if not train_id:
            QMessageBox.warning(self, "Ошибка", "Нет доступных поездов!")
            return

        self.station.change_status(train_id, new_status)
        self.update_table()

        # === АВТОСОХРАНЕНИЕ ===
        self.save_data(silent=True)
        QMessageBox.information(self, "Успех", f"Статус поезда {train_id} изменен на '{new_status}'")

    def save_data(self, silent=False):
        """Сохраняет данные. Если silent=True, не показывает всплывающее окно."""
        self.file_manager.save_to_file(self.data_file_path, self.station.trains)

        # Пишем в лог, было ли это автосохранение или ручное
        log_msg = "Автосохранение данных." if silent else "Данные успешно сохранены вручную."
        self.station.write_log(log_msg)
        self.update_logs()

        if not silent:
            QMessageBox.information(self, "Сохранение", "Данные сохранены в файл trains.json!")

    def load_data(self, silent=False):
        """Загружает данные. Если silent=True, не показывает всплывающее окно."""
        loaded_trains = self.file_manager.load_from_file(self.data_file_path)
        self.station.trains = loaded_trains

        log_msg = "Данные автоматически загружены при старте." if silent else "Данные загружены вручную."
        self.station.write_log(log_msg)
        self.update_table()

        if not silent:
            QMessageBox.information(self, "Загрузка", "Данные успешно загружены!")

    def update_logs(self):
        self.text_logs.setPlainText(self.station.get_logs_text())
        scrollbar = self.text_logs.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())