import pygame

mainClock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((800,400), pygame.RESIZABLE)
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()


test_surface = pygame.Surface((100,200))
test_surface.fill('Yellow')

while True:
    
    screen.fill((0, 20, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #blit = block image transfer
    screen.blit(test_surface,(20,0))



    pygame.display.update()
    mainClock.tick(60)