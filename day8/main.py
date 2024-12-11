import numpy as np
import itertools

file = "data.txt"

def p1():
    with open(file) as f:
        lines = [list(l.strip()) for l in f]

    grid = np.asarray(lines)
    elements = np.unique(grid)

    coords = {}
    for elem in elements:
        if elem == ".":
            continue
        coords[elem] = np.argwhere(grid==elem)

    antinodes = set()
    for key, vals in coords.items():
        for a, b in itertools.permutations(vals, 2):
            node = 2*a - b
            if np.all(0 <= node) and np.all(node < grid.shape):
                antinodes.add(tuple(node))
    return len(set(antinodes))

def p2():
    with open(file) as f:
        lines = [list(l.strip()) for l in f]

    grid = np.asarray(lines)
    elements = np.unique(grid)

    coords = {}
    for elem in elements:
        if elem == ".":
            continue
        coords[elem] = np.argwhere(grid==elem)

    antinodes = set()
    for key, vals in coords.items():
        for a, b in itertools.permutations(vals, 2):
            antinodes.add(tuple(a))
            diff = a - b
            node = a + diff
            while np.all(0 <= node) and np.all(node < grid.shape):
                antinodes.add(tuple(node))
                node += diff
    return len(set(antinodes))

print(p1())
print(p2())




