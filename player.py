import pygame

class Player():
    def __init__(self, ip, name, x, y, color):
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
        self.can_throw =False
        self.can_kick = False
        self.games_won = 0
        self.game = Game
        self.load()

    def load():
        self.sprite = self.load().convert_alpha()
        self.rect = self.sprite.get_rect(topleft=(self.x,self.y))

    def update(win):
        win.blit(self.sprite,self.rect)
        
    def move():
        for event in pygame.get.event():
            if event.type == pygame.KEYDOWN:
                if event.key = pygame.K_LEFT:
                    self.rect.centerx -= 5
                if event.key = pygame.K_RIGHT:
                    self.rect.centerx += 5  
                if event.key = pygame.K_DOWN:
                    self.rect.centery += 5
                if event.key = pygame.K_UP:
                    self.rect.centery -= 5 
            
