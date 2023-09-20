import math

from pico2d import*

open_canvas()

grass=load_image('grass.png')
character = load_image('character.png')

def run_circcle():
    clear_canvas.now()
    grass.draw_now(400,30)
    character.draw_now(400,9)
    delay(1)
    print('CIRCLE')
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_circle()
    run_rectangle()
    break
