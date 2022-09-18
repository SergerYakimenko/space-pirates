import pygame

class Ino(pygame.sprite.Sprite):  #ствоюємо підклас інопланетянина 
    def __init__(self, screen): #ініціалізуємо початкову позицію
        super(Ino, self).__init__() 
        self.screen = screen #
        self.image = pygame.image.load('images/prishelez.png')
        self.rect = self.image.get_rect()        
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def draw(self): # відмалоьвання інопланетянина
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        self.y += 0.03
        self.rect.y =self.y
       

