import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = QWidget()

    #title
    wid.setWindowTitle("生物过程补料计算器")

    #GUI buttons
    plan_deploy_btn = QPushButton("加载补料策略")
    calculate_btn = QPushButton("开始计算")

    #load buttons
    plan_deploy_btn.setParent(wid)
    calculate_btn.setParent(wid)

    #generate window
    wid.show()

    #waiting status loop
    app.exec()