
from doctest import DONT_ACCEPT_TRUE_FOR_1
from PyQt5 import QtCore, QtGui, QtWidgets
from sqlalchemy import true


class Ui_Score(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.resize(1139, 897)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1031, 721))
        self.frame.setStyleSheet("background-image: url(rock-paper-scissors.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(40, 40, 1011, 701))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(15)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(0,0,0,180);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.pushButton_1 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_1.setGeometry(QtCore.QRect(450, 580, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color:#e6b071;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 170, 0);\n"
"}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(lambda:self.Scores())

        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(230, 150, 551, 421))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border:none;\n"
"color:white ;\n"
"padding-left:140px ;\n"

)
        self.textBrowser.setObjectName("textBrowser")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 630, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color:#e6b071;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 170, 0);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.gotoMain())
        self.pushButton_2.clicked.connect(Form.hide)

        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setEnabled(True)
        self.label_1.setGeometry(QtCore.QRect(230, 60, 641, 151))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"color:white;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_1.setText(_translate("Form", "Show the results"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label_1.setText(_translate("Form", "Leaderboard"))
   
    def gotoMain(self):
             from main import Ui_Main
             self.window=QtWidgets.QStackedWidget()
             self.ui=Ui_Main()
             self.ui.setupUi(self.window)
             self.window.show()

    def Scores(self):
            import sqlite3
            import pandas as pd
            conn = sqlite3.connect('Score') 
            c = conn.cursor()
            c.execute("SELECT Username,score  FROM USER ORDER BY score DESC")
            results = c.fetchall()
            df = pd.DataFrame(results,columns=['Username','score'])
            df.index += 1 
            self.textBrowser.setText(str(df))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Score()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
