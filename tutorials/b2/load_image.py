import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600))
screen_rect = screen.get_rect()
image = pg.image.load('spaceship.png').convert()
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    screen.blit(image, screen_rect.center)
    pg.display.update()
