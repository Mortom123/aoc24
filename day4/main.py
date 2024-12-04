from utils.grid import Grid2D

file = "data.txt"

def p1():
    with open(file) as f:
        lines = [l.strip() for l in f]
    grid = Grid2D(lines)
    indices = grid.find_all("X")

    total = 0
    for row, col in indices:
        checks = []
        # check right
        try:
            checks.append("".join(grid[row, col:col + 4]))
        except Exception:
            pass
        # check left
        try:
            checks.append("".join(grid[row, col:col-4:-1]))
        except Exception:
            pass
        # check bottom
        try:
            checks.append("".join(grid[row:row+4, col]))
        except Exception:
            pass
        # check top
        try:
            checks.append("".join(grid[row:row-4:-1, col]))
        except Exception:
            pass
        # check \
        try:
            checks.append("".join(grid[row+i,col+i] for i in range(4)))
        except Exception:
            pass
        # check /
        try:
            checks.append("".join(grid[row-i, col+i] for i in range(4)))
        except Exception:
            pass
        # check \ rev
        try:
            checks.append("".join(grid[row-i, col-i] for i in range(4)))
        except Exception:
            pass
        # check / rev
        try:
            checks.append("".join(grid[row+i, col-i] for i in range(4)))
        except Exception:
            pass

        total += len([check for check in checks if check == "XMAS"])
    return total




def p2():
    with open(file) as f:
        lines = [l.strip() for l in f]
    grid = Grid2D(lines)
    indices = grid.find_all("A")

    total = 0
    max_row, max_col = grid.size()
    for row, col in indices:
        if 0 < row < max_row - 1 and 0 < col < max_col - 1:
            elem_1 = grid[row - 1, col - 1] + "A" + grid[row + 1, col + 1]
            elem_2 = grid[row - 1, col + 1] + "A" + grid[row + 1, col - 1]
            if (elem_1 == "MAS" or elem_1 == "SAM") and (elem_2 == "MAS" or elem_2 == "SAM"):
                total += 1
    return total

print(p1())
print(p2())



