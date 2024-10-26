from pygame import* 
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
