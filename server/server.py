import socket

class GameObject:
    def __init__(self,x,y,w,h,c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h 
        self.c = c



class Player(GameObject):
    def __init__(self, x, y, w, h, c):
        super().__init__(x, y, w, h, c)