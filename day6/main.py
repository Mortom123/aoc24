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

    max_x, max_y = grid.size()
    visited = set()
    current_direction = Direction.EAST

    while 0 <= current_point.x < max_x and 0 <= current_point.y < max_y:
        visited.add(current_point)
        next_point = current_point + current_direction.point()

        while grid[next_point.x, next_point.y] == "#":
            current_direction = current_direction.left()
            next_point = current_point + current_direction.point()

        current_point = next_point

    return len(visited)

def p2():
    lines = []
    with open(file) as f:
        for l in f:
            lines.append(list(l.strip()))

    grid = Grid2D(lines[::-1])
    current_point = Point(*grid.find_all("^")[0])

    max_x, max_y = grid.size()
    visited_list = []

    current_direction = Direction.EAST

    while 0 <= current_point.x < max_x and 0 <= current_point.y < max_y:
        visited_list.append((current_point, current_direction))

        next_point = current_point + current_direction.point()

        while grid[next_point.x, next_point.y] == "#":
            current_direction = current_direction.left()
            next_point = current_point + current_direction.point()

        current_point = next_point

    visited = set(visited_list)

    obstacles = 0
    total = len(visited_list)
    for i, (position, direction) in enumerate(visited_list):
        print(f"{i}/{total}")
        # Check if placing an obstacle at the next position would create a loop
        obstacle_position = position + direction.point()
        direction_with_obstacle = direction.left()
        position_with_obstacle = position
        visited_obstacle = visited.copy()
        print(len(visited_obstacle))

        while 0 <= position_with_obstacle.x < max_x and 0 <= position_with_obstacle.y < max_y:
            if (position_with_obstacle, direction_with_obstacle) in visited_obstacle:
                obstacles += 1
                break
            visited_obstacle.add((position_with_obstacle, direction_with_obstacle))
            next_position_with_obstacle = position_with_obstacle + direction_with_obstacle.point()

            while (grid[next_position_with_obstacle.x, next_position_with_obstacle.y] == "#"
                   or next_position_with_obstacle == obstacle_position):
                direction_with_obstacle = direction_with_obstacle.left()
                next_position_with_obstacle = next_position_with_obstacle + direction_with_obstacle.point()
            position_with_obstacle = next_position_with_obstacle

    return obstacles


print(p1())
print(p2())




