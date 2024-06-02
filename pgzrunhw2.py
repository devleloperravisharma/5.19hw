import pgzrun
from random import randint 

WIDTH = 300

HEIGHT = 300
'```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````'
def draw():
    width = WIDTH
    height = HEIGHT-200

    radius = 150
    Width = WIDTH


    r = 255
    g = 0
    b = randint(100,255)

    
    for drawing in range(30):
        drawings = Rect((0,0), (width, height))
        drawings.center = (150, 150)
        screen.draw.rect(drawings, (r,g,b))




        width -= 10
        height += 10
        r -= 5
        g += 5

    r = 255
    g = 192
    b = randint(202,203)

    #why isn't the circle class working ?
 
    for make in range(30):
        draws = Rect((0,0), (radius, height))
        draws.center = (150, 150)
        screen.draw.circle((150,150), radius, (r, g, b))


        radius -= 10
        width -= 10
        height += 10
        r -= 5

pgzrun.go()

