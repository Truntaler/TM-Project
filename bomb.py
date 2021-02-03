import pygame

class Bomb():
    def __init__(self, x, y, r = 10, color, exp_range):
        self.x = x
        self.y = y
        self.color = color
        self.explosion = Explosion()
        self.exp_range = exp_range
        self.time =  2.5 
        self.load()
    
    def load():
        self.sprite = self.load().convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(win):
        win.blit(self.sprite,self.rect)

    def detonate():
        self.explosion.update()
