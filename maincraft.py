game.py

from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
   def __init__(self):
       ShowBase.__init__(self)
       self.land = Mapmanager()
       x,y = self.land.loadLand("land.txt")
       self.hero = Hero((x//2,y//2,2),self.land)
       base.camLens.setFov(90)


game = Game()
game.run()



hero.py

key_switch_camera = 'c' # камера привязана к герою или нет
key_switch_mode = 'z' # можно проходить сквозь препятствия или нет


key_forward = 'w'   # шаг вперёд (куда смотрит камера)
key_back = 's'      # шаг назад
key_left = 'a'      # шаг влево (вбок от камеры)
key_right = 'd'     # шаг вправо
key_up = 'e'      # шаг вверх
key_down = 'q'     # шаг вниз


key_turn_left = 'n'     # поворот камеры направо (а мира - налево)
key_turn_right = 'm'    # поворот камеры налево (а мира - направо)

key_build = 'b'
key_destroy = 'v'

key_up = 'e'
key_down = 'q'


class Hero():
   def __init__(self, pos, land):
       self.land = land
       self.mode = True # режим прохождения сквозь всё
       self.hero = loader.loadModel('smiley')
       self.hero.setColor(1, 0.5, 0)
       self.hero.setScale(0.3)
       self.hero.setPos(pos)
       self.hero.reparentTo(render)
       self.cameraBind()
       self.accept_events()


   def cameraBind(self):
       base.disableMouse()
       base.camera.setH(180)
       base.camera.reparentTo(self.hero)
       base.camera.setPos(0, 0, 1.5)
       self.cameraOn = True


   def cameraUp(self):
       pos = self.hero.getPos()
       base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
       base.camera.reparentTo(render)
       base.enableMouse()
       self.cameraOn = False




   def changeView(self):
       if self.cameraOn:
           self.cameraUp()
       else:
           self.cameraBind()


   def turn_left(self):
       self.hero.setH((self.hero.getH() + 5) % 360)


   def turn_right(self):
       self.hero.setH((self.hero.getH() - 5) % 360)


   def look_at(self, angle):
       ''' возвращает координаты, в которые переместится персонаж, стоящий в точке (x, y),
       если он делает шаг в направлении angle'''


       x_from = round(self.hero.getX())
       y_from = round(self.hero.getY())
       z_from = round(self.hero.getZ())


       dx, dy = self.check_dir(angle)
       x_to = x_from + dx
       y_to = y_from + dy
       return x_to, y_to, z_from


   def just_move(self, angle):
       '''перемещается в нужные координаты в любом случае'''
       pos = self.look_at(angle)
       self.hero.setPos(pos)


   def move_to(self, angle):
       if self.mode:
           self.just_move(angle)
  
   def check_dir(self,angle):
       ''' возвращает округленные изменения координат X, Y,
       соответствующие перемещению в сторону угла angle.
       Координата Y уменьшается, если персонаж смотрит на угол 0,
       и увеличивается, если смотрит на угол 180.   
       Координата X увеличивается, если персонаж смотрит на угол 90,
       и уменьшается, если смотрит на угол 270.   
           угол 0 (от 0 до 20)      ->        Y - 1
           угол 45 (от 25 до 65)    -> X + 1, Y - 1
           угол 90 (от 70 до 110)   -> X + 1
           от 115 до 155            -> X + 1, Y + 1
           от 160 до 200            ->        Y + 1
           от 205 до 245            -> X - 1, Y + 1
           от 250 до 290            -> X - 1
           от 290 до 335            -> X - 1, Y - 1
           от 340                   ->        Y - 1  '''
       if angle >= 0 and angle <= 20:
           return (0, -1)
       elif angle <= 65:
           return (1, -1)
       elif angle <= 110:
           return (1, 0)
       elif angle <= 155:
           return (1, 1)
       elif angle <= 200:
           return (0, 1)
       elif angle <= 245:
           return (-1, 1)
       elif angle <= 290:
           return (-1, 0)
       elif angle <= 335:
           return (-1, -1)
       else:
           return (0, -1)


   def forward(self):
       angle =(self.hero.getH()) % 360
       self.move_to(angle)


   def back(self):
       angle = (self.hero.getH()+180) % 360
       self.move_to(angle)
  
   def left(self):
       angle = (self.hero.getH() + 90) % 360
       self.move_to(angle)


   def right(self):
       angle = (self.hero.getH() + 270) % 360
       self.move_to(angle)

   def build(self):
       angle = self.hero.getH()
       new_pos = self.look_at(angle)
       self.land.addBlock(new_pos)       

   def destroy(self):
       angle = self.hero.getH() %360
       new_pos = self.look_at(angle)
       self.land.delBlock(new_pos)
    
   def up(self):
       current_pos = self.hero.getZ()
       self.hero.setZ(current_pos + 1)

   def down(self):
       current_pos = self.hero.getZ()
       self.hero.setZ(current_pos - 1)


   def accept_events(self):
       base.accept(key_turn_left, self.turn_left)
       base.accept(key_turn_left + '-repeat', self.turn_left)
       base.accept(key_turn_right, self.turn_right)
       base.accept(key_turn_right + '-repeat', self.turn_right)


       base.accept(key_forward, self.forward)
       base.accept(key_forward + '-repeat', self.forward)
       base.accept(key_back, self.back)
       base.accept(key_back + '-repeat', self.back)
       base.accept(key_left, self.left)
       base.accept(key_left + '-repeat', self.left)
       base.accept(key_right, self.right)
       base.accept(key_right + '-repeat', self.right)

       base.accept(key_up, self.up)
       base.accept(key_up + '-repeat', self.up)

       base.accept(key_down, self.down)
       base.accept(key_up + '-repeat', self.down)



       base.accept(key_build, self.build) #подписка
       base.accept(key_destroy, self.destroy)
       

       base.accept(key_switch_camera, self.changeView)


mapmanager.py

class Mapmanager():
   """ Управление картой """
   def __init__(self):
       self.model = 'block' # модель кубика лежит в файле block.egg
       # # используются следующие текстуры:
       self.texture = 'block.png'         
       self.colors = [
           (0.2, 0.2, 0.35, 1),
           (0.2, 0.5, 0.2, 1),
           (0.7, 0.2, 0.2, 1),
           (0.5, 0.3, 0.0, 1)
       ] #rgba
       # создаём основной узел карты:
       self.startNew()
       # self.addBlock((0,10, 0))

   def startNew(self):
       """создаёт основу для новой карты"""
       self.land = render.attachNewNode("Land") # узел, к которому привязаны все блоки карты

   def getColor(self, z):
       if z < len(self.colors):
           return self.colors[z]
       else:
           return self.colors[len(self.colors) - 1]

   def addBlock(self, position):
       # создаём строительные блоки
       self.block = loader.loadModel(self.model)
       self.block.setTexture(loader.loadTexture(self.texture))
       self.block.setPos(position)
       self.color = self.getColor(int(position[2]))
       self.block.setColor(self.color)
       self.block.setTag("at", str(position) )
       self.block.reparentTo(self.land)

   def findBlocks(self, pos):
       return self.land.findAllMatches("=at=" + str(pos) )
   
   def delBlock(self, position):
       blocks = self.findBlocks(position) #['блок 1', 'блок 2',...]
       for block in blocks:
           block.removeNode()

   def clear(self):
       """обнуляет карту"""
       self.land.removeNode()
       self.startNew()


   def loadLand(self, filename):
       """создаёт карту земли из текстового файла, возвращает её размеры"""
       self.clear()
       with open(filename) as file:
           y = 0
           for line in file:
               x = 0
               line = line.split(' ')
               for z in line:
                   for z0 in range(int(z)+1):
                       block = self.addBlock((x, y, z0))
                   x += 1
               y += 1
       return x,y
   
   def findblocks(self, pos):
       return self.land.findAllMatches("=at=" + str(pos))
   
   class Mapmanager():

        def isEmpty(self,pos):
            blocks = self.findBlocks(pos)
            if blocks:
                return False
            else:
                return True

        def findHighestEmpty(self,pos):
            x,y,z = pos
            z = 1
            while not self.isEmpty((x,y,z)):
                z += 1
                return (x, y, z)



        #def buildBlock(self,pos):



   def delBlock(self,position):
       """удаляет блоки в указанной позиции"""
       blocks = self.findBlocks(position)
       for block in blocks:
           



land.txt

0 0 0 0 3 3 0 0 0 0 0 3 3 0 0 0 0 0 0 0
0 0 0 3 2 2 3 0 0 0 0 3 3 0 0 0 0 0 0 0
0 0 3 3 1 1 3 3 0 0 0 3 3 0 0 0 0 0 0 0
0 3 3 1 0 0 1 3 3 0 0 3 3 0 0 0 0 0 0 0
3 3 1 0 0 0 0 1 3 3 0 3 3 0 0 0 0 0 0 0
3 3 1 0 0 0 0 1 3 3 0 3 3 0 0 0 0 0 0 0
3 3 1 1 1 1 1 1 3 3 0 3 3 0 0 0 0 0 0 0
3 3 2 2 2 2 2 2 3 3 0 3 3 0 0 0 0 0 0 0
3 3 3 3 3 3 3 3 3 3 0 3 3 0 0 0 0 0 0 0
3 3 2 2 2 2 2 2 3 3 0 3 3 0 0 0 0 0 0 0
3 3 1 0 0 0 0 1 3 3 0 3 3 0 0 0 0 0 3 0
3 3 1 0 0 0 0 1 3 3 0 3 3 0 0 0 0 2 3 0
3 3 1 0 0 0 0 1 3 3 0 3 3 2 2 2 2 3 3 0
3 3 1 0 0 0 0 1 3 3 0 3 3 3 3 3 3 3 3 0
3 3 1 0 0 0 0 1 3 3 0 3 3 3 3 3 3 3 3 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 2 2 2 1 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 2 3 2 1 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 2 2 2 1 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 0 0 0 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 0 0 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 1 0 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 1 0 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 0 0 1 1
1 1 1 1 2 3 2 1 1 1 1 1 1 1 1 1 0 1 2 3
1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 3 3 3 3 3 3 3 3 1 3 3 3 3 3 3 3 3 3 3
1 3 2 2 2 2 2 2 3 1 3 3 2 2 2 2 2 2 3 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 1 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 1 2 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 2 3 1 3 2 0 0 0 0 0 0 2 3
1 3 2 1 1 1 1 2 3 1 3 2 0 0 0 0 0 0 2 3
1 3 3 3 3 3 3 3 3 1 3 3 2 2 2 2 2 2 3 3
1 3 3 3 3 3 3 3 3 1 3 3 3 3 3 3 3 3 3 3


land2.txt

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0


land3.txt


0 0 0 0 0 0 0
0 0 0 1 0 0 0
0 0 1 2 1 0 0
0 1 2 3 2 1 0
0 0 1 2 1 0 0
0 0 0 1 0 0 0
0 0 0 0 0 0 0
       
