import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wid = QWidget()

    #title
    wid.setWindowTitle("生物过程补料计算器")

    #gui separate


    #input gui
    #gui label
    input_title_label = QLabel("计算参数",wid)
    input_title_label.setGeometry(950,125,200,50)
    sampling_label = QLabel("取样量:",wid)
    sampling_label.setGeometry(700,200,200,70)
    before_sampling_label = QLabel("取样前体系质量:",wid)
    before_sampling_label.setGeometry(700,300,200,70)
    after_sampling_label = QLabel("取样后体系质量:",wid)
    after_sampling_note_label =QLabel("*必填*",wid)
    after_sampling_label.setGeometry(700,400,200,70)
    after_sampling_note_label.setGeometry(1325,400,100,70)
    #gui inputline
    input_sampling_line = QLineEdit("输入 取样量",wid)
    input_sampling_line.setGeometry(920,200,400,70)
    input_before_sampling_line = QLineEdit("输入 取样前体系质量",wid)
    input_before_sampling_line.setGeometry(920,300,400,70)
    input_after_sampling_line = QLineEdit("输入 取样后体系质量",wid)
    input_after_sampling_line.setGeometry(920,400,400,70)

    
    #parameters gui
    #gui label
    feed_strategy_label = QLabel("将执行的补料策略：",wid)
    feed_strategy_label.setGeometry(100,150,300,50)
    feed_result_label = QLabel("所需的补料量：",wid)
    feed_result_label.setGeometry(100,400,300,50)
    #gui button
    plan_deploy_btn = QPushButton("设置补料策略",wid)
    plan_deploy_btn.setGeometry(1000,50,200,50)


    #execute gui
    #gui buttons
    calculate_btn = QPushButton("开始计算",wid)
    calculate_btn.setGeometry(1000,700,200,50)


    #generate window
    wid.show()

    #waiting status loop
    app.exec()