#!/usr/bin/python
import sys
import os
import qrcode
import hashlib
import base64
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt4 import QtGui
from PyQt4 import Qt

class BearGapWindow(QtGui.QWidget):
  def __init__(self):
    super(BearGapWindow, self).__init__()
    self.initUI()

  def makeQRCode(self, text):
    qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_H,
      box_size=6,
      border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    return qr.make_image()

  def textToImg(self, plaintext):
    #text = base64.b64encode(str(plaintext).encode("utf-8"))
    text = str(plaintext).encode("utf-8")
    length = len(text)
    m = hashlib.sha256()
    m.update(text)
    texthash = m.hexdigest()
    qrsize = 50
    div = length/qrsize
    modulus = length%qrsize
    if modulus > 0:
      div = div + 1


    # clear layout
    while not self.qrbox.isEmpty():
      item = self.qrbox.itemAt(0)
      item.widget().setParent(None)

    #self.pic.setPixmap(QtGui.QPixmap.fromImage(imq))
    #self.pic.adjustSize()
    pic = []
    for p in range(div):
      im = self.makeQRCode('bearcode:%s[%dof%d] %s' % (texthash, p+1, div, text[p*qrsize:min(((p+1)*qrsize),length)]))
      #imq = ImageQt(im.resize((im.size[0]/1, im.size[1]/1), Image.ANTIALIAS).convert("RGBA"))
      imq = ImageQt(im.convert("RGBA"))
      painter = QtGui.QPainter(imq)
      imqrect = imq.rect()
      painter.setFont(QtGui.QFont("Arial", 24))
      rect = painter.boundingRect(imqrect, 0x84, "%d of %d" % (p+1, div))
      painter.fillRect(rect, QtGui.QColor(255,255,255))
      painter.drawText(imqrect, 0x84, "%d of %d" % (p+1, div))
      del painter
      thispic = QtGui.QLabel()
      thispic.setPixmap(QtGui.QPixmap.fromImage(imq))
      thispic.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
      self.qrbox.addWidget(thispic)
      pic.append(thispic)
    

  def initUI(self):

    self.resize(450, 450)
    self.move(300, 300)
    self.setWindowTitle('Beargap')
    
    #im = Image.open("../garysaurus.png")
    im = qrcode.make("omg srsly :O")
    # need to convert to RGBA or else PIL.ImageQt fails
    imq = ImageQt(im.convert("RGBA"))

    self.pic = QtGui.QLabel()
    self.pic.setPixmap(QtGui.QPixmap.fromImage(imq))
    #pic.setGeometry(0, 0, 290, 290)
    self.qrwidget = QtGui.QWidget()
    self.qrbox = QtGui.QHBoxLayout()
    self.qrbox.addWidget(self.pic)
    self.qrbox.setSizeConstraint(QtGui.QLayout.SetFixedSize)
    self.qrwidget.setLayout(self.qrbox)

    self.textedit = QtGui.QTextEdit()
    self.textedit.textChanged.connect(self.onChanged)
    self.textedit.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)

    qbtn = QtGui.QPushButton('Generate QR code')
    qbtn.clicked.connect(self.onClicked)
    qbtn.resize(qbtn.sizeHint())
    #qbtn.move(150, 0)

    # configure layout
    hbox = QtGui.QHBoxLayout()
    hbox.addWidget(self.textedit)
    hbox.addWidget(qbtn)

    scrollArea = QtGui.QScrollArea()
    scrollArea.setWidget(self.qrwidget)
    scrollArea.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

    vbox = QtGui.QVBoxLayout()
    vbox.addWidget(scrollArea)
    vbox.addLayout(hbox)
        
    self.setLayout(vbox)

    self.textToImg("gary")

    self.show()

  def onClicked(self):
    self.text = self.textedit.toPlainText()
    #print self.text
    self.textToImg(self.text)

  def onChanged(self):
    #self.text = self.textedit.toPlainText()
    pass


def main():
  app = QtGui.QApplication(sys.argv)
  bgw = BearGapWindow()
  sys.exit(app.exec_())

if __name__ == '__main__':
  main()
