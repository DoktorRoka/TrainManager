import sys
import traceback
from PyQt6.QtWidgets import QApplication
from src.dispatch_window import DispatchWindow

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("\n--- ПРОИЗОШЛА ОШИБКА ---")
    print(tb)
    print("------------------------\n")

sys.excepthook = excepthook

def main():
    app = QApplication(sys.argv)
    window = DispatchWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()