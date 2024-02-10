import matplotlib.pyplot as plt
import numpy as np
plt.title("Bresenham Algorithm")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

def bresenham(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0

    if abs(dy) < abs(dx): # 0 < m < 1
        if x0 > x1:
            x0, y0, x1, y1 = x1, y1, x0, y0

        yi = 1
        if dy < 0:
            yi = -1
            dy = -dy
        D = 2 * dy - dx
        y = y0

        for x in range(x0, x1 + 1):
            points.append((x, y))
            if D > 0:
                y = y + yi
                D = D - 2 * dx
            D = D + 2 * dy

    else: 
        if y0 > y1:
            x0, y0, x1, y1 = x1, y1, x0, y0
        xi = 1
        if dx < 0:
            xi = -1
            dx = -dx
        D = 2 * dx - dy
        x = x0

        for y in range(y0, y1 + 1):
            points.append((x, y))
            if D > 0:
                x = x + xi
                D = D - 2 * dy
            D = D + 2 * dx


    return points

def drawLineForHighM(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2 * dx - dy
    x = x0

    for y in range(y0, y1 + 1):
        points.append((x, y))
        if D > 0:
            x = x + xi
            D = D - 2 * dy
        D = D + 2 * dx

    return points

def main():
    x0, y0 = 1, 1
    x1, y1 = 8, 4

    points = []

    points = bresenham(x0, y0, x1, y1)
    
    x_values, y_values = zip(*points)

    plt.plot(x_values, y_values, marker='o', label= abs(y1 - y0) < abs(x1 - x0) and 'm < 1' or 'm > 1'  )
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenham\'s Line Drawing Algorithm')
    plt.grid(True)
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()