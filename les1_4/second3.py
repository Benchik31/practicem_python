import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра с коллизиями и стрелами")

background = pygame.image.load("lesson4/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(0, HEIGHT)
        self.speed = 3

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.rect.x = 0
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > WIDTH:
            self.kill()

player = Player()
enemy1 = Enemy()
enemy2 = Enemy()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy1)
all_sprites.add(enemy2)

enemies = pygame.sprite.Group()
enemies.add(enemy1)
enemies.add(enemy2)

bullets = pygame.sprite.Group()

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    keys = pygame.key.get_pressed()

    player.update(keys)

    enemies.update()

    bullets.update()

    for bullet in bullets:
        enemy_hit = pygame.sprite.spritecollide(bullet, enemies, True)
        if enemy_hit:
            bullet.kill()
            for enemy in enemy_hit:
                enemy.kill()

    screen.blit(background, (0, 0))

    all_sprites.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
