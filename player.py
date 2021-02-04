import pygame
from bomb import Bomb
from gameobject import GameObject


class Player(GameObject):
    def __init__(self, x, y, width, height, ip, name, color, game):
        super().__init__(x, y, width, height)
        self.ip = ip 
        self.name = name
        self.color = color
        self.vel = 10
        self.bomb_cap = 1
        self.bombs = []
        self.exp_range = 1
        self.can_throw =False
        self.can_kick = False
        self.games_won = 0
        self.game = game
        self.load("./test_bg.jpg")

    
    def place(self, x, y):
        if len(self.bombs) <= self.bomb_cap:
            x = self.x
            y = self.y
            self.bombs.append(Bomb(self.rect.centerx, self.rect.centery, self.color, self.exp_range))

        
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

