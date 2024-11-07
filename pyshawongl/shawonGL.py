import pygame
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

figures = []

# Set up the OpenGL environment
def myInit():
    # Set background color
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(5.0)  # Set point size
    glOrtho(-54, 51, -54, 51, -1, 1)

def displayPoints(color=(0.2, 0.5, 0.4)):
    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT)

    

    # x-axis
    glBegin(GL_LINES)
    glVertex2f(-54, 0)
    glVertex2f(51, 0)
    glEnd()

    # y-axis
    glBegin(GL_LINES)
    glVertex2f(0, -54)
    glVertex2f(0, 54)
    glEnd()

    # Center
    # glBegin(GL_POINTS)
    # glVertex2f(0, 0)
    # glEnd()

    # Rectangle
    # glBegin( GL_QUADS )
    # glVertex2f( 100.0, 100.0 )
    # glVertex2f( 300.0, 100.0 )
    # glVertex2f( 300.0, 200.0 )
    # glVertex2f( 100.0, 200.0 )
    # glEnd()

    # Triangle
    # glBegin(  GL_TRIANGLE_STRIP )
    # glVertex2f( 10.0, 21.0 )
    # glVertex2f( 30.0, 21.0 )
    # glVertex2f( 30.0, 31.0 )
    # glEnd()

    for pixels, colors in figures:
        # Set the drawing color
        glColor3f(colors[0], colors[1], colors[2])
        for pixel in pixels:
            # Draw a pixel(x,y)
            if len(pixel) == 2:
                glBegin(GL_POINTS)
                glVertex2f(pixel[0], pixel[1])
                glEnd()
            else:
                # Logic for striped line(x1, y1, x2, y2, isStriped)
                if len(pixel) == 5:
                    glLineStipple(1, 0xAAAA)
                    glEnable(GL_LINE_STIPPLE)
                else:
                    glDisable(GL_LINE_STIPPLE)

                # Draw a line P1(x1,y1) & P2(x2,y2)
                glBegin(GL_LINES)
                glVertex2f(pixel[0], pixel[1])
                glVertex2f(pixel[2], pixel[3])
                glEnd()
    glFlush()

def pygameSetup(figure):
    global figures
    figures = figure

    # Initialize Pygame
    pygame.init()

    # Set up the display window
    width, height = 500, 500
    window = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("OpenGL with Pygame")

    # Set up the OpenGL environment
    myInit()

    # Frame rate control
    clock = pygame.time.Clock()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display points
        displayPoints()

        # Update the screen using double buffering
        pygame.display.flip()

        # Control the frame rate (60 frames per second)
        clock.tick(60)

    # Quit Pygame
    pygame.quit()