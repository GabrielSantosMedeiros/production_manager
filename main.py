from PySide6 import QtWidgets
import sys

WIDGET_WIDTH = 1000
WIDGET_HEIGHT = 600

class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainWidget()
    widget.resize(WIDGET_WIDTH, WIDGET_HEIGHT)
    widget.show()

    sys.exit(app.exec())