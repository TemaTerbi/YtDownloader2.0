import sys
import pytube
import time
import getpass

from PyQt6 import QtWidgets, QtGui, QtCore
from pytube import YouTube

import ytui
from ytui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.name_user = getpass.getuser()
        # self.video = YouTube('https://www.youtube.com/watch?v=i3wfWe9Dev0')
        self.path = f'C:\\Users\\{self.name_user}\\Desktop'
        self.quality = ''
        self.logical_ui()

    def logical_ui(self):
        self.ui.pushButton.clicked.connect(self.check_btn)
        self.ui.pushButton_2.clicked.connect(self.set_quality_to_144)
        self.ui.pushButton_3.clicked.connect(self.set_quality_to_360)
        self.ui.pushButton_4.clicked.connect(self.set_quality_to_720)
        self.ui.pushButton_5.clicked.connect(self.set_quality_to_1080)
        self.ui.pushButton_6.clicked.connect(self.download_btn)

    def check_btn(self):
        try:
            url = self.ui.lineEdit.text()
            self.video = YouTube(url)
            time.sleep(2)
            self.ui.label.setText("Ссылка корректая, продолжаю работу...")
        except Exception as e:
            self.ui.label.setText("Ссылка введена неправильно!")

    def set_quality_to_144(self):
        self.quality = '144'
        self.ui.label.setText("Вы выбрали качество 144Р")

    def set_quality_to_360(self):
        self.quality = '360'
        self.ui.label.setText("Вы выбрали качество 360Р")

    def set_quality_to_720(self):
        self.quality = '720'
        self.ui.label.setText("Вы выбрали качество 720Р")

    def set_quality_to_1080(self):
        self.quality = '1080'
        self.ui.label.setText("Вы выбрали качество 1080Р")

    def download_btn(self):
        try:
            if self.quality == '144':
                self.download(17)
            elif self.quality == '360':
                self.download(18)
            elif self.quality == '720':
                self.download(22)
            elif self.quality == '1080':
                self.download(299)
            else:
                self.ui.label.setText("Ссылка не вставлена")
        except Exception as e:
            self.ui.label.setText("Ссылка не вставлена")

    def download(self, itag):
        try:
            self.video.streams.get_by_itag(itag).download(output_path=self.path)
            self.ui.label.setText("Видео успешно загружено")
        except Exception as e:
            self.ui.label.setText("Загрузка не завершена")


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())
