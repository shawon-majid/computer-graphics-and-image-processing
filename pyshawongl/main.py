
from line_drawing import bresenham_line
from circle_drawing import bresenham_circle, midpoint_circle
from shawonGL import pygameSetup

def main():

    shapes = [] 
    
    shapes.append((bresenham_circle(0, 0, 22), (1, 0, 0)))
    shapes.append((midpoint_circle(0, 0, 20), (1, 1, 1)))
    shapes.append((bresenham_line(-20, -20, 20, 20), (0, 1, 0)))
    shapes.append((bresenham_line(-20, 20, 20, -20), (0, 1, 0)))


    



    pygameSetup(shapes)






if __name__ == "__main__":
    main()
