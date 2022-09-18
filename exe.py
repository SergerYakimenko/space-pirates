import pygame, controls  
from ship import Ship 
from pygame.sprite import Group 
                     
from stats import Stats
from scores import Scores

def run():  
    pygame.init()    
    screen = pygame.display.set_mode((1100,700))
    pygame.display.set_caption("Космичні пірати")
    bg_color = (0,0,0)#фоновий кольору для вікна
    ship = Ship(screen)
    bullets = Group() 
    inos = Group()   
    controls.create_army(screen, inos)
    stats = Stats()   
    sc = Scores(screen, stats)  



    while True: #головний цикл гри створюємо в функції run, обролюються всі дії користувача під час гри
        controls.events(screen, ship, bullets)
        if stats.run_game: #перевіряється умова наявності життів у грі
            ship.update_ship()
            
            controls.update(bg_color, screen, stats, sc, ship, inos, bullets) # поновлення екрану (колір, екран, статистика, життя, прибульці , корабель) 
            controls.update_bullets(screen, stats, sc, inos, bullets) #стирання куль, які вийшли за межі екрану 
            controls.update_inos(stats, screen, sc, ship, inos, bullets)

run()