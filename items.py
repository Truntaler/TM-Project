from player import Player
from gameobject import GameObject
import pygame


"""

increases the speed of the player

"""
class ItemVel(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y,100,100)
        self.load()
    
    def upgrade(self, player):
        player.vel += 1



"""

increases the bomb capacity 


"""



class ItemBombAmount(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y,100,100)
        self.load()
    
    def upgrade(self, player):
        player.bomb_cap += 1




"""

increases the range for each bomb


"""



class ItemBombRangeBGameObjectombRange():
    def __init__(self, x, y):
        super().__init__(x,y,100,100)
        self.load()
    
    def upgrade(self, player):
        player.exp_range += 1



"""

allows the player to throw Bombs


"""



class ItemBombThrowing(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y, 100, 100)
        self.load()
    
    def upgrade(self, player):
        player.can_throw = True



"""

allows the player to kick Bombs


"""



class ItemBombKicking(GameObject):
    def __init__(self, x, y):
        super().__init__(x,y,100,100)
        self.load()
    
    def upgrade(self, player):
        player.can_kick = True

class ItemBombThrowing():
    def __init__(self, x, y, width, height):
        super().__init__(x,y,width,height)
        self.load()
    
    def upgrade(self, player):
        player.can_throw = True
    
    def load(self):
        self.sprite = self.pygame.load().convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(self,win):
        win.blit(self.sprite,self.rect)