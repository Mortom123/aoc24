import numpy as np

from utils.pathfinding import astar, get_path
from utils.point import get_neighbors
from typing import Tuple, List

file = "data.txt"

type Node = Tuple[int, int]

def p1():
    with open(file) as f:
        bytes = [tuple(map(int, l.strip().split(","))) for l in f]
    max_x, max_y = max(bytes, key=lambda a: a[0])[0], max(bytes, key=lambda a: a[1])[1]

    if file == "ex.txt":
        bytes = bytes[:12]
    else:
        bytes = bytes[:1024]

    start: Node = (0, 0)

    def is_goal(t: Node) -> bool:
        return t[0] == max_x and t[1] == max_y

    bytes_lookup = set(bytes)
    def neighbors(t: Node) -> List[Tuple[Node, float]]:
        n = []
        for i in get_neighbors(np.asarray(t)):
            i = (i[0], i[1])
            if i in bytes_lookup:
                continue
            if not 0 <= i[0] <= max_x or not 0 <= i[1] <= max_y:
                continue
            n.append((i, 1))
        return n

    def heuristic(t: Node) -> int:
        return (max_x - t[0]) + (max_y - t[1])

    return astar(start, is_goal, neighbors, heuristic)[0].cost

def p2():
    with open(file) as f:
        bytes = [tuple(map(int, l.strip().split(","))) for l in f]
    max_x, max_y = max(bytes, key=lambda a: a[0])[0], max(bytes, key=lambda a: a[1])[1]

    if file == "ex.txt":
        current_index = 12
    else:
        current_index = 1024

    start: Node = (0, 0)

    def is_goal(t: Node) -> bool:
        return t[0] == max_x and t[1] == max_y

    def heuristic(t: Node) -> int:
        return (max_x - t[0]) + (max_y - t[1])

    bytes_lookup = set(bytes[:current_index])
    def neighbors(t: Node) -> List[Tuple[Node, float]]:
        n = []
        for i in get_neighbors(np.asarray(t)):
            i = (i[0], i[1])
            if i in bytes_lookup:
                continue
            if not 0 <= i[0] <= max_x or not 0 <= i[1] <= max_y:
                continue
            n.append((i, 1))
        return n

    current_path = set(get_path(astar(start, is_goal, neighbors, heuristic)[0]))
    while True:
        current_block = bytes[current_index]
        current_index += 1

        if current_block not in current_path:
            continue

        bytes_lookup = set(bytes[:current_index])
        result = astar(start, is_goal, neighbors, heuristic)
        if not len(result):
            print(current_index - 1)
            return ",".join(list(map(str, current_block)))
        current_path = set(get_path(astar(start, is_goal, neighbors, heuristic)[0]))

if __name__ == "__main__":
    print(p1())
    print(p2())