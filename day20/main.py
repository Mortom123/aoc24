import numpy as np
from itertools import combinations

from utils.pathfinding import astar, get_path
from utils.point import get_neighbors
from typing import Tuple, List

file = "data.txt"

type Node = Tuple[int, int]

def read_input():
    with open(file) as f:
        coords = [list(l.strip()) for l in f]
    grid = np.asarray(coords)
    start, end = np.argwhere(grid == "S")[0], np.argwhere(grid == "E")[0]
    return grid, start, end

def manhattan(a: Node, b: Node):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def p1():
    grid, start, end = read_input()

    def is_goal(coords: Node) -> bool:
        return coords[0] == end[0] and coords[1] == end[1]

    def neighbors(coords: Node) -> List[Tuple[Node, float]]:
        nonlocal grid
        ns = []
        for n in get_neighbors(np.asarray(coords)):
            n_value = grid[*n]

            if n_value == "#":
                continue
            node: Node = (int(n[0]), int(n[1]))
            ns.append((node, 1))
        return ns

    def heuristic(coords: Node) -> int:
        return manhattan(coords, end)

    start_node: Node = (int(start[0]), int(start[1]))
    default_route = astar(start_node, is_goal, neighbors, heuristic)[0]

    default_path = get_path(default_route)

    min_save = 100
    dist = 2

    cheats = 0
    for index, i in enumerate(default_path):
        after = default_path[index+min_save+1:]
        for a in after:
            cheat_dist = manhattan(a,i)
            if cheat_dist <= dist:
                cheats += 1

    return cheats

def p2():
    grid, start, end = read_input()

    def is_goal(coords: Node) -> bool:
        return coords[0] == end[0] and coords[1] == end[1]

    def neighbors(coords: Node) -> List[Tuple[Node, float]]:
        nonlocal grid
        ns = []
        for n in get_neighbors(np.asarray(coords)):
            n_value = grid[*n]

            if n_value == "#":
                continue
            node: Node = (int(n[0]), int(n[1]))
            ns.append((node, 1))
        return ns

    def heuristic(coords: Node) -> int:
        return manhattan(coords, end)

    start_node: Node = (int(start[0]), int(start[1]))
    default_route = astar(start_node, is_goal, neighbors, heuristic)[0]

    default_path = get_path(default_route)

    min_save = 100
    dist = 20

    cheats = 0
    for a,b in combinations(range(len(default_path)), 2):
        pa, pb = default_path[a], default_path[b]
        cheat_dist = manhattan(pa, pb)
        saving = b - (cheat_dist + a)
        if cheat_dist <= dist and saving >= min_save:
            cheats += 1
    return cheats

print(p1())
print(p2())