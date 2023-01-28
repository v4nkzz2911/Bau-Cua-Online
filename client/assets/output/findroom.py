# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findroom.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        Main.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 73, 75, 255), stop:0.997452 rgba(255, 189, 96, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 9, 801, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background:none;")
        self.title.setScaledContents(True)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.credit = QtWidgets.QLabel(self.centralwidget)
        self.credit.setGeometry(QtCore.QRect(0, 560, 801, 31))
        self.credit.setStyleSheet("color:white;background-color:none;")
        self.credit.setAlignment(QtCore.Qt.AlignCenter)
        self.credit.setObjectName("credit")
        self.exit = QtWidgets.QLabel(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(730, 20, 55, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.exit.setFont(font)
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit.setStyleSheet("QLabel {\n"
"background:none;\n"
"}\n"
"QLabel::hover {\n"
"background:none;\n"
"color:white;\n"
"}")
        self.exit.setAlignment(QtCore.Qt.AlignCenter)
        self.exit.setObjectName("exit")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(0, 140, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.description.setFont(font)
        self.description.setStyleSheet("background:none;")
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.roomid_label = QtWidgets.QLabel(self.centralwidget)
        self.roomid_label.setGeometry(QtCore.QRect(120, 260, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.roomid_label.setFont(font)
        self.roomid_label.setStyleSheet("background:none;")
        self.roomid_label.setObjectName("roomid_label")
        self.roomid_input = QtWidgets.QLineEdit(self.centralwidget)
        self.roomid_input.setGeometry(QtCore.QRect(250, 260, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(15)
        self.roomid_input.setFont(font)
        self.roomid_input.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"border:1px solid white; border-radius: 5px;")
        self.roomid_input.setText("")
        self.roomid_input.setObjectName("roomid_input")
        self.joinroom = QtWidgets.QPushButton(self.centralwidget)
        self.joinroom.setGeometry(QtCore.QRect(200, 410, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.joinroom.setFont(font)
        self.joinroom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.joinroom.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 127, 176), stop:1 rgba(255, 255, 127, 187));\n"
"color: rgb(255, 255, 255);")
        self.joinroom.setObjectName("joinroom")
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Game Bầu Cua Online - Find Room"))
        self.title.setText(_translate("Main", "TÌM PHÒNG"))
        self.credit.setText(_translate("Main", "Game made by MHP. You can buy me a cup of coffee through https://www.buymeacoffee.com/py.hacker.hieu, thank you very much."))
        self.exit.setText(_translate("Main", "X"))
        self.description.setText(_translate("Main", "Vui lòng nhập ID phòng bạn muốn vào"))
        self.roomid_label.setText(_translate("Main", "ID phòng:"))
        self.roomid_input.setPlaceholderText(_translate("Main", "Nhập ID phòng ở đây"))
        self.joinroom.setText(_translate("Main", "Vào phòng"))