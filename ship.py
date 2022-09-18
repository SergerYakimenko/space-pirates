import pygame 

from pygame.sprite import Sprite 

class Ship(Sprite):
    

    def __init__(self,screen):
        # ініціалізація корабля
        super (Ship, self).__init__()#під час іонізації підтягуємо в клас все що було в батьківському класі
        self.screen = screen
        self.image = pygame.image.load("images/korabl.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float (self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):#функція для малювання корабля 
        
        self.screen.blit(self.image, self.rect)
    
    def update_ship (self):
         #поновлення позиції корабля
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.5 
        if self.mleft and self.rect.left > 0:
            self.center -= 0.5 
        self.rect.centerx = self.center 


    def create_ship(self): #початкове роозміщення корабля
        self.center = self.screen_rect.centerx


        
