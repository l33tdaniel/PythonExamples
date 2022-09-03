import pygame

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800,400), pygame.RESIZABLE)
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()

while True:
    screen.fill((0, 20, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    mainClock.tick(60)