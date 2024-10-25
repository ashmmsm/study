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





from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QMessageBox, QRadioButton, QVBoxLayout, QHBoxLayout 
)
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()
win.resize(200,200)
win.setWindowTitle('Тест на дебилизм')

text = QLabel('Сколько будет 2+2')

answer1 = QRadioButton('5')
answer2 = QRadioButton('пять')
answer3 = QRadioButton('низнаю')
answer4 = QRadioButton('4')

main = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

main.addWidget(text, alignment = Qt.AlignCenter)

h1.addWidget(answer1, alignment = Qt.AlignLeft)
h1.addWidget(answer2, alignment = Qt.AlignLeft)
h2.addWidget(answer3, alignment = Qt.AlignLeft)
h2.addWidget(answer4, alignment = Qt.AlignLeft)

main.addLayout(h1)
main.addLayout(h2)

win.setLayout(main)

win.show()
app.exec()




from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QTextEdit, QLabel, QListWidget,
    QPushButton, QLineEdit
)
#ИНТЕРФЕЙС
application = QApplication([])
window = QWidget()
window.resize(800,500)
window.setWindowTitle('Умные заметки')

text_field = QTextEdit()

list_notes = QListWidget()
# list_notes.addItem('Понедельник')
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')

list_tags = QListWidget()
create_tag = QPushButton('Создать тег')
delete_tag = QPushButton('Удалить тег')
search = QPushButton('Поиск')
search_field = QLineEdit()
search_field.setPlaceholderText('Введите тег:')
#РАСПОЛОЖЕНИЕ
main_layout = QHBoxLayout()
list_layout = QVBoxLayout()
button_layout1 = QHBoxLayout()
button_layout2 = QHBoxLayout()

list_layout.addWidget(list_notes)
button_layout1.addWidget(create_note)
button_layout1.addWidget(delete_note)
list_layout.addLayout(button_layout1)
list_layout.addWidget(save_note)

list_layout.addWidget(list_tags)
list_layout.addWidget(search_field)
button_layout2.addWidget(create_tag)
button_layout2.addWidget(delete_tag)
list_layout.addLayout(button_layout2)
list_layout.addWidget(search)

main_layout.addWidget(text_field)
main_layout.addLayout(list_layout)

#ЗАПУСК
window.setLayout(main_layout)
window.show()
application.exec()




import json
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QTextEdit, QListWidget,
    QPushButton, QLineEdit, QInputDialog
)
#ИНТЕРФЕЙС
application = QApplication([])
window = QWidget()
window.resize(800,500)
window.setWindowTitle('Умные заметки')

text_field = QTextEdit()

list_notes = QListWidget()
note_create = QPushButton('Создать заметку')
note_delete = QPushButton('Удалить заметку')
note_save = QPushButton('Сохранить заметку')

list_tags = QListWidget()
create_tag = QPushButton('Создать тег')
delete_tag = QPushButton('Удалить тег')
search = QPushButton('Поиск')
search_field = QLineEdit()
search_field.setPlaceholderText('Введите тег:')
#РАСПОЛОЖЕНИЕ
main_layout = QHBoxLayout()
list_layout = QVBoxLayout()
button_layout1 = QHBoxLayout()
button_layout2 = QHBoxLayout()

list_layout.addWidget(list_notes)
button_layout1.addWidget(note_create)
button_layout1.addWidget(note_delete)
list_layout.addLayout(button_layout1)
list_layout.addWidget(note_save)

list_layout.addWidget(list_tags)
list_layout.addWidget(search_field)
button_layout2.addWidget(create_tag)
button_layout2.addWidget(delete_tag)
list_layout.addLayout(button_layout2)
list_layout.addWidget(search)

main_layout.addWidget(text_field)
main_layout.addLayout(list_layout)

#ФУНКЦИОНАЛ
def show_note():
    key = list_notes.selectedItems()[0].text()
    text_field.setText(data[key]["текст"])
    list_tags.clear()
    list_tags.addItems(data[key]["теги"])

def create_note():
    key, ok = QInputDialog.getText(window, "Добавить заметку", "Название заметки: ")
    if ok and key != "":
        data[key] = {"текст" : "", "теги" : []}
        list_notes.addItem(key)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        data[key]["текст"] = text_field.toPlainText()
        with open("data.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False)

def delete_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del data[key]
        list_notes.clear()
        list_tags.clear()
        text_field.clear()
        list_notes.addItems(data)
        with open("data.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = search_field.text()
        data[key]['теги'].append(tag)
        list_tags.addItem(tag)
        with open("data.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False)

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        data[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(data[key]['теги'])
        with open("data.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False)

def search_tag():
    if search.text() == 'Поиск':
        tag = search_field.text()
        data_filtred = {}

        for note in data:
            if tag in data[note]['теги']:
                data_filtred[note] = data[note]

        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(data_filtred)
        search.setText('Сбросить поиск')
    else:
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(data)
        search.setText('Поиск')

#ОБРАБОТКА СОБЫТИЙ
list_notes.itemClicked.connect(show_note)
note_create.clicked.connect(create_note)
note_save.clicked.connect(save_note)
note_delete.clicked.connect(delete_note)
create_tag.clicked.connect(add_tag)
delete_tag.clicked.connect(del_tag)
search.clicked.connect(search_tag)


#ЗАПУСК
with open('data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

list_notes.addItems(data)

window.setLayout(main_layout)
window.show()
application.exec()





from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 300)

class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = []
questions.append(Question('2 + 2','4','2','1','5'))
questions.append(Question('Почему?','Потому','Низнаю','Когда','Зачем'))
questions.append(Question('Уважаешь?','Да','Нет','(',')'))


btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире!') # текст вопроса


RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup() # это для группировки переключателей, чтобы управлять их поведением
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке


RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"



layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() # скроем панель с ответом, сначала должна быть видна панель вопросов


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
window.setLayout(layout_card)

#Функционал
buttons = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(question: Question):
    shuffle(buttons)
    lb_Question.setText(question.question)
    buttons[0].setText(question.right)
    buttons[1].setText(question.wrong1)
    buttons[2].setText(question.wrong2)
    buttons[3].setText(question.wrong3)

def check_answer():

    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

    if buttons[0].isChecked():
        lb_Result.setText('Правильно!')
    else:
        lb_Result.setText('Неверно!')

def next_question():

    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')

    window.current_question += 1
    if window.current_question >= len(questions):
        window.current_question = 0
    ask(questions[window.current_question])
    
def perehod():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(perehod)

window.current_question = -1
next_question()
window.show()
app.exec()





import json
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QVBoxLayout, QHBoxLayout,
    QTextEdit, QListWidget,
    QPushButton, QLineEdit, QInputDialog
)
#ИНТЕРФЕЙС
application = QApplication([])
window = QWidget()
window.resize(800,500)
window.setWindowTitle('Умные заметки')

text_field = QTextEdit()

list_notes = QListWidget()
note_create = QPushButton('Создать заметку')
note_delete = QPushButton('Удалить заметку')
note_save = QPushButton('Сохранить заметку')

list_tags = QListWidget()
create_tag = QPushButton('Создать тег')
delete_tag = QPushButton('Удалить тег')
search = QPushButton('Поиск')
search_field = QLineEdit()
search_field.setPlaceholderText('Введите тег:')
#РАСПОЛОЖЕНИЕ
main_layout = QHBoxLayout()
list_layout = QVBoxLayout()
button_layout1 = QHBoxLayout()
button_layout2 = QHBoxLayout()

list_layout.addWidget(list_notes)
button_layout1.addWidget(note_create)
button_layout1.addWidget(note_delete)
list_layout.addLayout(button_layout1)
list_layout.addWidget(note_save)

list_layout.addWidget(list_tags)
list_layout.addWidget(search_field)
button_layout2.addWidget(create_tag)
button_layout2.addWidget(delete_tag)
list_layout.addLayout(button_layout2)
list_layout.addWidget(search)

main_layout.addWidget(text_field)
main_layout.addLayout(list_layout)

#ФУНКЦИОНАЛ
def show_note():
    key = list_notes.selectedItems()[0].text()
    text_field.setText(data[key]["текст"])
    list_tags.clear()
    list_tags.addItems(data[key]["теги"])

def create_note():
    key, ok = QInputDialog.getText(window, "Добавить заметку", "Название заметки: ")
    if ok and key != "":
        data[key] = {"текст" : "", "теги" : []}
        list_notes.addItem(key)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        data[key]["текст"] = text_field.toPlainText()
        with open("data.json", "w", encoding='UTF-8') as file:
            json.dump(data, file, ensure_ascii=False)

#ОБРАБОТКА СОБЫТИЙ
list_notes.itemClicked.connect(show_note)
note_create.clicked.connect(create_note)
note_save.clicked.connect(save_note)


#ЗАПУСК
with open('data.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

list_notes.addItems(data)

window.setLayout(main_layout)
window.show()
application.exec()
