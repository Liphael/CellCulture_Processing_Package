import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = QWidget()

    #title
    wid.setWindowTitle("生物过程补料计算器")

    #generate window
    wid.show()

    #waiting status loop
    app.exec()