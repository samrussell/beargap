#!/usr/bin/python
import sys
import os
import qrcode
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt4 import QtGui

class BearGapWindow(QtGui.QWidget):
  def __init__(self):
    super(BearGapWindow, self).__init__()
    self.initUI()

  def textToImg(self, text):
    im = qrcode.make(text)
    imq = ImageQt(im.convert("RGBA"))
    self.pic.setPixmap(QtGui.QPixmap.fromImage(imq))
    self.pic.adjustSize()
    

  def initUI(self):
    

    self.resize(450, 450)
    self.move(300, 300)
    self.setWindowTitle('Beargap')
    
    #im = Image.open("../garysaurus.png")
    im = qrcode.make("omg srsly :O")
    # need to convert to RGBA or else PIL.ImageQt fails
    imq = ImageQt(im.convert("RGBA"))

    self.pic = QtGui.QLabel(self)
    self.pic.setPixmap(QtGui.QPixmap.fromImage(imq))
    #pic.setGeometry(0, 0, 290, 290)

    qle = QtGui.QLineEdit(self)
    qle.textChanged[str].connect(self.onChanged)

    qbtn = QtGui.QPushButton('Generate QR code', self)
    qbtn.clicked.connect(self.onClicked)
    qbtn.resize(qbtn.sizeHint())
    qbtn.move(150, 0)

    self.show()

  def onClicked(self):
    self.textToImg(self.text)

  def onChanged(self, text):
    self.text = text


def main():
  app = QtGui.QApplication(sys.argv)
  bgw = BearGapWindow()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
