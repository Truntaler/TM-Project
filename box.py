import random 
from gameobject import GameObject
from items import *

class Box(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 100, 100)
        self.item = self.select_item()
        self.items = [ItemVel(self.x,self.y),ItemBombAmount(self.x,self.y),ItemBombRange(self.x,self.y),
                      ItemBombThrowing(self.x,self.y), ItemBombKicking(self.x,self.y)]
        
        self.load("Hier muss Bildpfad rein!")

    def select_item(self):
        n = random.random()
        if n > 0.225:
            return random.choice(self.items)
