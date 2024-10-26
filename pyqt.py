from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QGroupBox, QLabel,
    QRadioButton, QPushButton)

app = QApplication([])

win = QWidget()
win.setWindowTitle('Викторина')

# Интерфейс
question = QLabel('Ты кто по жизни?')
button = QPushButton('Ответить')
# Интерфейс группы с ответами
answers = QGroupBox('Варианты')
rbnt1 = QRadioButton('Чел')
rbnt2 = QRadioButton('Пес')
rbnt3 = QRadioButton('Гитлер')
rbnt4 = QRadioButton('Анимешник')
# Интерфейс окна с результатом
results = QGroupBox('Результат')
result = QLabel('Правильно')
right_answer = QLabel('Гитлер')
# Размещение внутри группы с ответами
h = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v1.addWidget(rbnt1)
v1.addWidget(rbnt2)
v2.addWidget(rbnt3)
v2.addWidget(rbnt4)
h.addLayout(v1)
h.addLayout(v2)
answers.setLayout(h)
# Размещение внутри группы с результатом
v = QVBoxLayout()
v.addWidget(result)
v.addWidget(right_answer, alignment = Qt.AlignHCenter)
results.setLayout(v)
# Размещение
main_layout = QVBoxLayout()
main_layout.addWidget(question, alignment = Qt.AlignHCenter)
main_layout.addWidget(answers)
main_layout.addWidget(results)
main_layout.addWidget(button)
win.setLayout(main_layout)
# Запуск
win.show()
app.exec()
