# напиши здесь код основного окна игры
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        base.camLens.setFov(90)

game = Game() 
game.run()


# напиши здесь код создания и управления картой
class Mapmanager():
    def __init__(self):
        self.startNew()
        # self.addBlock((0, 10, 0))
        # self.addBlock((1, 10, 0))

    def startNew(self):
        self.land = render.attachNewNode('Land')

    def addBlock(self, position):
        self.block = loader.loadModel('block.egg')
        self.block.setTexture(loader.loadTexture('block.png'))
        self.block.setPos(position)
        self.block.reparentTo(self.land) 

    def loadLand(self, filename):
        map = open(filename) #- > ['1 0 1', ['0 1 0','0 0 0']]
        y = 0
        for line - > '1 0 1' in map:
            block_line = line.split() #- > ['1', '0', '1']
            x = 0 
            for block - > 1 in block_line:
                for z - > 0 in range(int(block) + 1):  #- > 2 во втором 2
                    one_block = self.addBlock((x -> 0, y->0, z->1)) на втором шаге 2 0 0
                x += 1
            y += 1
          далее переходим на y и z

  def loadLand(self, filename):
       map = open(filename) #- > хранится все строки
       ['0 0 0','0 1 0', '0 0 0']
       for block -> '0 0 0' in map:
           cordinate = block.split()#['0','0','0']
            x,z, y = int(cordinate[0])
       




