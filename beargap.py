#!/usr/bin/python
import sys
import os
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(450, 450)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    
    pic = QtGui.QLabel(w)
    pic.setGeometry(10, 10, 400, 400)
    pic.setPixmap(QtGui.QPixmap(os.getcwd() + "/garysaurus.png"))

    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
