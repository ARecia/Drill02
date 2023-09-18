from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
    x,y = 400, 90
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x+=2
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x,y)

        y+=2
        delay(0.01)

    while(x>0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x-=2
        delay(0.01)

    while(y>90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        y-=2
        delay(0.01)

    while(x<400):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)

        x+=2
        delay(0.01)

    radius = 270
    angle = 360
    while (angle>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400 + radius * math.cos(math.radians(angle))
        y= 300 + radius * math.sin(math.radians(angle))
        character.draw_now(x,y)

        angle-=1
        delay(0.01)







