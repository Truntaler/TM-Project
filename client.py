import pygame
from player import Player


pygame.init()
screen = pygame.display.set_mode((1440, 810))
clock = pygame.time.Clock()

screen_width, screen_height = pygame.display.get_surface().get_size()

test_p = Player(100,100,1000,800,"irgendeine ip","Name",(0,0,0),"Game")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    test_p.update(screen)
    pygame.display.update()
    clock.tick(60)