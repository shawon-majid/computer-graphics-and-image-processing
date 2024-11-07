


def bresenham_line(x1, y1, x2, y2):

    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    step_x = 1 if x1 < x2 else -1
    step_y = 1 if y1 < y2 else -1

    x = x1
    y = y1

    points.append((x, y))

    if dy < dx:
        
        # if |m| < 1, the line is more horizontal
        # so need to change x by 1 step
        # m = dy / dx (rise over run)

        d = 2 * dy - dx # base case   
        for _ in range(dx):
            if d  >= 0:
                d += 2 * (dy - dx)
                y += step_y
            else:
                d += 2 * dy
            
            x += step_x

            points.append((x, y))
    else:
        # if |m| > 1, the line is more vertical
        # so need to change y by 1 step
        # m = dy / dx (rise over run)

        d = 2 * dx - dy

        for _ in range(dy):
            if d >= 0:
                d += 2 * (dx - dy)
                x += step_x
            else:
                d += 2 * dx

            y += step_y

            points.append((x, y))

    return points












