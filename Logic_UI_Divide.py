from MainWindow import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys


class ParentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


if __name__ == '__main__':

    # 这里写函数代名+1
    app = QApplication(sys.argv)
    MainWindow = ParentWindow()

    # btn_returnfrom_player_info.clicked.connect(ChildWindowPlayerInfo.close)
    # 显示
    MainWindow.show()
    sys.exit(app.exec_())
