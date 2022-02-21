from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Main(object):
    def setupUi(self,MainForm):
        MainForm.setObjectName("Form")
        MainForm.resize(1139, 897)
        MainForm.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.frame = QtWidgets.QFrame(MainForm)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1031, 721))
        self.frame.setStyleSheet("background-image: url(rock-paper-scissors.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(MainForm)
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
        self.pushButton_1.setGeometry(QtCore.QRect(440, 300, 121, 31))
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
        self.pushButton_1.setObjectName("pushButton_6")
        self.pushButton_1.clicked.connect(lambda:self.gotoUserWindow())
        self.pushButton_1.clicked.connect(MainForm.hide)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 370, 121, 31))
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
        self.pushButton_2.clicked.connect(lambda:self.gotoLeaderBoard())
        self.pushButton_2.clicked.connect(MainForm.hide)

        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 440, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.Closeapp())

        self.label = QtWidgets.QLabel(MainForm)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(300, 700, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"color:white;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(MainForm)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(280, 110, 541, 171))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0,0,0,0);\n"
"color:white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("MainForm", "Form"))
        self.pushButton_1.setText(_translate("MainForm", "Play"))
        self.pushButton_2.setText(_translate("MainForm", "Leaderboard"))
        self.pushButton_3.setText(_translate("MainForm", "Quit"))
        self.label.setText(_translate("MainForm", "All right reserved. Jakub Kiełb 2022 ©"))
        self.label_2.setText(_translate("MainForm", "Paper Rock Scissors"))
    

    def gotoUserWindow(self):
            from User import Ui_User
            self.window=QtWidgets.QStackedWidget()
            self.ui=Ui_User()
            self.ui.setupUi(self.window)
            self.window.show()
    def gotoLeaderBoard(self):
            from leaderboard import Ui_Score
            self.window=QtWidgets.QStackedWidget()
            self.ui=Ui_Score()
            self.ui.setupUi(self.window)
            self.window.show()
    def Closeapp(self):
             import sys
             sys.exit()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QWidget()
    ui = Ui_Main()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec_())
