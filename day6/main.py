from utils.grid import Grid2D
from utils.point import Point
from utils.direction import Direction

file = "ex.txt"

def p1():
    lines = []
    with open(file) as f:
        for l in f:
            lines.append(list(l.strip()))

    grid = Grid2D(lines[::-1])
    current_point = Point(*grid.find_all("^")[0])

    print(grid)

    max_x, max_y = grid.size()
    visited = set()
    current_direction = Direction.EAST

    while 0 <= current_point.x < max_x and 0 <= current_point.y < max_y:
        visited.add(current_point)
        next_point = current_point + current_direction.point()

        print(current_point, current_direction.point(), next_point)
        print(grid[next_point.x, next_point.y])
        while (grid[next_point.x, next_point.y] != "." and
               grid[next_point.x, next_point.y] is not None):
            current_direction = current_direction.left()
            next_point = current_point + current_direction.point()

        current_point = next_point

    return len(visited)

print(p1())



