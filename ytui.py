from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setStyleSheet("background-color: #8B90A1;")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 30, 401, 31))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
                                    "    background-color: white;\n"
                                    "    border-radius: 12px;\n"
                                    "    padding: 5px;\n"
                                    "    font: 87 10pt \"Arial Black\";\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:hover {\n"
                                    "    background-color: #dee6ed;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus{\n"
                                    "    background-color: #dee6ed;\n"
                                    "};\n"
                                    "\n"
                                    "")
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 501, 191))
        self.frame.setStyleSheet("background-color: #da7e78;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #dee6ed;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid white;\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #da7e78;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "};")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #dee6ed;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid white;\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #da7e78;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "};")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #dee6ed;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid white;\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #da7e78;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "};")
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setGeometry(QtCore.QRect(140, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #dee6ed;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid white;\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #da7e78;\n"
                                        "    font: 87 8pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "};")
        self.pushButton_5.setFlat(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 70, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setToolTipDuration(-1)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "    border-radius: 12px;\n"
                                      "    background-color: #dee6ed;\n"
                                      "    font: 87 8pt \"Arial Black\";\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    border: 2px solid white;\n"
                                      "    border-radius: 12px;\n"
                                      "    background-color: #da7e78;\n"
                                      "    font: 87 8pt \"Arial Black\";\n"
                                      "    color: white;\n"
                                      "};")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 300, 391, 61))
        self.label.setStyleSheet("background-color: white;\n"
                                 "font: 87 14pt \"Montserrat\";\n"
                                 "border-radius: 12px;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 410, 391, 71))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setToolTipDuration(-1)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #93c47d;\n"
                                        "    font: 87 14pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "    border: 2px solid white;\n"
                                        "    border-radius: 12px;\n"
                                        "    background-color: #da7e78;\n"
                                        "    font: 87 14pt \"Arial Black\";\n"
                                        "    color: white;\n"
                                        "};")
        self.pushButton_6.setFlat(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame.raise_()
        self.lineEdit.raise_()
        self.label.raise_()
        self.pushButton_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Загрузчик видео"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Введите ссылку"))
        self.pushButton_2.setText(_translate("MainWindow", "144P"))
        self.pushButton_3.setText(_translate("MainWindow", "360P"))
        self.pushButton_4.setText(_translate("MainWindow", "720P"))
        self.pushButton_5.setText(_translate("MainWindow", "1080P"))
        self.pushButton.setText(_translate("MainWindow", "Проверить"))
        self.pushButton_6.setText(_translate("MainWindow", "Скачать!"))
