import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Якубов Бинягу Олегович")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
LIGHT_BLUE = (173, 216, 230)
YELLOW = (255, 255, 0)

image_path = "image.png"
image = pygame.image.load(image_path)
image = pygame.transform.scale(image, (150, 150))

image_x, image_y = 50, 50
new_x, new_y = 400, 300

random_rects = []
for _ in range(5):
    rand_color = [random.randint(0, 255) for _ in range(3)]
    rand_rect = pygame.Rect(
        random.randint(0, WIDTH - 50),
        random.randint(0, HEIGHT - 50),
        random.randint(30, 150),
        random.randint(30, 150)
    )
    random_rects.append((rand_color, rand_rect))

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (100, 100), 50)

    pygame.draw.circle(screen, RED, (WIDTH // 4, HEIGHT * 3 // 4), 40, 15)

    pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 2), 100)

    pygame.draw.rect(screen, (0, 0, 255), (50, 400, 300, 200))

    for color, rect in random_rects:
        pygame.draw.rect(screen, color, rect)

    roof_top = (WIDTH // 2, HEIGHT // 2 - 150)
    roof_left = (WIDTH // 2 - 100, HEIGHT // 2 - 50)
    roof_right = (WIDTH // 2 + 100, HEIGHT // 2 - 50)
    pygame.draw.polygon(screen, BROWN, [roof_top, roof_left, roof_right])
    pygame.draw.rect(screen, (210, 180, 140), (WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 150))

    pygame.draw.rect(screen, (139, 69, 19), (WIDTH // 2 - 30, HEIGHT // 2 + 30, 60, 70))

    pygame.draw.rect(screen, LIGHT_BLUE, (WIDTH // 2 - 60, HEIGHT // 2 - 20, 40, 40))  # окно

    points = [(600, 100), (650, 120), (640, 200), (580, 220), (560, 150)]
    pygame.draw.lines(screen, (0, 0, 0), True, points, 3)

    screen.blit(image, (new_x, new_y))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
