import pygame.font
from ship import Ship
from pygame.sprite import Group 

class Scores(): #вивод іргової інформації щодо рекорду та рахунку
    def __init__(self, screen, stats) -> None: 
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (34, 171, 76)#шрифт для виведення інформації
        self.font = pygame.font.SysFont(None, 36) 
        self.image_score()                  
        self.image_high_score()# функція відповідальна за рекорд
        self.image_ships()

    

    def image_score (self): #перетворює текст рахунку в графічне зображення 
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0)) 
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40 
        self.screen_rect.top = 20 


    #метод відповідальний за рекорд 
    def image_high_score(self): #претворює рекорд в графічне зображення
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top + 20
    
    def image_ships(self): #кількість життів
        self.ships = Group()
        for ship_number in range (self.stats.ships_left):
            ship = Ship(self.screen)

            ship.rect.x = 15 + ship_number * ship.rect.width
            ship.rect.y = 20
            self.ships.add(ship)




        # для відображення рахунку, вивод рахунку на екран створюємо метод шов скоре
    def show_score (self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)


       
        

