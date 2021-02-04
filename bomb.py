import pygame
from explosion import Explosion

class Bomb():
    def __init__(self, x, y, width, height, color, exp_range):
        self.x = x
        self.y = y
        self.color = color
        self.explosion = Explosion()
        self.exp_range = exp_range
        self.time =  2.5 
        self.load()
    
    def load(self):
        self.sprite = self.pygame.load().convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(self,win):
        win.blit(self.sprite,self.rect)

    def detonate(self):
        self.explosion.update()
