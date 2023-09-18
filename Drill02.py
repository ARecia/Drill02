from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
    x=400
    while (x<800,):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)

        x=x+2
        delay(0.01)
        if x == 800:
            break

    y=90
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(800,y)

        y=y+2
        delay(0.01)
        if y == 600:
            break
    x=800
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 600)

        x=x-2
        delay(0.01)
        if x == 0:
            break
    y=600
    while(y>60):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0, y)

        y=y-2
        delay(0.01)
        if y == 60:
            break

    x=0
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)

        x = x + 2
        delay(0.01)




