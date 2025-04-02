import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движение фона")

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

background_x = 0
background_y = 0
background_speed = 5

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        background_x += background_speed
    if keys[pygame.K_RIGHT]:
        background_x -= background_speed
    if keys[pygame.K_UP]:
        background_y += background_speed
    if keys[pygame.K_DOWN]:
        background_y -= background_speed

    screen.blit(background, (background_x, background_y))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
