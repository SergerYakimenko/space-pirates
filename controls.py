
import pygame, sys
from ship import Ship
from bullet import Bullet 
from ino import Ino 
import time

def events(screen, ship, bullets): 
#обробка подій
    for event in pygame.event.get(): #перебираються всі події в грі, збираємо всі події користувача
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_x: # кнопка праворуч
                ship.mright = True 
            if event.key == pygame.K_z: #кнопка ліворуч
                ship.mleft = True
            elif event.key == pygame.K_SPACE: #якщо натискається клавіша пробіл
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)  
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_x:
                ship.mright = False
       
            elif event.key == pygame.K_z:
                ship.mleft = False
def update (bg_color, screen, stats, sc,  ship, inos, bullets): #функція яка відповідає за поновлення екрану (колір, екран, корабель, пришельці, контейнер з кульками) 
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    inos.draw (screen) 
    pygame.display.flip()

    #обновлять позиції куль, та видаляти кулі, що вийшли за межі екрану для економії памяті та ресурсів компютера
def update_bullets(screen, stats, sc, inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: #якщо низ кулі на рівні менше 0 
            bullets.remove(bullet)# ми видяляємо цю кулю
    
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)  #створюємо функцію яка перевіряє колізій (перетинання обєктів гри куль та прибульців) 2 тру означає що треба видаляти і кулю і пришельця

    if collisions: #в разі конфлікту збільшуємо рахунок на 10
        for inos in collisions.values(): #для підрахунку всіх вбитих пирбульців великою кулькою
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score (stats, sc)
        sc.image_ships()


    #перевірка чи встановлено рекорд з вбивством чергового пришельця


    if len(inos) == 0:
        bullets.empty() 
        create_army(screen, inos)


def ship_kill(stats, screen, sc, ship, inos, bullets): #cтолкновение корабля і армії
    if stats.ships_left > 0: 
        stats.ships_left-=1
        sc.image_ships()
        inos.empty()
        bullets.empty()
        create_army (screen, inos)
        ship.create_ship() 
        time.sleep(2)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, sc, ship, inos, bullets): #поновлює позиції проибульців
    inos.update()
    if pygame.sprite.spritecollideany(ship, inos):
        ship_kill(stats, screen, sc, ship, inos, bullets)
   
    inos_check(stats, screen, sc, ship, inos, bullets)

def inos_check(stats, screen, sc, ship, inos, bullets):
    # перевірка чи пройшли прибульці
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom: #якщо нижня частина прибульця торкнулась нижного краю екрану
            ship_kill(stats, screen, sc, ship, inos, bullets)
            break



    
def create_army(screen, inos): #створюємо армію прибульців
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((1100-2*ino_width)/ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100-2*ino_height)/ino_height)

    for row_number in range(number_ino_y-9):

        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x #відстань між прибульцями
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


def check_high_score(stats, sc): #перевірка нових рекордів
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score() 
        with open ("hascor.txt", "w") as f: 
            f.write(str(stats.high_score))

