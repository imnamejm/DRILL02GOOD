import math

from pico2d import*

open_canvas()

grass=load_image('grass.png')
character = load_image('character.png')

def rander_all(x, y):
    clear_canvas.now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.1) 


def run_rectangle():
    print('RECTANGLE')
    
#botton line
    for x in range(50, 750,10):
        rander_all(x, 90)
#top line
    for x in range (750,50-1,-10):
        rander_all(x, 550)
#left line
    for y in range (550,90-1,-10):
        rander_all(50, y)    
#right line
    for x in range (90,550,10):
        rander_all(750, y)
        
while True:
    run_circle()
    run_rectangle()
    break
