from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
app = QApplication([])

win = QMainWindow()
win.setGeometry(0,0,500,300)
win.setWindowTitle('Exemplo QT')

label = QtWidgets.QLabel(win)
label.setText('Olá, mundo!')

label.move(100,100)
win.show()
app.exec_()