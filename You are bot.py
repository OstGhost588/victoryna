import random

from PyQt5.QtWidgets import *
app = QApplication([])
numberlbl = QLabel("Номер переможця")
starBtn = QPushButton("Дізнатися номер переможця")
window = QWidget()
window.resize(500, 500)

lbl = QLabel("Вікторина")
main_line = QVBoxLayout()
main_line.addWidget(lbl)
def banana():
    a =random.randint(1, 10)
    numberlbl.setText(str(a))

window.setLayout(main_line)
window.show()


app.exec()