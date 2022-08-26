import pygame


WIDTH = 1000
HEIGHT = 1000

colors = {
    "BLUE": (0,0,255),
    "RED": (255,0,0),
    "GREEN": (0,255,0),
    "BLACK": (0,0,0),
    "WHITE": (255,255,255)
}

def setup():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    return screen

def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

    return True

def draw_elements(screen, list, color):
    for e in list:
        pygame.draw.circle(screen, color, (e.x, e.y), 5, 0)

def update(screen, ecosystem):
    screen.fill(colors["BLACK"])
    draw_elements(screen, ecosystem.organisms, colors["GREEN"])
    draw_elements(screen, ecosystem.foods, colors["RED"])
    pygame.display.update()

def stop():
    pygame.quit()