from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
import game_window as gw


class Launcher(object):
    def __init__(self):
        self.ui = QUiLoader().load("./launcher.ui")
        self.ui.pushButton.clicked.connect(self.door)
        self.new_type = {
            "Yes": True,
            "No": False
        }[self.ui.buttonGroup.checkedButton().text()]

    def door(self):
        x_len = self.ui.spinBox.value()
        y_len = self.ui.spinBox_2.value()
        window_door = gw.Main(int(x_len), int(y_len), self.new_type)
        self.ui.close()


if __name__ == '__main__':
    Window = QApplication([])
    Launch_Self = Launcher()
    Launch_Self.ui.show()
    Window.exec_()
