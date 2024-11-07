
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midpoint_circle(cx, cy, r):

    points = []

    x = 0
    y = r
    d = 1 - r

    while x <= y:
        
        points.append((cx + x, cy + y))
        points.append((cx - x, cy + y))
        points.append((cx + x, cy - y))
        points.append((cx - x, cy - y))
        points.append((cx + y, cy + x))
        points.append((cx - y, cy + x))
        points.append((cx + y, cy - x))
        points.append((cx - y, cy - x))
        
        # yMid = y + 0.5
        # if x*x + yMid*yMid > r*r: # outside the circle
            # y += 1

        # we can change this to more efficient calculation
        # let's set d = -r

        if d < 0: 
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1    

    return points


        


def bresenham_circle(cx, cy, r):

    points = []

    x = 0
    y = r
    d = 3 - 2 * r

    while x <= y:
        points.append((cx + x, cy + y))
        points.append((cx - x, cy + y))
        points.append((cx + x, cy - y))
        points.append((cx - x, cy - y))
        points.append((cx + y, cy + x))
        points.append((cx - y, cy + x))
        points.append((cx + y, cy - x))
        points.append((cx - y, cy - x))


        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1

        x += 1

    return points