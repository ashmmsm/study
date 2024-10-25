import pygame
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Размеры экрана
WIDTH, HEIGHT = 800, 600

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ВЫ КТО ТАКИЕ???")

# Размеры платформ
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100

# Скорость платформ и мяча
PADDLE_SPEED = 6
BALL_SPEED_X = 6
BALL_SPEED_Y = 6

# Создание платформ и мяча
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
puk_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Счет
player_score = 0
puk_score = 0

# Функция для отрисовки элементов
def draw_elements():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, puk_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    font = pygame.font.Font(None, 36)
    player_text = font.render(str(player_score), True, WHITE)
    puk_text = font.render(str(puk_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 50))
    screen.blit(puk_text, (WIDTH // 4 * 3, 50))

# Функция для обновления игры
def update():
    global player_score, puk_score, BALL_SPEED_X, BALL_SPEED_Y

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Обработка столкновений мяча с верхней и нижней стенками
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y = -BALL_SPEED_Y

    # Обработка столкновений мяча с платформами
    if ball.colliderect(player_paddle) or ball.colliderect(puk_paddle):
        BALL_SPEED_X = -BALL_SPEED_X

    # Обработка столкновений мяча с левой и правой стенками (за пределами поля)
    if ball.left <= 0:
        puk_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        BALL_SPEED_X = -BALL_SPEED_X
    elif ball.right >= WIDTH:
        player_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        BALL_SPEED_X = -BALL_SPEED_X

# Функция для управления платформой игрока
def player_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED

def puk_movement():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and puk_paddle.top > 0:
        if puk_paddle.top < ball.y:
            puk_paddle.y += PADDLE_SPEED
    if keys[pygame.K_DOWN] and puk_paddle.bottom < HEIGHT:
        if puk_paddle.bottom > ball.y:
            puk_paddle.y -= PADDLE_SPEED

# Функция для управления платформой оппонента
# def opponent_movement():
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_w] and opponent_paddle.top > 0:
#     # if opponent_paddle.top < ball.y:
#         opponent_paddle.y += PADDLE_SPEED
#     if keys[pygame.K_s] and opponent_paddle.bottom < HEIGHT:
#     # if opponent_paddle.bottom > ball.y:
#         opponent_paddle.y -= PADDLE_SPEED

# Основной цикл игры
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_movement()
    puk_movement()
    update()
    draw_elements()
    pygame.display.flip()
    clock.tick(60)

    # Проверка счета игрока и оппонента
    if player_score >= 5 or puk_score >= 5:
        print("УСЕ КАНЕЦ")
        restart = input("ХОТИТЕ ПРОДОЛЖИТЬ??? (yes/no): ").lower()
        if restart == "yes":
            # Сброс счета и параметров игры
            player_score = 0
            puk_score = 0
            ball.center = (WIDTH // 2, HEIGHT // 2)
            BALL_SPEED_X = 6  # Вернуть скорость мяча в исходное состояние
            BALL_SPEED_Y = 6
        else:
            running = False

# Завершение игры
# pygame.quit()
# running = True
# clock = pygame.time.Clock()
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     player_movement()
#     opponent_movement()
#     update()
#     draw_elements()
#     pygame.display.flip()
#     clock.tick(60)

#     # Проверка счета игрока и оппонента
#     if player_score >= 5 or opponent_score >= 5:
#         print("ВСЕ КАНЕЦ")
#         restart = input("ВЫ ХОТИТЕ ЗАВЕРШИТЬ ИГРУ? (ДА!/НЕТ): ").lower()
#         if restart == "yes":
#             # Сброс счета и параметров игры
#             player_score = 0
#             opponent_score = 0
#             ball.center = (WIDTH // 2, HEIGHT // 2)
#             BALL_SPEED_X = abs(BALL_SPEED_X)  # Вернуть направление движения мяча в исходное состояние
#             BALL_SPEED_Y = abs(BALL_SPEED_Y)
#         else:
#             running = False

# Завершение игры
# pygame.quit()
# def initialize_game():
#     pygame.init()
# def update_score(player_score, opponent_score):
#     # Ваш код обновления счета здесь
#     pass
# def check_win_condition(player_score, opponent_score):
#     return player_score == 5 or opponent_score == 5
# def main_game_loop():
#     player_score = 0
#     opponent_score = 0
#     running = True

#     while running:

#      if check_win_condition(player_score, opponent_score):
#         print("ВСЕ КАНЕЦ")
#         restart = input("ВЫ ХОТИТЕ ЗАВЕРШИТЬ ИГРУ? (ДА!/НЕТ): ").lower()
#         if restart == "yes":
#             player_score = 0
#             opponent_score = 0
#             continue  # Начать новую игру
#         else:
#             running = False

# # Функция завершения игры
# def quit_game():
#     pygame.quit()

# # Основной блок программы
# if __name__ == "__main__":
#     initialize_game()
#     main_game_loop()


player_movement()
puk_movement()
    # player_two()
update()
draw_elements()
pygame.display.flip()
clock.tick(60)

# Завершение игры
pygame.quit()
