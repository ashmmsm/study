from pygame import *

#Создаем класс для наших спрайтов
class GameSprite():
    def __init__(self,x,y,img):
        self.image = transform.scale(image.load(img),(70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    #Способность отображение для персонажей
    def view(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Wall():
    def __init__(self,x,y,width,height):
        self.image = Surface((width,height))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def view(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


#Создаем обьекты для нашей игры
wall_1 = Wall(50,50,600,20)
hero = GameSprite(100,400,'hero.png')
enemy = GameSprite(500,200,'cyborg.png')
gold = GameSprite(600,400,'treasure.png')
#Создание экрана
window = display.set_mode((700,500))
#Картинка для нашего экрана
background = transform.scale(image.load('background.jpg'),(700,500))

#Игровой цикл
game = True
while game:

    window.blit(background,(0,0))
    
    #Обработка выхода из игры
    for e in event.get():
        if e.type == QUIT:
            game = False

    #Движение главного героя
    keys = key.get_pressed()
    if keys[K_UP]:
        hero.rect.y -= 10
    if keys[K_DOWN]:
        hero.rect.y += 10
    if keys[K_LEFT]:
        hero.rect.x -= 10
    if keys[K_RIGHT]:
        hero.rect.x += 10

    #Отображение персонажей
    hero.view()
    enemy.view()
    gold.view()

    wall_1.view()
    #Команда отвечает за частоту отработки цикла
    time.delay(5)
    #Обновление нашего экрана
    display.update()






from pygame import *
from random import randint
#Создаем экран
window = display.set_mode((700,500))
display.set_caption('Gitler VS Pica')
#Загружаем картинки
img = image.load('back.jpg')
img = transform.scale(img,(700,500))

gitler = transform.scale(image.load('gitler.png'),(150,150))
pica = transform.scale(image.load('pica.png'),(150,150))

gitler_x = 100
gitler_y = 300

pica_x = 500
pica_y = 300

#Игровой цикл
clock = time.Clock()
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(img,(0,0))
    window.blit(gitler,(gitler_x,gitler_y))
    window.blit(pica,(gitler_x - randint(-100,100),gitler_y - randint(-100,100)))

    keys = key.get_pressed()
    if keys[K_UP] and gitler_y > 0:
        gitler_y -= 10
    if keys[K_DOWN] and gitler_y < 350:
        gitler_y += 10
    if keys[K_LEFT] and gitler_x > 0:
        gitler_x -= 10
    if keys[K_RIGHT] and gitler_x < 550:
        gitler_x += 10

    clock.tick(10)
    display.update()


''''''''''
Калкулятор ИМТ
''''''''''
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QLineEdit, QPushButton,
    QLabel, QVBoxLayout)

app = QApplication([])

window = QWidget()
window.setWindowTitle('Калькулятор ИМТ')
window.resize(400,200)

result = QLabel('Введите ваши данные: ')
result.setStyleSheet('''
                        color: black;
                        background-color: white;
                        font-size: 30px;
                        padding: 10px;
                        border: 5px solid black;
''')
weight = QLineEdit()
weight.setStyleSheet('''
                        color: black;
                        background-color: white;
                        font-size: 20px;
                        padding: 10px;
                        border: 5px solid black;
''')
weight.setPlaceholderText('Введите ваш вес: ')
height = QLineEdit()
height.setStyleSheet('''
                        color: black;
                        background-color: white;
                        font-size: 20px;
                        padding: 10px;
                        border: 5px solid black;
''')
height.setPlaceholderText('Введите ваш рост: ')
button = QPushButton('Расчитать')
button.setStyleSheet('''
                        color: black;
                        background-color: white;
                        font-size: 20px;
                        padding: 10px;
                        border: 5px solid black;
''')

layout = QVBoxLayout()
layout.addWidget(result)
layout.addWidget(weight)
layout.addWidget(height)
layout.addWidget(button)

def show_result():
    ves = weight.text()
    rost = height.text()
    try:
        res = int(ves) / float(rost)**2
        if res < 25:
            result.setText('Ваш вес в пределах нормы')
        else:
            result.setText('У вас избыточный вес')
    except:
        result.setText('Вам нужно ввести цифры!')

button.clicked.connect(show_result)

window.setLayout(layout)
window.show()
app.exec()
