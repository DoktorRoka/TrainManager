import sys
import os
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from src.design import Ui_MainWindow
from src.station_manager import StationManager
from src.file_manager import FileManager
from src.passenger_train import PassengerTrain
from src.cargo_train import CargoTrain


class DispatchWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.station = StationManager()
        self.file_manager = FileManager()

        if hasattr(sys, 'frozen') or hasattr(sys, '__compiled__'):
            base_dir = os.path.dirname(os.path.abspath(sys.executable))
        else:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        self.data_file_path = os.path.join(base_dir, 'data', 'trains.json')

        # Привязка кнопок
        self.btn_refresh.clicked.connect(self.update_table)
        self.btn_delete.clicked.connect(self.delete_train)
        self.btn_add.clicked.connect(self.add_train)
        self.btn_change_status.clicked.connect(self.change_status)
        self.btn_save.clicked.connect(lambda: self.save_data(silent=False))
        self.btn_load.clicked.connect(lambda: self.load_data(silent=False))

        # Привязка переключателя типа поезда (ДИНАМИЧЕСКИЙ ИНТЕРФЕЙС)
        self.combo_type.currentTextChanged.connect(self.toggle_fields)
        self.toggle_fields()  # Вызываем один раз при старте, чтобы настроить поля

        self.load_data(silent=True)

    def toggle_fields(self):
        """Включает и выключает поля ввода в зависимости от типа поезда"""
        is_passenger = (self.combo_type.currentText() == "Пассажирский")

        # Поля пассажирского
        self.input_services.setEnabled(is_passenger)
        self.input_wagon_types.setEnabled(is_passenger)

        # Поля грузового
        self.input_cargo_type.setEnabled(not is_passenger)
        self.input_cargo_weight.setEnabled(not is_passenger)

        # Очищаем неактивные поля для красоты
        if is_passenger:
            self.input_cargo_type.clear()
            self.input_cargo_weight.clear()
        else:
            self.input_services.clear()
            self.input_wagon_types.clear()

    def update_table(self):
        # Очищаем только строки, заголовки остаются те, что из Qt Designer
        self.table_trains.setRowCount(0)
        self.combo_trains.clear()

        for row, train in enumerate(self.station.trains):
            self.table_trains.insertRow(row)

            # Общие поля
            self.table_trains.setItem(row, 0, QTableWidgetItem(train.train_id))
            self.table_trains.setItem(row, 2, QTableWidgetItem(train.route))
            self.table_trains.setItem(row, 3, QTableWidgetItem(str(train.wagons_count)))
            self.table_trains.setItem(row, 8, QTableWidgetItem(train.status))

            # Специфичные поля в зависимости от типа
            if isinstance(train, PassengerTrain):
                self.table_trains.setItem(row, 1, QTableWidgetItem("Пассажирский"))
                self.table_trains.setItem(row, 4, QTableWidgetItem(train.wagon_types))
                self.table_trains.setItem(row, 5, QTableWidgetItem(train.services))
                self.table_trains.setItem(row, 6, QTableWidgetItem("-"))  # Прочерк для груза
                self.table_trains.setItem(row, 7, QTableWidgetItem("-"))
            else:
                self.table_trains.setItem(row, 1, QTableWidgetItem("Грузовой"))
                self.table_trains.setItem(row, 4, QTableWidgetItem("-"))  # Прочерк для пассажиров
                self.table_trains.setItem(row, 5, QTableWidgetItem("-"))
                self.table_trains.setItem(row, 6, QTableWidgetItem(train.cargo_type))
                self.table_trains.setItem(row, 7, QTableWidgetItem(str(train.cargo_weight)))

            self.combo_trains.addItem(train.train_id)

        self.table_trains.resizeColumnsToContents()

        self.update_logs()

    def add_train(self):
        t_id = self.input_train_id.text()
        route = self.input_route.text()
        wagons = self.input_wagons.text()
        t_type = self.combo_type.currentText()

        if not t_id or not route or not wagons:
            QMessageBox.warning(self, "Ошибка", "Заполните общие поля (Номер, Маршрут, Вагоны)!")
            return

        try:
            wagons_count = int(wagons)

            if t_type == "Пассажирский":
                w_types = self.input_wagon_types.text()
                servs = self.input_services.text()
                train = PassengerTrain(t_id, route, wagons_count, w_types, servs)
            else:
                c_type = self.input_cargo_type.text()
                c_weight = float(self.input_cargo_weight.text())
                train = CargoTrain(t_id, route, wagons_count, c_type, c_weight)

            self.station.add_train(train)

            # Очистка полей
            self.input_train_id.clear()
            self.input_route.clear()
            self.input_wagons.clear()
            self.toggle_fields()  # Сбросит остальные поля

            self.update_table()
            self.save_data(silent=True)
            QMessageBox.information(self, "Успех", "Рейс успешно добавлен!")
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Количество вагонов и вес груза должны быть числами!")

    def delete_train(self):
        selected_row = self.table_trains.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите поезд в таблице для удаления!")
            return

        train_id = self.table_trains.item(selected_row, 0).text()
        self.station.remove_train(train_id)
        self.update_table()
        self.save_data(silent=True)

    def change_status(self):
        train_id = self.combo_trains.currentText()
        new_status = self.combo_status.currentText()
        if not train_id: return
        self.station.change_status(train_id, new_status)
        self.update_table()
        self.save_data(silent=True)
        QMessageBox.information(self, "Успех", f"Статус поезда {train_id} изменен на '{new_status}'")

    def save_data(self, silent=False):
        self.file_manager.save_to_file(self.data_file_path, self.station.trains)
        self.station.write_log("Автосохранение данных." if silent else "Данные сохранены вручную.")
        self.update_logs()

    def load_data(self, silent=False):
        self.station.trains = self.file_manager.load_from_file(self.data_file_path)
        self.station.write_log("Данные загружены при старте." if silent else "Данные загружены вручную.")
        self.update_table()

    def update_logs(self):
        self.text_logs.setPlainText(self.station.get_logs_text())
        scrollbar = self.text_logs.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())