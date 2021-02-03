import pygame


class Explosion():
    def __init__(self,x,y, exp_range):
        self.x = x
        self.y = y
        self.exp_range = exp_range
        self.time = 2

    def load():
        self.sprite = self.load().convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(win):
        win.blit(self.sprite,self.rect)
