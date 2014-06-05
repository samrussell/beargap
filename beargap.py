#!/usr/bin/python
import sys
import os
import qrcode
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(450, 450)
    w.move(300, 300)
    w.setWindowTitle('Beargap')
    
    #im = Image.open("../garysaurus.png")
    im = qrcode.make("omg srsly :O")
    # need to convert to RGBA or else PIL.ImageQt fails
    imq = ImageQt(im.convert("RGBA"))

    pic = QtGui.QLabel(w)
    pic.setPixmap(QtGui.QPixmap.fromImage(imq))
    #pic.setGeometry(0, 0, 290, 290)

    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
