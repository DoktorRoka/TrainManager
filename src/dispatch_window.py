import os
import sys
from datetime import datetime

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

from src.design import Ui_MainWindow
from src.station_manager import StationManager
from src.file_manager import FileManager
from src.passenger_train import PassengerTrain
from src.cargo_train import CargoTrain


STATUS_COLORS = {
    "Ожидает": "#d4920a",
    "Отправлен": "#1a9a5a",
    "В пути": "#1a7abf",
    "Прибыл": "#158a4a",
    "Задерживается": "#d03030",
}


class DispatchWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.station = StationManager()
        self.file_manager = FileManager()

        if hasattr(sys, 'frozen') or hasattr(sys, '__compiled__'):
            self.base_dir = os.path.dirname(os.path.abspath(sys.executable))
        else:
            self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        self.data_file_path = os.path.join(self.base_dir, 'data', 'trains.json')

        self._connect_signals()
        self._setup_table()
        self.toggle_fields()
        self.load_data(silent=True)

    def _connect_signals(self):
        self.btn_refresh.clicked.connect(self.update_table)
        self.btn_delete.clicked.connect(self.delete_train)
        self.btn_add.clicked.connect(self.add_train)
        self.btn_change_status.clicked.connect(self.change_status)
        self.btn_save.clicked.connect(lambda: self.save_data(silent=False))
        self.btn_load.clicked.connect(lambda: self.load_data(silent=False))
        self.combo_type.currentTextChanged.connect(self.toggle_fields)

    def _setup_table(self):
        header = self.table_trains.horizontalHeader()
        for col in range(self.table_trains.columnCount()):
            header.setSectionResizeMode(col, header.ResizeMode.ResizeToContents)
        self.table_trains.setEditTriggers(
            self.table_trains.EditTrigger.NoEditTriggers
        )

    def toggle_fields(self):
        is_passenger = self.combo_type.currentText() == "Пассажирский"

        self.input_services.setEnabled(is_passenger)
        self.input_wagon_types.setEnabled(is_passenger)
        self.input_cargo_type.setEnabled(not is_passenger)
        self.input_cargo_weight.setEnabled(not is_passenger)

        if is_passenger:
            self.input_cargo_type.clear()
            self.input_cargo_weight.clear()
        else:
            self.input_services.clear()
            self.input_wagon_types.clear()

    def _make_item(self, text: str, color: str | None = None) -> QTableWidgetItem:
        item = QTableWidgetItem(text)
        if color:
            item.setForeground(Qt.GlobalColor.white)
            item.setBackground(Qt.GlobalColor(color))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        return item

    def _make_status_item(self, status: str) -> QTableWidgetItem:
        hex_color = STATUS_COLORS.get(status, "#667085")
        item = QTableWidgetItem(status)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        from PyQt6.QtGui import QColor
        item.setForeground(QColor(hex_color))
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        return item

    def update_statistics(self):
        total = len(self.station.trains)
        passenger_count = sum(1 for t in self.station.trains if isinstance(t, PassengerTrain))
        cargo_count = sum(1 for t in self.station.trains if isinstance(t, CargoTrain))
        delayed = sum(1 for t in self.station.trains if t.status == "Задерживается")
        in_transit = sum(1 for t in self.station.trains if t.status == "В пути")
        arrived = sum(1 for t in self.station.trains if t.status == "Прибыл")

        self.label_stats.setText(
            f"<table cellpadding='5' style='font-size:14px; color:#0d3b66;'>"
            f"<tr><td><b>Всего рейсов:</b></td><td>{total}</td></tr>"
            f"<tr><td>Пассажирских:</td><td>{passenger_count}</td></tr>"
            f"<tr><td>Грузовых:</td><td>{cargo_count}</td></tr>"
            f"<tr><td>В пути:</td><td style='color:#1a7abf;'>{in_transit}</td></tr>"
            f"<tr><td>Прибыло:</td><td style='color:#158a4a;'>{arrived}</td></tr>"
            f"<tr><td>Задерживается:</td><td style='color:#d03030;'><b>{delayed}</b></td></tr>"
            f"</table>"
        )

    def update_table(self):
        self.table_trains.setRowCount(0)
        self.combo_trains.clear()

        for row, train in enumerate(self.station.trains):
            self.table_trains.insertRow(row)

            self.table_trains.setItem(row, 0, self._make_item(train.train_id))
            self.table_trains.setItem(row, 2, self._make_item(train.route))
            self.table_trains.setItem(row, 3, self._make_item(str(train.wagons_count)))
            self.table_trains.setItem(row, 8, self._make_status_item(train.status))

            if isinstance(train, PassengerTrain):
                self.table_trains.setItem(row, 1, self._make_item("Пассажирский"))
                self.table_trains.setItem(row, 4, self._make_item(train.wagon_types or "—"))
                self.table_trains.setItem(row, 5, self._make_item(train.services or "—"))
                self.table_trains.setItem(row, 6, self._make_item("—"))
                self.table_trains.setItem(row, 7, self._make_item("—"))
            else:
                self.table_trains.setItem(row, 1, self._make_item("Грузовой"))
                self.table_trains.setItem(row, 4, self._make_item("—"))
                self.table_trains.setItem(row, 5, self._make_item("—"))
                self.table_trains.setItem(row, 6, self._make_item(train.cargo_type or "—"))
                self.table_trains.setItem(row, 7, self._make_item(str(train.cargo_weight)))

            self.combo_trains.addItem(train.train_id)

        self.table_trains.resizeColumnsToContents()
        self.update_statistics()
        self.update_logs()

    def add_train(self):
        t_id = self.input_train_id.text().strip()
        route = self.input_route.text().strip()
        wagons = self.input_wagons.text().strip()
        t_type = self.combo_type.currentText()

        if not t_id or not route or not wagons:
            QMessageBox.warning(self, "Ошибка", "Заполните обязательные поля: Номер, Маршрут, Вагоны!")
            return

        if any(t.train_id == t_id for t in self.station.trains):
            QMessageBox.warning(self, "Ошибка", f"Поезд с номером «{t_id}» уже существует!")
            return

        try:
            wagons_count = int(wagons)
            if wagons_count <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Количество вагонов должно быть положительным целым числом!")
            return

        try:
            if t_type == "Пассажирский":
                w_types = self.input_wagon_types.text().strip()
                servs = self.input_services.text().strip()
                train = PassengerTrain(t_id, route, wagons_count, w_types, servs)
            else:
                c_type = self.input_cargo_type.text().strip()
                c_weight_text = self.input_cargo_weight.text().strip()
                if not c_type or not c_weight_text:
                    QMessageBox.warning(self, "Ошибка", "Заполните поля грузового поезда: Тип груза, Вес!")
                    return
                c_weight = float(c_weight_text)
                if c_weight <= 0:
                    raise ValueError
                train = CargoTrain(t_id, route, wagons_count, c_type, c_weight)

            self.station.add_train(train)

            self.input_train_id.clear()
            self.input_route.clear()
            self.input_wagons.clear()
            self.toggle_fields()

            self.update_table()
            self.save_data(silent=True)
            QMessageBox.information(self, "Успех", f"Рейс №{t_id} успешно добавлен!")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Вес груза должен быть положительным числом!")

    def delete_train(self):
        selected_row = self.table_trains.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите поезд в таблице для удаления!")
            return

        train_id = self.table_trains.item(selected_row, 0).text()
        reply = QMessageBox.question(
            self, "Подтверждение",
            f"Удалить поезд №{train_id}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )
        if reply != QMessageBox.StandardButton.Yes:
            return

        self.station.remove_train(train_id)
        self.update_table()
        self.save_data(silent=True)

    def change_status(self):
        train_id = self.combo_trains.currentText()
        new_status = self.combo_status.currentText()
        if not train_id:
            QMessageBox.warning(self, "Ошибка", "Нет поездов для смены статуса!")
            return
        self.station.change_status(train_id, new_status)
        self.update_table()
        self.save_data(silent=True)
        QMessageBox.information(self, "Успех", f"Статус поезда №{train_id} → «{new_status}»")

    def save_data(self, silent=False):
        try:
            self.file_manager.save_to_file(self.data_file_path, self.station.trains)
            msg = "Автосохранение данных." if silent else "Данные сохранены вручную."
            self.station.write_log(msg)
            if not silent:
                QMessageBox.information(self, "Сохранение", "Данные успешно сохранены!")
        except OSError as e:
            QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл:\n{e}")
        self.update_logs()

    def update_logs(self):
        self.text_logs.setPlainText(self.station.get_logs_text())
        scrollbar = self.text_logs.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())

    def load_data(self, silent=False):
        try:
            self.station.trains = self.file_manager.load_from_file(self.data_file_path)
            msg = "Данные загружены при старте." if silent else "Данные загружены вручную."
            self.station.write_log(msg)
            self.update_table()
            if not silent:
                QMessageBox.information(self, "Загрузка", "Данные успешно загружены!")
        except Exception as e:
            if not silent:
                QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить файл:\n{e}")
