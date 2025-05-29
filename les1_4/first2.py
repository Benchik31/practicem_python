import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Анимация фигур")

WHITE = (255, 255, 255)

shapes = [
    {"type": "square", "x": 50, "y": 100, "size": 50, "dx": 5, "color": (255, 0, 0)},
    {"type": "rectangle", "x": 50, "y": 200, "width": 100, "height": 50, "dx": 4, "color": (0, 255, 0)},
    {"type": "circle", "x": 50, "y": 300, "radius": 30, "dx": 6, "color": (0, 0, 255)},
    {"type": "triangle", "x": 50, "y": 400, "size": 60, "dx": 3, "color": (255, 255, 0)}
]

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for shape in shapes:
                if shape["type"] == "square" and shape["x"] <= mouse_x <= shape["x"] + shape["size"] and shape["y"] <= mouse_y <= shape["y"] + shape["size"]:
                    shape["color"] = random_color()
                elif shape["type"] == "rectangle" and shape["x"] <= mouse_x <= shape["x"] + shape["width"] and shape["y"] <= mouse_y <= shape["y"] + shape["height"]:
                    shape["color"] = random_color()
                elif shape["type"] == "circle" and (mouse_x - shape["x"])**2 + (mouse_y - shape["y"])**2 <= shape["radius"]**2:
                    shape["color"] = random_color()
                elif shape["type"] == "triangle":
                    x1, y1 = shape["x"], shape["y"]
                    x2, y2 = shape["x"] - shape["size"] // 2, shape["y"] + shape["size"]
                    x3, y3 = shape["x"] + shape["size"] // 2, shape["y"] + shape["size"]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
                    area1 = abs(mouse_x * (y2 - y3) + x2 * (y3 - mouse_y) + x3 * (mouse_y - y2)) / 2
                    area2 = abs(x1 * (mouse_y - y3) + mouse_x * (y3 - y1) + x3 * (y1 - mouse_y)) / 2
                    area3 = abs(x1 * (y2 - mouse_y) + x2 * (mouse_y - y1) + mouse_x * (y1 - y2)) / 2
                    if area == area1 + area2 + area3:
                        shape["color"] = random_color()

    for shape in shapes:
        if shape["type"] == "square":

            pygame.draw.rect(screen, shape["color"], (shape["x"], shape["y"], shape["size"], shape["size"]))
            shape["x"] += shape["dx"]
            if shape["x"] <= 0 or shape["x"] + shape["size"] >= WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()
        elif shape["type"] == "rectangle":

            pygame.draw.rect(screen, shape["color"], (shape["x"], shape["y"], shape["width"], shape["height"]))
            shape["x"] += shape["dx"]
            if shape["x"] <= 0 or shape["x"] + shape["width"] >= WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()
        elif shape["type"] == "circle":

            pygame.draw.circle(screen, shape["color"], (shape["x"], shape["y"]), shape["radius"])
            shape["x"] += shape["dx"]
            if shape["x"] - shape["radius"] <= 0 or shape["x"] + shape["radius"] >= WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()
        elif shape["type"] == "triangle":
            x1, y1 = shape["x"], shape["y"]
            x2, y2 = shape["x"] - shape["size"] // 2, shape["y"] + shape["size"]
            x3, y3 = shape["x"] + shape["size"] // 2, shape["y"] + shape["size"]
            pygame.draw.polygon(screen, shape["color"], [(x1, y1), (x2, y2), (x3, y3)])
            shape["x"] += shape["dx"]
            if shape["x"] - shape["size"] // 2 <= 0 or shape["x"] + shape["size"] // 2 >= WIDTH:
                shape["dx"] = -shape["dx"]
                shape["color"] = random_color()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
