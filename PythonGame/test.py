import pygame as pg
print(pg.ver)

if pg.font is None:
    print("The font Module is not available")
    exit()
    
backgroung_image_filename = 'C:\\Users\\朱远宏\\Desktop\\python.png'
mouse_image_filename ='C:\\Users\\朱远宏\\Desktop\\1.png'

from sys import exit

pg.init()
screen = pg.display.set_mode((640,480),0,32)
pg.display.set_caption("Hello world!")
background = pg.image.load(backgroung_image_filename)
mouse_cursor = pg.image.load(mouse_image_filename)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    
    screen.blit(background,(0,0))
    
    x,y = pg.mouse.get_pos()
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    screen.blit(mouse_cursor,(x,y))
    
    pg.display.update()