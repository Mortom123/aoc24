from typing import Set, Tuple, List
import numpy as np

file = "data.txt"

def get_regions(indicies: Set[Tuple[int, int]], connections: Set[Tuple[int, int]]) -> List[Set[Tuple[int, int]]]:
    regions = []
    while len(indicies) > 0:
        current_region = set()
        current_leaves = [indicies.pop()]
        while len(current_leaves) > 0:
            node = current_leaves.pop(0)
            current_region.add(node)

            for con in connections:
                neighbor_node = node[0] + con[0], node[1] + con[1]
                if neighbor_node in indicies:
                    current_leaves.append(neighbor_node)
                    indicies.remove(neighbor_node)
        regions.append(current_region)
    return regions


def get_perimeter(region: Set[Tuple[int, int]], connections: Set[Tuple[int, int]]) -> float:
    total = 0
    for node in region:
        possible = len(connections)
        for con in connections:
            neighbor_node = node[0] + con[0], node[1] + con[1]
            if neighbor_node in region:
                possible -= 1
        total += possible
    return total


def get_straight_edge_perimeter(region: Set[Tuple[int, int]]) -> float:
    if len(region) == 1 or len(region) == 2:
        return 4
    up = (0, 1)
    down = (0, -1)
    left = (1, 0)
    right = (-1, 0)

    total = 0
    for node in region:
        nup = node[0] + up[0], node[1] + up[1]
        ndown = node[0] + down[0], node[1] + down[1]
        nleft = node[0] + left[0], node[1] + left[1]
        nright = node[0] + right[0], node[1] + right[1]
        nupleft = node[0] + up[0] + left[0], node[1] + up[1] + left[1]
        nupright = node[0] + up[0] + right[0], node[1] + up[1] + right[1]
        ndownleft = node[0] + down[0] + left[0], node[1] + down[1] + left[1]
        ndownright = node[0] + down[0] + right[0], node[1] + down[1] + right[1]

        if nright not in region and nup not in region: 
            total += 1
        
        if nright not in region and ndown not in region: 
            total += 1
    
        if nleft not in region and ndown not in region: 
            total += 1
    
        if nleft not in region and nup not in region:
            total += 1

        if nright in region and nup in region and nupright not in region:
            total += 1
        
        if nright in region and ndown in region and ndownright not in region: 
            total += 1
        
        if nleft in region and ndown in region and ndownleft not in region: 
            total += 1
        
        if nleft in region and nup in region and nupleft not in region: 
            total += 1
    
    return total


def p1():
    with open(file) as f:
        lines = [list(l.strip()) for l in f.readlines()]
    grid = np.asarray(lines)
    elements = np.unique(grid)

    connections = {(1,0),(-1,0),(0,1),(0,-1)}

    total = 0
    for elem in elements:
        indices = {(int(i[0]), int(i[1])) for i in np.argwhere(grid == elem)}
        regions = get_regions(indices, connections)
        for r in regions:
            total += (get_perimeter(r, connections) * len(r))
    return total


def p2():
    with open(file) as f:
        lines = [list(l.strip()) for l in f.readlines()]
    grid = np.asarray(lines)
    elements = np.unique(grid)

    connections = {(1,0),(-1,0),(0,1),(0,-1)}

    total = 0
    for elem in elements:
        indices = {(int(i[0]), int(i[1])) for i in np.argwhere(grid == elem)}
        regions = get_regions(indices, connections)
        for r in regions:
            cost = get_straight_edge_perimeter(r)
            total += (cost * len(r))
    return total

print(p1())
print(p2())