import sys
import PyQt5
from PyQt5.QtGui import QImage, QPixmap

import numpy as np
from PIL import Image
# from PIL.ImageQt import ImageQt

import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
from PyQt5 import QtGui

class QMain(qw.QWidget):

    def __init__(self):
        super().__init__()
        self.__buildUI()

    def __buildUI(self):
        self.resize(500,500)
        self.move(300,300)
        self.setWindowTitle("Data Visualizer")

        im_path = 'datasets/face2/train_B/me_base512.png' 

        self.labelIm = qw.QLabel()

        im = Image.open(im_path)
        im_rgba = im.convert('RGBA')
        qim = QImage(im_rgba.tobytes('raw', 'BGRA'), im.width, im.height, QImage.Format.Format_ARGB32)
        self.pix = QPixmap.fromImage(qim)

        scaled_pix = self.pix.scaled(self.labelIm.size(), qc.Qt.AspectRatioMode.KeepAspectRatio)

        # labelIm.setMinimumSize(10, 10)
        # labelIm.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)
        self.labelIm.setMinimumSize(128,128)
        self.labelIm.setPixmap(scaled_pix)

        labelIm2 = qw.QLabel()
        labelIm2.setMinimumSize(10, 10)
        # labelIm2.setSizePolicy(qw.QSizePolicy.Expanding, qw.QSizePolicy.Expanding)
        labelIm2.setPixmap(scaled_pix)

        layout = qw.QVBoxLayout()
        layout.addWidget(self.labelIm)
        # layout.addWidget(labelIm2)

        self.setLayout(layout)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        scaled_pix = self.pix.scaled(self.labelIm.size(), qc.Qt.AspectRatioMode.KeepAspectRatio)
        self.labelIm.setPixmap(scaled_pix)


def run():
    app = qw.QApplication(sys.argv)
    window = QMain()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()