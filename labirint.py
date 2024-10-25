import pygame
import math

pygame.init()

# Map data
text_map = ['1111111111111',
            '1$$$$$$1$$$$1',
            '1$1111$11$1$1', 
            '1$$1$1$$$$1$1', 
            '11$1$111111$1', 
            '1$$1$$$$$$$$1', 
            '1$11$1111$111', 
            '$$1$$1$$$$1$1', 
            '1111$111111$1', 
            '1$$$$$$$$$$$1',
            '1111111111111']

TILE = 50
WIDTH = len(text_map[0])*TILE
HEIGHT = len(text_map)*TILE
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
win_rect = pygame.Rect(0, 7*TILE, TILE, TILE)
FPS = 60

player_pos = (11*TILE+10, 8*TILE+10)
player_angle = 0
player_speed = 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 0, 255)
SKYBLUE = (0, 186, 255)
GRAY = (40, 40, 40)

MAP_SCALE = 5
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (0, HEIGHT - HEIGHT // MAP_SCALE)

FOV = math.pi / 3
HALF_FOV = FOV / 3
NUM_RAYS = 650
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 0.5*DIST * TILE
SCALE = WIDTH // NUM_RAYS

walls = []
world_map = set()
mini_map = set()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '$':
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            world_map.add((i * TILE, j * TILE))
            rect = pygame.Rect(i*TILE, j*TILE, TILE, TILE)
            walls.append(rect)
             
def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE

def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        if sin_a:
            sin_a = sin_a
        else:
            sin_a = 0.000001
        if cos_a:
            cos_a = cos_a
        else:
            cos_a = 0.000001
        if cos_a >= 0:
            x, dx = (xm + TILE, 1)
        else:
            x, dx = (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * TILE
        if sin_a >= 0:
            y, dy = (ym + TILE, 1)
        else:
           y, dy = (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * TILE
        if depth_v < depth_h:
            depth = depth_v 
        else:
            depth = depth_h
        depth *= math.cos(player_angle - cur_angle)
        if depth == 0:
            depth = 0.00000001
        proj_height = PROJ_COEFF / depth
        c = 200 / (1 + depth * depth * 0.00002)
        color = (c//2, c // 2, c // 3)
        pygame.draw.rect(sc, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))
        cur_angle += DELTA_ANGLE
        
class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            new_x = self.x + player_speed * cos_a
            new_y = self.y + player_speed * sin_a
            if not self.check_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
        if keys[pygame.K_s]:
            new_x = self.x - player_speed * cos_a
            new_y = self.y - player_speed * sin_a
            if not self.check_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
        if keys[pygame.K_a]:
            new_x = self.x + player_speed * sin_a
            new_y = self.y - player_speed * cos_a
            if not self.check_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
        if keys[pygame.K_d]:
            new_x = self.x - player_speed * sin_a
            new_y = self.y + player_speed * cos_a
            if not self.check_collision(new_x, new_y):
                self.x = new_x
                self.y = new_y
        if keys[pygame.K_LEFT]:
            self.angle -= 0.02
        if keys[pygame.K_RIGHT]:
            self.angle += 0.02
    def check_collision(self, x, y):
        for wall in walls:
            if wall.collidepoint(x, y):
                return True
        return False
          
sc = pygame.display.set_mode((WIDTH, HEIGHT))
sc_map = pygame.Surface((WIDTH // MAP_SCALE, HEIGHT // MAP_SCALE))
clock = pygame.time.Clock()
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if win_rect.collidepoint(player.pos):
        sc.fill((127, 255, 0))
        font = pygame.font.SysFont('Comic Sans MS', 64)
        text = font.render("МОЛОДЕЦ!", True, WHITE)
        sc.blit(text, (HALF_WIDTH - 3*TILE, HALF_HEIGHT))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    player.movement()
    sc.fill(BLACK)
    pygame.draw.rect(sc, SKYBLUE, (0, 0, WIDTH, HALF_HEIGHT))
    pygame.draw.rect(sc, GRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        
    ray_casting(sc, player.pos, player.angle)
    sc_map.fill(BLACK)
    # pygame.draw.circle(sc, GREEN, (int(player.x), int(player.y)), 12)
    # pygame.draw.line(sc, GREEN, player.pos, (player.x + WIDTH * math.cos(player.angle), player.y + WIDTH * math. sin(player.angle)), 2)
    # for x,y in world_map:
        # pygame.draw.rect(sc, GREEN, (x, y, TILE, TILE), 2)
    map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE #координаты игрока на мини карте
    pygame.draw.circle(sc_map, GREEN, (int(map_x), int(map_y)), 5) #рисуем зелёный крун по коордиратам map_x и map_y
    for x, y in mini_map:
        pygame.draw.rect(sc_map, (160, 80, 55), (x, y, MAP_TILE, MAP_TILE)) #рисуем квадраты на мини карте
    sc.blit(sc_map, MAP_POS) #отобразим поверхность на экране
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
