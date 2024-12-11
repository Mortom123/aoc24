from typing import Set, Tuple
from utils.grid import Grid2D
from utils.point import Point
from utils.direction import Direction

file = "data.txt"

def guard_route(limits: Tuple[int, int], starting_point: Point, starting_direction: Direction, obstacles: Set[Point]):
    max_x, max_y = limits
    circle_check = set()
    visited = []
    current_point = starting_point
    current_direction = starting_direction

    while 0 <= current_point.x < max_x and 0 <= current_point.y < max_y:
        if (current_point, current_direction) in circle_check:
            return visited, True
        visited.append((current_point, current_direction))
        circle_check.add((current_point, current_direction))

        next_point = current_point + current_direction.point()

        while next_point in obstacles:
            current_direction = current_direction.left()
            next_point = current_point + current_direction.point()

        current_point = next_point

    return visited, False

def p1():
    lines = []
    with open(file) as f:
        for l in f:
            lines.append(list(l.strip()))

    grid = Grid2D(lines[::-1])
    starting_point = Point(*grid.find_all("^")[0])
    starting_direction = Direction.EAST
    obstacles = set(Point(*i) for i in grid.find_all("#"))
    limits = grid.size()

    visited, _ = guard_route(limits, starting_point, starting_direction, obstacles)
    return len(set(i[0] for i in visited))

def p2():
    lines = []
    with open(file) as f:
        for l in f:
            lines.append(list(l.strip()))

    grid = Grid2D(lines[::-1])
    starting_point = Point(*grid.find_all("^")[0])
    starting_direction = Direction.EAST
    obstacles = set(Point(*i) for i in grid.find_all("#"))
    limits = grid.size()

    visited, _ = guard_route(limits, starting_point, starting_direction, obstacles)
    visited_points = set(i[0] for i in visited)

    extra_obstacles = 0

    max_x, max_y = limits
    for x in range(max_x):
        for y in range(max_y):
            if grid[x,y] != ".":
                continue
            p = Point(x, y)
            if p not in visited_points:
                continue

            tmp_obstacles = obstacles.copy()
            tmp_obstacles.add(p)
            _, is_loop = guard_route(limits, starting_point, starting_direction, tmp_obstacles)

            if is_loop:
                extra_obstacles += 1

    return extra_obstacles

print(p1())
print(p2())



