import sys
from PyQt5.QtWidgets import QApplication

from logic import main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = main_window.MainWindow()
    main_window.show()
    sys.exit(app.exec_())
