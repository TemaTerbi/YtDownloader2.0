import dataclasses
import sys
import pytube
import time
import getpass
import re

from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import QObject, QEvent, QPropertyAnimation
from PyQt6.QtGui import QHoverEvent, QColor
from PyQt6.QtWidgets import QPushButton, QGraphicsColorizeEffect, QWidget
from pytube import YouTube

import ytui
from ytui import Ui_MainWindow

@dataclasses.dataclass
class ColorAnimation:
    element: QWidget
    color: QColor
    duration: int = 1000
    animation_in: QPropertyAnimation = None
    effect: QGraphicsColorizeEffect = None

    def __post_init__(self):
        self.effect = QGraphicsColorizeEffect(self.element)
        self.element.setGraphicsEffect(self.effect)
        self.effect.setColor(self.color)
        # create animation
        self.animation_in = QPropertyAnimation(self.effect, b'strength')
        self.animation_in.setStartValue(0.)
        self.animation_in.setEndValue(1.)
        self.animation_in.setDuration(self.duration)

        # same animation, reversed
        self.animation_out = QPropertyAnimation(self.effect, b'strength')
        self.animation_out.setStartValue(1.)
        self.animation_out.setEndValue(0.)
        self.animation_out.setDuration(self.duration)
        # for some reason have to start the animation for buttons to not blink
        self.animation_out.start()

    def start(self):
        time = self.animation_out.currentTime()
        self.animation_out.stop()
        self.animation_in.start()
        self.animation_in.setCurrentTime(self.duration - time)

    def revert(self):
        time = self.animation_in.currentTime()
        self.animation_in.stop()
        self.animation_out.start()
        self.animation_out.setCurrentTime(self.duration - time)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.name_user = getpass.getuser()
        # self.video = YouTube('https://www.youtube.com/watch?v=i3wfWe9Dev0')
        self.path = f'C:\\Users\\{self.name_user}\\Desktop'
        self.quality = ''
        self.button_colors = dict()
        # self.setWindowIcon(QtGui.QIcon('./icon.png'))
        self.logical_ui()

    def logical_ui(self):
        self.ui.pushButton.clicked.connect(self.check_btn)
        self.ui.pushButton_2.clicked.connect(self.set_quality_to_144)
        self.ui.pushButton_3.clicked.connect(self.set_quality_to_360)
        self.ui.pushButton_4.clicked.connect(self.set_quality_to_720)
        self.ui.pushButton_5.clicked.connect(self.set_quality_to_1080)
        self.ui.pushButton_6.clicked.connect(self.download_btn)

        # find all buttons in the window
        buttons = self.findChildren(QPushButton)
        # attach an event filter to buttons
        for b in buttons:
            b.installEventFilter(self)
            self.animate_button(b)

    def animate_button(self, button):
        styles = button.styleSheet()
        print(button.dynamicPropertyNames())
        button.autoFillBackground()

        # parse a fucking css stylesheet
        def parse_stylesheet(ss: str):
            prop = 'background-color'
            color_re = re.compile(f'.*{prop}:\s*(#[a-f0-9]*)')

            color = None
            hover_next = False
            hover_block = False
            new_ss = ''
            for line in ss.split('\n'):
                # start of hover block
                if 'hover' in line:
                    hover_block = True
                # found property
                if hover_block and (m := color_re.match(line)):
                    value, = m.groups()
                    print(value)
                    color = QColor(value)
                # do not add hover style to new style
                if not hover_block:
                    new_ss += line + '\n'
                # find end of hover style
                if '}' in line:
                    hover_block = False

            if color is None:
                raise ValueError(f"Нет hover стиля! ({color})")
            return color, new_ss

        # get hover color and new styles without hover
        color, new_styles = parse_stylesheet(styles)
        button.setStyleSheet(new_styles)

        print(new_styles)
        print(color)
        ca = ColorAnimation(button, color, 300)
        self.button_colors[button] = ca

    def get_animation(self, obj: QObject):
        return self.button_colors[obj]

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if isinstance(obj, QPushButton) and event.type() == QEvent.Type.HoverEnter:
            print('enter')
            self.get_animation(obj).start()
        elif isinstance(obj, QPushButton) and event.type() == QEvent.Type.HoverLeave:
            print('leave')
            self.get_animation(obj).revert()
        # print(obj, event, event.type())

        return super(MainWindow, self).eventFilter(obj, event)

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
app.setWindowIcon(QtGui.QIcon('icon.png'))
application = MainWindow()
window = QtWidgets.QMainWindow()
window.setWindowIcon(QtGui.QIcon('BLBwO.png'))
application.show()


sys.exit(app.exec())
