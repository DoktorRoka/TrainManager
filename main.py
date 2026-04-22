import sys
import traceback
from PyQt6.QtWidgets import QApplication
from src.dispatch_window import DispatchWindow


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print(f"\n{'='*40}")
    print("НЕОБРАБОТАННОЕ ИСКЛЮЧЕНИЕ:")
    print(tb)
    print('='*40)


sys.excepthook = excepthook


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Менеджер ЖД")

    window = DispatchWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
