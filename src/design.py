from PyQt6 import QtCore, QtGui, QtWidgets


FRUTIGER_AERO_STYLE = """
QMainWindow {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #e8f4fd, stop:0.5 #d0eafc, stop:1 #b8ddf7);
}

QWidget#centralwidget {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #e8f4fd, stop:0.5 #d0eafc, stop:1 #b8ddf7);
}

QTabWidget::pane {
    border: 1px solid rgba(255,255,255,120);
    border-radius: 10px;
    background: rgba(255,255,255,180);
    margin-top: -1px;
}

QTabBar::tab {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(255,255,255,200), stop:1 rgba(220,235,250,200));
    color: #1a5276;
    padding: 10px 28px;
    margin-right: 3px;
    border: 1px solid rgba(150,190,220,160);
    border-bottom: none;
    border-top-left-radius: 10px;
    border-top-right-radius: 10px;
    font-size: 13px;
    font-weight: bold;
    min-width: 130px;
}

QTabBar::tab:selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(255,255,255,240), stop:1 rgba(240,248,255,240));
    color: #0d3b66;
    border-color: rgba(100,170,230,180);
}

QTabBar::tab:hover:!selected {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(255,255,255,230), stop:1 rgba(230,242,252,230));
}

QGroupBox {
    font-size: 13px;
    font-weight: bold;
    color: #1a5276;
    border: 1px solid rgba(150,190,220,140);
    border-radius: 12px;
    margin-top: 18px;
    padding: 22px 14px 14px 14px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(255,255,255,210), stop:1 rgba(235,245,252,210));
}

QGroupBox::title {
    subcontrol-origin: margin;
    left: 18px;
    padding: 0 10px;
    color: #1a6baa;
}

QLineEdit {
    padding: 8px 14px;
    border: 1px solid rgba(120,180,220,180);
    border-radius: 8px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f5fafe);
    color: #1a3c5e;
    font-size: 13px;
    selection-background-color: #3ca0d6;
    selection-color: #ffffff;
}

QLineEdit:focus {
    border: 2px solid #3ca0d6;
    padding: 7px 13px;
    background: #ffffff;
}

QLineEdit:disabled {
    background: rgba(230,240,248,200);
    color: #9ab5c8;
    border-color: rgba(200,220,235,150);
}

QPushButton {
    padding: 9px 22px;
    border: 1px solid rgba(120,180,220,140);
    border-radius: 8px;
    font-size: 13px;
    font-weight: bold;
    min-height: 22px;
    color: #ffffff;
}

QPushButton#btn_add,
QPushButton#btn_change_status {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #5ec3f2, stop:0.4 #3ca8e0, stop:1 #2a8fc5);
    border: 1px solid rgba(30,120,180,180);
}

QPushButton#btn_add:hover,
QPushButton#btn_change_status:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #72d0ff, stop:0.4 #4cb5e8, stop:1 #359ed8);
}

QPushButton#btn_add:pressed,
QPushButton#btn_change_status:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #2a8fc5, stop:1 #1e7ab0);
}

QPushButton#btn_delete {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ff9a8b, stop:0.4 #f06565, stop:1 #d94545);
    border: 1px solid rgba(180,50,50,160);
}

QPushButton#btn_delete:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffb0a0, stop:0.4 #f58080, stop:1 #e05555);
}

QPushButton#btn_delete:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #c03030, stop:1 #a02525);
}

QPushButton#btn_refresh,
QPushButton#btn_save,
QPushButton#btn_load {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(255,255,255,230), stop:1 rgba(230,242,252,230));
    color: #1a5276;
    border: 1px solid rgba(120,180,220,140);
}

QPushButton#btn_refresh:hover,
QPushButton#btn_save:hover,
QPushButton#btn_load:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #eaf5fd);
}

QPushButton#btn_refresh:pressed,
QPushButton#btn_save:pressed,
QPushButton#btn_load:pressed {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #c8e0f0, stop:1 #b0d0e5);
}

QTableWidget {
    border: 1px solid rgba(150,190,220,140);
    border-radius: 10px;
    background: rgba(255,255,255,210);
    alternate-background-color: rgba(240,248,255,180);
    gridline-color: rgba(180,210,235,120);
    font-size: 13px;
    selection-background-color: rgba(60,168,224,80);
    selection-color: #0d3b66;
}

QTableWidget::item {
    padding: 6px 12px;
}

QTableWidget::item:selected {
    background: rgba(60,168,224,90);
}

QHeaderView::section {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(200,225,245,240), stop:1 rgba(180,210,235,240));
    color: #1a5276;
    font-size: 12px;
    font-weight: bold;
    padding: 8px 12px;
    border: none;
    border-bottom: 2px solid rgba(60,160,220,160);
    border-right: 1px solid rgba(200,225,245,120);
}

QHeaderView::section:first {
    border-top-left-radius: 10px;
}

QHeaderView::section:last {
    border-top-right-radius: 10px;
    border-right: none;
}

QComboBox {
    padding: 7px 14px;
    border: 1px solid rgba(120,180,220,160);
    border-radius: 8px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #ffffff, stop:1 #f0f8fe);
    color: #1a3c5e;
    font-size: 13px;
    min-height: 22px;
}

QComboBox:focus {
    border: 2px solid #3ca0d6;
}

QComboBox::drop-down {
    border: none;
    width: 28px;
}

QComboBox::down-arrow {
    image: none;
    border-left: 5px solid transparent;
    border-right: 5px solid transparent;
    border-top: 6px solid #3ca0d6;
}

QComboBox QAbstractItemView {
    border: 1px solid rgba(120,180,220,160);
    border-radius: 8px;
    background: rgba(255,255,255,240);
    selection-background-color: rgba(60,168,224,100);
    selection-color: #0d3b66;
    padding: 4px;
    outline: none;
}

QTextEdit {
    border: 1px solid rgba(120,180,220,140);
    border-radius: 10px;
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #0a1628, stop:1 #122640);
    color: #a0d8ef;
    font-family: 'Consolas', 'Segoe UI', monospace;
    font-size: 12px;
    padding: 12px;
    selection-background-color: #2a6fa8;
    selection-color: #e0f0ff;
}

QLabel {
    color: #1a5276;
    font-size: 12px;
}

QLabel#label_stats {
    font-size: 14px;
    color: #0d3b66;
}

QScrollBar:vertical {
    background: rgba(200,225,245,80);
    width: 12px;
    border-radius: 6px;
}

QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 rgba(120,190,235,180), stop:1 rgba(80,160,220,180));
    border-radius: 6px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
        stop:0 rgba(100,175,230,220), stop:1 rgba(60,145,210,220));
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar:horizontal {
    background: rgba(200,225,245,80);
    height: 12px;
    border-radius: 6px;
}

QScrollBar::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 rgba(120,190,235,180), stop:1 rgba(80,160,220,180));
    border-radius: 6px;
    min-width: 30px;
}

QScrollBar::add-line:horizontal,
QScrollBar::sub-line:horizontal {
    width: 0px;
}

QMessageBox {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #e8f4fd, stop:1 #d0eafc);
}

QMessageBox QLabel {
    color: #1a3c5e;
    font-size: 13px;
}

QMessageBox QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #5ec3f2, stop:0.4 #3ca8e0, stop:1 #2a8fc5);
    color: #ffffff;
    border: 1px solid rgba(30,120,180,180);
    border-radius: 6px;
    padding: 6px 18px;
    min-width: 80px;
}

QMessageBox QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        stop:0 #72d0ff, stop:0.4 #4cb5e8, stop:1 #359ed8);
}
"""


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 660)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet(FRUTIGER_AERO_STYLE)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(14, 14, 14, 14)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self._build_schedule_tab()
        self._build_management_tab()
        self._build_logs_tab()

        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _build_schedule_tab(self):
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        layout = QtWidgets.QVBoxLayout(self.tab)
        layout.setContentsMargins(10, 14, 10, 10)
        layout.setSpacing(12)

        self.table_trains = QtWidgets.QTableWidget(parent=self.tab)
        self.table_trains.setObjectName("table_trains")
        self.table_trains.setColumnCount(9)
        self.table_trains.setRowCount(0)
        self.table_trains.setAlternatingRowColors(True)
        self.table_trains.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_trains.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.table_trains.horizontalHeader().setStretchLastSection(True)
        self.table_trains.verticalHeader().setVisible(False)
        self.table_trains.setShowGrid(True)
        layout.addWidget(self.table_trains)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.setSpacing(12)
        self.btn_delete = QtWidgets.QPushButton(parent=self.tab)
        self.btn_delete.setObjectName("btn_delete")
        self.btn_refresh = QtWidgets.QPushButton(parent=self.tab)
        self.btn_refresh.setObjectName("btn_refresh")
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_refresh)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.tabWidget.addTab(self.tab, "")

    def _build_management_tab(self):
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        outer_layout = QtWidgets.QHBoxLayout(self.tab_3)
        outer_layout.setContentsMargins(10, 14, 10, 10)
        outer_layout.setSpacing(14)

        left_column = QtWidgets.QVBoxLayout()
        left_column.setSpacing(14)

        self._build_add_train_group(left_column)
        self._build_change_status_group(left_column)
        left_column.addStretch()

        outer_layout.addLayout(left_column, stretch=3)
        self._build_stats_group(outer_layout)

        self.tabWidget.addTab(self.tab_3, "")

    def _build_add_train_group(self, parent_layout):
        self.groupBox = QtWidgets.QGroupBox()
        self.groupBox.setObjectName("groupBox")
        form = QtWidgets.QFormLayout(self.groupBox)
        form.setContentsMargins(18, 26, 18, 18)
        form.setSpacing(14)
        form.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.input_train_id = QtWidgets.QLineEdit()
        self.input_train_id.setObjectName("input_train_id")
        self.input_train_id.setPlaceholderText("127А")
        form.addRow("Номер поезда:", self.input_train_id)

        self.input_route = QtWidgets.QLineEdit()
        self.input_route.setObjectName("input_route")
        self.input_route.setPlaceholderText("Москва — Санкт-Петербург")
        form.addRow("Маршрут:", self.input_route)

        self.input_wagons = QtWidgets.QLineEdit()
        self.input_wagons.setObjectName("input_wagons")
        self.input_wagons.setPlaceholderText("12")
        form.addRow("Кол-во вагонов:", self.input_wagons)

        self.combo_type = QtWidgets.QComboBox()
        self.combo_type.setObjectName("combo_type")
        self.combo_type.addItem("Пассажирский")
        self.combo_type.addItem("Грузовой")
        form.addRow("Тип поезда:", self.combo_type)

        self.input_wagon_types = QtWidgets.QLineEdit()
        self.input_wagon_types.setObjectName("input_wagon_types")
        self.input_wagon_types.setPlaceholderText("купе, плацкарт, СВ")
        form.addRow("Типы вагонов:", self.input_wagon_types)

        self.input_services = QtWidgets.QLineEdit()
        self.input_services.setObjectName("input_services")
        self.input_services.setPlaceholderText("ресторан, кондиционер, WiFi")
        form.addRow("Сервисы:", self.input_services)

        self.input_cargo_type = QtWidgets.QLineEdit()
        self.input_cargo_type.setObjectName("input_cargo_type")
        self.input_cargo_type.setPlaceholderText("уголь, лес, контейнеры")
        form.addRow("Тип груза:", self.input_cargo_type)

        self.input_cargo_weight = QtWidgets.QLineEdit()
        self.input_cargo_weight.setObjectName("input_cargo_weight")
        self.input_cargo_weight.setPlaceholderText("5000")
        form.addRow("Вес груза (т):", self.input_cargo_weight)

        self.btn_add = QtWidgets.QPushButton()
        self.btn_add.setObjectName("btn_add")
        self.btn_add.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        form.addRow(self.btn_add)

        parent_layout.addWidget(self.groupBox)

    def _build_change_status_group(self, parent_layout):
        self.groupBox_2 = QtWidgets.QGroupBox()
        self.groupBox_2.setObjectName("groupBox_2")
        form = QtWidgets.QFormLayout(self.groupBox_2)
        form.setContentsMargins(18, 26, 18, 18)
        form.setSpacing(14)
        form.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        self.combo_trains = QtWidgets.QComboBox()
        self.combo_trains.setObjectName("combo_trains")
        form.addRow("Поезд:", self.combo_trains)

        self.combo_status = QtWidgets.QComboBox()
        self.combo_status.setObjectName("combo_status")
        self.combo_status.addItem("Ожидает")
        self.combo_status.addItem("Отправлен")
        self.combo_status.addItem("В пути")
        self.combo_status.addItem("Прибыл")
        self.combo_status.addItem("Задерживается")
        form.addRow("Новый статус:", self.combo_status)

        self.btn_change_status = QtWidgets.QPushButton()
        self.btn_change_status.setObjectName("btn_change_status")
        self.btn_change_status.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        form.addRow(self.btn_change_status)

        parent_layout.addWidget(self.groupBox_2)

    def _build_stats_group(self, parent_layout):
        self.groupBox_3 = QtWidgets.QGroupBox()
        self.groupBox_3.setObjectName("groupBox_3")
        stats_layout = QtWidgets.QVBoxLayout(self.groupBox_3)
        stats_layout.setContentsMargins(18, 26, 18, 18)

        self.label_stats = QtWidgets.QLabel()
        self.label_stats.setObjectName("label_stats")
        self.label_stats.setWordWrap(True)
        self.label_stats.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft
        )
        stats_layout.addWidget(self.label_stats)
        stats_layout.addStretch()

        parent_layout.addWidget(self.groupBox_3, stretch=2)

    def _build_logs_tab(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        layout = QtWidgets.QVBoxLayout(self.tab_2)
        layout.setContentsMargins(10, 14, 10, 10)
        layout.setSpacing(12)

        self.text_logs = QtWidgets.QTextEdit(parent=self.tab_2)
        self.text_logs.setReadOnly(True)
        self.text_logs.setObjectName("text_logs")
        layout.addWidget(self.text_logs)

        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.setSpacing(12)
        self.btn_save = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        self.btn_load = QtWidgets.QPushButton(parent=self.tab_2)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.setCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        btn_layout.addWidget(self.btn_save)
        btn_layout.addWidget(self.btn_load)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        self.tabWidget.addTab(self.tab_2, "")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(
            _translate("MainWindow", "Менеджер ЖД — Диспетчерская")
        )

        headers = [
            "Номер", "Тип", "Маршрут", "Вагоны",
            "Типы вагонов", "Сервисы", "Тип груза", "Вес (т)", "Статус",
        ]
        for i, text in enumerate(headers):
            item = self.table_trains.horizontalHeaderItem(i)
            if item is None:
                self.table_trains.setHorizontalHeaderItem(
                    i, QtWidgets.QTableWidgetItem(text)
                )
            else:
                item.setText(text)

        self.btn_delete.setText("Удалить выбранный")
        self.btn_refresh.setText("Обновить таблицу")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab), "Расписание"
        )
        self.groupBox.setTitle("Добавление нового рейса")
        self.btn_add.setText("Добавить рейс")
        self.groupBox_2.setTitle("Смена статуса поезда")
        self.btn_change_status.setText("Изменить статус")
        self.groupBox_3.setTitle("Статистика станции")
        self.label_stats.setText("Нет данных")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_3), "Управление"
        )
        self.btn_save.setText("Сохранить данные в файл")
        self.btn_load.setText("Загрузить из файла")
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2), "Файлы и логи"
        )
