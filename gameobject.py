import pygame


class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def load(self, path):
        self.sprite = pygame.image.load(path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(self, win):
        win.blit(self.sprite,self.rect)
