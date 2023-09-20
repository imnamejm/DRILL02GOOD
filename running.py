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

def run_circle():
    print('CIRCLE')
    cx , cy, r = 400, 300, 200
    for deg in range(0, 360, 5):
        x = cx + r * math.cos(deg / 360 * 2 * math.pi)
        y = cy + r * math.sin(deg / 360 * 2 * math.pi)
        rander_all(x, y)

def run_rectangle():
    print('RECTANGLE')
    
#botton line
    for x in range(50, 750,10):
        rander_all(x, 90)
#top line
    for x in range (750,50-1,-10):
        rander_all(x, 550)
        
    


while True:
    run_circle()
    run_rectangle()
    break
