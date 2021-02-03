import pygame
from bomb import Bomb


class Player():
    def __init__(self, ip, name, x, y, color, game):
        self.ip = ip 
        self.name = name
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.color = color
        self.vel = 10
        self.bomb_cap = 1
        self.bombs = []
        self.exp_range = 1
        self.can_throw =False
        self.can_kick = False
        self.games_won = 0
        self.game = game
        self.load()

    def load(self):
        self.sprite = self.load().convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(self, win):
        win.blit(self.sprite,self.rect)

    def place(self, x, y):
        if len(self.bombs) <= self.bomb_cap:
            x = self.x
            y = self.y
            self.bombs.append(Bomb(self.centerx, self.centery, self.color, self.exp_range))

        
    def move(self, x, y):
        if x == 1:
            self.rect.centerx += 5
        if x == -1:
            self.rect.centerx -= 5  
        if y == 1:
            self.rect.centery += 5
        if y == -1:
            self.rect.centery -= 5
    
    def get_ip(self):
        return self.ip

    def get_name(self):            
        return self.name