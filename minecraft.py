#game.py
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero


class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        self.hero = Hero( (0,0,1) )
        base.camLens.setFov(90)

game = Game()
game.run()

#mapmanager.py
class Mapmanager():
    def __init__(self):
        self.startNew()

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel('block.egg')
        self.block.setTexture(loader.loadTexture('block.png'))
        self.block.setPos(position)
        self.block.reparentTo(self.land)

    def loadLand(self, filename):
        map = open(filename)
        y = 0
        for line in map:
            block_line = line.split()
            x = 0
            for block in block_line:
                for z in range(int(block) + 1):
                    one_block = self.addBlock((x, y, z))
                x += 1
            y += 1
#hero.py
class Hero():
    def __init__(self, position):
        self.hero = loader.loadModel('smiley')
        self.hero.setPos(position)
        self.hero.setScale(0.3)
        self.hero.setColor( 1, 1, 0)
        self.hero.reparentTo(render)
        self.accept_events()

    def turn_left(self):
        current_angle = self.hero.getH()
        self.hero.setH(current_angle + 10)

    def turn_right(self):
        current_angle = self.hero.getH()
        self.hero.setH(current_angle - 10)

    def forward(self):
        current_angle = self.hero.getH() % 360
        x_from = self.hero.getX() 
        y_from = self.hero.getY()

        if current_angle > 0 and current_angle < 20:
            change_x, change_y = 0, -1
        elif current_angle < 70:
            change_x, change_y = 1, -1
        elif current_angle < 110:
            change_x, change_y = 1, 0
        elif current_angle < 160:
            change_x, change_y = 1, 1
        elif current_angle < 200:
            change_x, change_y = 0, 1
        elif current_angle < 250:
            change_x, change_y = -1, 1
        elif current_angle < 290:
            change_x, change_y = -1, 0
        elif current_angle < 340:
            change_x, change_y = -1, -1
        else:
            change_x, change_y = 0, -1

        x_to = x_from + change_x
        y_to = y_from + change_y
        self.hero.setPos( x_to, y_to, 1 )

    def accept_events(self):
        base.accept('q', self.turn_left)
        base.accept('q' + '-repeat', self.turn_left)

        base.accept('e', self.turn_right)
        base.accept('e' + '-repeat', self.turn_right)

        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)


