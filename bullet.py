from turtle import Screen
import pygame

class Bullet(pygame.sprite.Sprite): #створюємо новий клас для кульки 
    def __init__(self, screen, ship): 
        super(Bullet, self).__init__() 
        self.screen = screen
        self.rect = pygame.Rect (0, 0, 2, 12) #розмір кульки
        self.color = 34, 171, 76#колір кульки
        self.speed = 4.5 #швидкість зміни положення кульки
        self.rect.centerx = ship.rect.centerx 
        self.rect.top = ship.rect.top 
        self.y = float (self.rect.y) 

    #промальовуємо кульку 
    def update (self):
        self.y -= self.speed 
        self.rect.y = self.y 

    def draw_bullet (self):
        #малюємо кулю на екрані
        pygame.draw.rect(self.screen, self.color, self.rect) 