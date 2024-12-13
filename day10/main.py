import numpy as np
file = "data.txt"

def bfs(grid, start_point, skip_visited=False):
    neighbors = [
        [-1, 0],
        [1, 0],
        [0, 1],
        [0, -1]
    ]
    visited = []

    next = [tuple(start_point)]
    while len(next):
        current = next.pop()

        visited.append(current)
        current_val = grid[current[0], current[1]]

        if current_val == 9:
            continue

        for n in neighbors:
            n_loc = current[0] + n[0], current[1] + n[1]

            if not (0 <= n_loc[0] < grid.shape[0]) or not (0 <= n_loc[1] < grid.shape[1]):
                continue

            if n_loc in visited and not skip_visited:
                continue

            n_val = grid[*n_loc]
            if n_val - current_val == 1:
                next.append(n_loc)
    return visited

def p1():
    with open(file, "r") as f:
        grid = [[int(i) for i in l.strip()] for l in f]
    grid = np.asarray(grid)

    start_points = np.argwhere(grid == 0)

    total = 0
    for s in start_points:
        visited = bfs(grid, s)
        for i in visited:
            if grid[i[0], i[1]] == 9:
                total += 1
    return total

def p2():
    with open(file, "r") as f:
        grid = [[int(i) for i in l.strip()] for l in f]
    grid = np.asarray(grid)

    start_points = np.argwhere(grid == 0)

    total = 0
    for s in start_points:
        visited = bfs(grid, s, True)
        for i in visited:
            if grid[i[0], i[1]] == 9:
                total += 1
    return total
print(p1())
print(p2())



