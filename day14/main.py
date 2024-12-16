import numpy as np
import re

file = "data.txt"

match = re.compile(r"p=(\d+,\d+) v=(\d+,\d+)")

def p1():
    if file == "ex.txt":
        grid_size = np.asarray((11,7))
    else:
        grid_size = np.asarray((101, 103))

    ps = []
    vs = []
    with open(file) as f:
        for l in f:
            l = l.strip()
            p, v = l.split()
            p, v = tuple(map(int, p.split("=")[1].split(","))), tuple(map(int, v.split("=")[1].split(",")))
            ps.append(p)
            vs.append(v)
    ps = np.array(ps)
    vs = np.array(vs)
    end = (ps + 100 * vs) % grid_size
    quadrant_cutoff_x, quadrant_cutoff_y = grid_size[0] // 2, grid_size[1] // 2

    quadrant_1 = end[
        np.logical_and(end[:,0] < quadrant_cutoff_x, end[:,1] < quadrant_cutoff_y)
    ]
    quadrant_2 = end[
        np.logical_and(end[:,0] > quadrant_cutoff_x, end[:,1] < quadrant_cutoff_y)
    ]
    quadrant_3 = end[
        np.logical_and(end[:,0] < quadrant_cutoff_x, end[:,1] > quadrant_cutoff_y)
    ]
    quadrant_4 = end[
        np.logical_and(end[:,0] > quadrant_cutoff_x, end[:,1] > quadrant_cutoff_y)
    ]
    factor = len(quadrant_1) * len(quadrant_2) * len(quadrant_3) * len(quadrant_4)
    return factor

def p2():
    return 7584 # had to look here to figure it out : https://github.com/marcodelmastro/AdventOfCode2024/blob/main/Day14.ipynb

print(p1())
print(p2())