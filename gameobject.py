import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, ip, name, x, y, width) -> None:
        super().__init__()
        self.ip = ip 
        self.name = name
        self.x = x
        self.y = y
        self.width = width