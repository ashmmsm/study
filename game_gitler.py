from pygame import *

#Создаем класс для наших спрайтов
class GameSprite():
    def __init__(self,x,y,img):
        self.image = transform.scale(image.load(img),(100,100))
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

def stop_wall(wall):
    if sprite.collide_rect(hero,wall):
        if hero.rect.x >= wall.rect.x:
            hero.rect.x += 10
        else:
            hero.rect.x -= 10

        if hero.rect.y >= wall.rect.y:
            hero.rect.y += 10
        else:
            hero.rect.y -= 10

def enemy_move(enemy):
    if enemy.rect.x < hero.rect.x:
        enemy.rect.x += 1

    if enemy.rect.x > hero.rect.x:
        enemy.rect.x -= 1

    if enemy.rect.y < hero.rect.y:
        enemy.rect.y += 1

    if enemy.rect.y > hero.rect.y:
        enemy.rect.y -= 1


#Создаем обьекты для нашей игры
wall_1 = Wall(200,100,10,600)
wall_2 = Wall(400,100,10,600)
wall_3 = Wall(600,100,10,600)

hero = GameSprite(100,400,'hero.png')
enemy1 = GameSprite(500,200,'cyborg.png')
enemy2 = GameSprite(50,0,'cyborg.png')
gold = GameSprite(600,400,'treasure.png')
#Создание экрана
window = display.set_mode((700,500))
#Картинка для нашего экрана
background = transform.scale(image.load('back.webp'),(700,500))
#шрифт
font.init()
#музыка
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
#Игровой цикл
game = True
finish = False
while game:

    window.blit(background,(0,0))
    
    #Обработка выхода из игры
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        #Движение главного героя
        keys = key.get_pressed()
        if keys[K_UP] and hero.rect.y > 0:
            hero.rect.y -= 10
        if keys[K_DOWN] and hero.rect.y < 450:
            hero.rect.y += 10
        if keys[K_LEFT] and hero.rect.x > 0:
            hero.rect.x -= 10
        if keys[K_RIGHT] and hero.rect.x < 650:
            hero.rect.x += 10

        #Движение врага
        enemy_move(enemy1)
        enemy_move(enemy2)

    #условие поражения
    if sprite.collide_rect(hero, enemy1) or sprite.collide_rect(hero, enemy2):
        lose = font.Font(None,100).render('YOU LOSE',1,(255,0,0))
        window.blit(lose,(200,200))
        finish = True

    #условие победы
    if sprite.collide_rect(hero, gold):
        win = font.Font(None,100).render('YOU WIN',1,(0,255,0))
        window.blit(win,(200,200))
        finish = True

    # stop_wall(wall_1)
    # stop_wall(wall_2)
    # stop_wall(wall_3)
    

    #Отображение персонажей
    hero.view()
    enemy1.view()
    enemy2.view()
    gold.view()

    # wall_1.view()
    # wall_2.view()
    # wall_3.view()
    #Команда отвечает за частоту отработки цикла
    time.delay(50)
    #Обновление нашего экрана
    display.update()
