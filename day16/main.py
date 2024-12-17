import numpy as np
from utils.direction import Direction
from utils.astar import astar, astar_multipath
from utils.point import Point
from typing import List, Tuple
from dataclasses import dataclass

file = "data.txt"

@dataclass(unsafe_hash=True)
class PointWithDirection:
    point: Point
    direction: Direction

def p1():
    grid = []
    with open(file) as f:
        for l in f:
            l = l.strip()
            grid.append(list(l))
    grid = np.asarray(grid)

    s = np.argwhere(grid == "S")[0]
    g = np.argwhere(grid == "E")[0]
    start = PointWithDirection(
        point=Point(int(s[1]), int(s[0])),
        direction=Direction.EAST
    )

    def is_goal(p: PointWithDirection):
        return g[0] == p.point.y and g[1] == p.point.x

    def get_neighbors(current: PointWithDirection) -> List[Tuple[PointWithDirection, float]]:
        ns = []

        check_directions = {
            Direction.NORTH,
            Direction.EAST,
            Direction.WEST,
            Direction.SOUTH,
        } - {current.direction.inverse()}

        for d in check_directions:
            n = current.point + d.point()
            if grid[n.y, n.x] == "#":
                continue
            cost = 1
            if d != current.direction:
                cost += 1000
            ns.append((PointWithDirection(n, d), cost))
        return ns

    def heuristic(p: PointWithDirection) -> float:
        return abs(g[0] - p.point.y) + abs(g[1] - p.point.x)

    goal_node = astar(start, is_goal, get_neighbors, heuristic)

    return goal_node.cost

def p2():
    grid = []
    with open(file) as f:
        for l in f:
            l = l.strip()
            grid.append(list(l))
    grid = np.asarray(grid)

    s = np.argwhere(grid == "S")[0]
    g = np.argwhere(grid == "E")[0]
    start = PointWithDirection(
        point=Point(int(s[1]), int(s[0])),
        direction=Direction.EAST
    )

    def is_goal(p: PointWithDirection):
        return g[0] == p.point.y and g[1] == p.point.x

    def get_neighbors(current: PointWithDirection) -> List[Tuple[PointWithDirection, float]]:
        ns = []

        check_directions = {
                               Direction.NORTH,
                               Direction.EAST,
                               Direction.WEST,
                               Direction.SOUTH,
                           } - {current.direction.inverse()}

        for d in check_directions:
            n = current.point + d.point()
            if grid[n.y, n.x] == "#":
                continue
            cost = 1
            if d != current.direction:
                cost += 1000
            ns.append((PointWithDirection(n, d), cost))
        return ns

    def heuristic(p: PointWithDirection) -> float:
        return abs(g[0] - p.point.y) + abs(g[1] - p.point.x)

    goal_node = astar_multipath(start, is_goal, get_neighbors, heuristic)

    nodes = goal_node
    node_indices = set()
    while nodes:
        current = nodes.pop()
        node_indices.add((current.value.point.y, current.value.point.x))

        for n in current.parents:
            nodes.append(n)

    return len(node_indices)

print(p1())
print(p2())