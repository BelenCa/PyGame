import pygame as py

pg.init()

pantalla = pg.display.set_mode((600, 400))
pg.display.set_caption("Hola")

game_over = False

while not game_over:
    #Gestion de eventos
    for evento in pg.event.get():
        pass

    #Gestion del estado

    pantalla.fill((0,255,0))
    pg.display.flip()