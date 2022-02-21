
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPropertyAnimation, QPoint, QEasingCurve

class Ui_Game(object):
    def setupUi(self,FormGame):
        FormGame.setObjectName("Form1")
        FormGame.resize(1139, 897)
        self.frame = QtWidgets.QFrame(FormGame)
        FormGame.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        FormGame.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame.setGeometry(QtCore.QRect(30, 30, 1031, 721))
        self.frame.setStyleSheet("background-image: url(rock-paper-scissors.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(FormGame)
        self.frame_2.setGeometry(QtCore.QRect(40, 40, 1011, 701))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(15)
        self.frame_2.setFont(font)
        self.frame_2.setStyleSheet("background-color: rgb(0,0,0,200);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.pushButton_1 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setWeight(50)

        self.pushButton_1.setFont(font)
        self.pushButton_1.setGeometry(QtCore.QRect(460, 540, 111, 31))
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
        self.pushButton_1.clicked.connect(lambda:self.bot())
        self.pushButton_1.clicked.connect(lambda:self.answer())
        self.pushButton_1.clicked.connect(lambda:self.savescore())
        self.pushButton_1.clicked.connect(lambda:self.displayscore())
        self.pushButton_1.clicked.connect(lambda:self.UpdateScore())

        self.pushButton_2 = QtWidgets.QPushButton(FormGame)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setGeometry(QtCore.QRect(920, 62, 91, 31))
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
        self.pushButton_2.clicked.connect(lambda:self.restart())
        self.pushButton_2.clicked.connect(lambda:self.clearscore())
        self.pushButton_2.clicked.connect(lambda:self.generateBotName())

        self.pushButton_3 = QtWidgets.QPushButton(FormGame)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setWeight(50)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 110, 91, 31))
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
        self.pushButton_3.clicked.connect(lambda:self.gotoLeaderBoard())
        self.pushButton_3.clicked.connect(lambda:self.clearscore())
        self.pushButton_3.clicked.connect(FormGame.hide)
        self.pushButton_3.setFont(font)

        self.pushButton_4 = QtWidgets.QPushButton(FormGame)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("font bottons music")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
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
        self.pushButton_4.setObjectName("pushButton_7")
        self.pushButton_4.clicked.connect(lambda:self.OpenMusic())

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(880, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(lambda:self.clearscore())
        self.pushButton_5.clicked.connect(lambda:self.close())

        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 590, 111, 101))
        self.pushButton_6.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:50px;\n"
"color:white;\n"
"background-color:#e6b071;\n"
"image: url(rock-128.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 170, 0);\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(lambda:self.label.setStyleSheet("image: url(rock-128.png);"))
        self.pushButton_6.clicked.connect(lambda:self.label.setText('.'))

        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setGeometry(QtCore.QRect(460, 590, 111, 101))
        self.pushButton_7.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:50px;\n"
"color:white;\n"
"background-color:#e6b071;\n"
"image: url(paper-128.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 170, 0);\n"
"}")
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(lambda:self.label.setStyleSheet("image: url(paper-128.png);"))
        self.pushButton_7.clicked.connect(lambda:self.label.setText('.'))


        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(740, 590, 111, 101))
        self.pushButton_8.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:50px;\n"
"color:white;\n"
"background-color:#e6b071;\n"
"image: url(scissors-128.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(255, 170, 127);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"background-color:rgb(255, 170, 0);\n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(lambda:self.label.setStyleSheet("image: url(scissors-128.png);"))
        self.pushButton_8.clicked.connect(lambda:self.label.setText('.'))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(11)
        font.setWeight(50)
        self.pushButton_8.setFont(font)


        self.label = QtWidgets.QLabel(FormGame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(440, 390, 241, 181))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(FormGame)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(440, 200, 241, 181))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(FormGame)
        self.label_3.setGeometry(QtCore.QRect(430, 65, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(FormGame)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(80, 240, 221, 191))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setPointSize(21)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(0,0,0,0);\n""color:white;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        self.label_5 = QtWidgets.QLabel(FormGame)
        self.label_5.setGeometry(QtCore.QRect(46, 52, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Mongolian Baiti")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        

        self.retranslateUi(FormGame)
        QtCore.QMetaObject.connectSlotsByName(FormGame)


    def retranslateUi(self, FormGame):
        _translate = QtCore.QCoreApplication.translate
        FormGame.setWindowTitle(_translate("FormGame", "FormGame"))
        self.pushButton_1.setText(_translate("FormGame", "Play"))
        self.pushButton_2.setText(_translate("FormGame", "Restart"))
        self.pushButton_3.setText(_translate("Form", "Leaderboard"))
        self.pushButton_5.setText(_translate("FormGame", "Quit"))
        self.pushButton_4.setText(_translate("FormGame", "m"))

    
    def close(self):
            import sys
            sys.exit()
            
    def bot(self):
            import random
            list1=["image: url(rock-128.png);","image: url(paper-128.png);","image: url(scissors-128.png);"]
            choice=random.choice(list1) 
            if self.label.styleSheet()=='':
                    self.label_2.setStyleSheet("color:white;margin:50px;")
                    self.label_2.setText("Choose a tool")
            else:
                    self.label_2.clear()
                    self.label_2.setStyleSheet(choice)

    def answer(self):
                if (self.label.styleSheet() =="image: url(rock-128.png);" and self.label_2.styleSheet() == "image: url(rock-128.png);") or (self.label.styleSheet() =="image: url(paper-128.png);" and self.label_2.styleSheet() =="image: url(paper-128.png);") or (self.label.styleSheet() =="image: url(scissors-128.png);" and self.label_2.styleSheet() == "image: url(scissors-128.png);"):
                        self.label_4.setText("Draw")
                        self.anim = QPropertyAnimation(self.label_4, b"pos")
                        self.anim.setEasingCurve(QEasingCurve.OutBounce)
                        self.anim.setEndValue(QPoint(100,275))
                        self.anim.setDuration(800)
                        self.anim.start()

                elif (self.label.styleSheet() =="image: url(rock-128.png);" and self.label_2.styleSheet() =="image: url(scissors-128.png);") or (self.label.styleSheet() =="image: url(paper-128.png);" and self.label_2.styleSheet() == "image: url(rock-128.png);") or (self.label.styleSheet() == "image: url(scissors-128.png);" and self.label_2.styleSheet() == "image: url(paper-128.png);"):
                        self.label_4.setText("Win")
                        self.anim = QPropertyAnimation(self.label_4, b"pos")
                        self.anim.setEasingCurve(QEasingCurve.OutBounce)
                        self.anim.setEndValue(QPoint(100, 450))
                        self.anim.setDuration(800)
                        self.anim.start()

                elif self.label.styleSheet() =="":
                        self.label_4.setText("")

                else:
                        self.label_4.setText("Lose")
                        self.anim = QPropertyAnimation(self.label_4, b"pos")
                        self.anim.setEasingCurve(QEasingCurve.OutBounce)
                        self.anim.setEndValue(QPoint(100, 100))
                        self.anim.setDuration(800)
                        self.anim.start()

    def savescore(self):
            if self.label_4.text()=="Win":
                    self.suma=0
                    self.suma+=1
                    with open("saving.txt","a") as file:
                            file.write(f"{self.suma}")

    def displayscore(self):
            with open("saving.txt","r",encoding = 'utf-8') as self.file:
                    self.Amount_of_elements=self.file.read()
            self.label_5.setText("Score:"+str(len(self.Amount_of_elements)))
            with open('username.txt','r') as user:
                             self.username1=user.read()

    def UpdateScore(self):     
            import sqlite3
            conn = sqlite3.connect('Score') 
            c = conn.cursor()
            product_sql = "UPDATE  USER SET score=? WHERE Username=?;"
            c.execute(product_sql,(len(self.Amount_of_elements),self.username1))
            conn.commit()

    def clearscore(self):
            if self.pushButton_3.isEnabled:
                   with open("saving.txt","a") as self.file:
                           self.file.truncate(0)
                   with open("username.txt","a") as self.file1:
                           self.file1.truncate(0)
    def restart(self):
            self.label.setStyleSheet('')
            self.label_2.setText("")
            self.label_2.setStyleSheet('')
            self.label_3.setText('')
            self.label_4.setText('')
            self.label_5.setText('')
    def generateBotName(self):
            from faker import Faker
            fake = Faker()
            self.label_3.setText(fake.name())

    def OpenMusic(self):
            import winsound
            winsound.PlaySound(r'songofc.wav', winsound.SND_ASYNC)

    def gotoLeaderBoard(self):
            from leaderboard import Ui_Score
            self.window=QtWidgets.QStackedWidget()
            self.ui=Ui_Score()
            self.ui.setupUi(self.window)
            self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormGame = QtWidgets.QWidget()
    ui = Ui_Game()
    ui.setupUi(FormGame)
    FormGame.show()
    sys.exit(app.exec_())
