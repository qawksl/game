import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
BLOCK_SIZE = 20
SPEED = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра Змейка")

snake = [(200, 200), (220, 200), (240, 200)]
food = (400, 300)
direction = (1, 0)
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    # Двигаем змейку
    head = snake[0]
    new_head = (head[0] + direction[0] * BLOCK_SIZE, head[1] + direction[1] * BLOCK_SIZE)
    snake.insert(0, new_head)

    # Проверяем столкновение с едой
    if snake[0] == food:
        food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE, random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
        score += 1
    else:
        snake.pop()

    # Проверяем столкновение со стеной или самой собой
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
        snake[0][1] < 0 or snake[0][1] >= HEIGHT or
        snake[0] in snake[1:]):
        print("Игра окончена! Ваш счет:", score)
        pygame.time.delay(2000)
        snake = [(200, 200), (220, 200), (240, 200)]
        food = (400, 300)
        direction = (1, 0)
        score = 0

    # Рисуем все
    screen.fill(BLACK)
    for pos in snake:
        pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
    font = pygame.font.Font(None, 36)
    text = font.render("Счет: " + str(score), 1, WHITE)
    screen.blit(text, (10, 10))
    pygame.display.flip()

    # Ограничиваем частоту кадров
    pygame.time.Clock().tick(SPEED)
