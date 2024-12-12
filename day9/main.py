import numpy as np
import itertools

file = "data.txt"

def p1():
    with open(file) as f:
        line = [int(i) for i in f.readlines()[0].strip()]

    current_file = 0
    current_index = 0
    files = {".": []}
    isFile = True
    for l in line:
        index_range = list(range(current_index, current_index + l))
        if isFile:
            files[current_file] = index_range
            current_file += 1
        else:
            files["."].extend(index_range)

        current_index += l
        isFile = not isFile

    open_slots = files.pop(".")

    x = ["."] * current_index
    for k,v in files.items():
        for i in v:
            x[i] = k

    current_min = open_slots.pop(0)
    current_max = current_index - 1

    while current_min < current_max:
        x[current_min], x[current_max] = x[current_max], x[current_min]

        current_max -= 1
        while x[current_max] == ".":
            current_max -= 1

        current_min = open_slots.pop(0)

    total = 0
    for index, i in enumerate(x):
        if i == ".":
            break
        total += (index * i)

    return total

def p2():
    with open(file) as f:
        line = [int(i) for i in f.readlines()[0].strip()]

    current_file = 0
    current_index = 0
    files = {".": []}
    isFile = True
    for l in line:
        index_range = list(range(current_index, current_index + l))
        if isFile:
            if len(index_range):
                files[current_file] = index_range
            current_file += 1
        else:
            if len(index_range):
                files["."].append(index_range)

        current_index += l
        isFile = not isFile

    open_slots = files.pop(".")

    keys = list(sorted(files.keys(), reverse=True))

    for i in keys:
        indices = files[i]
        move_to = None
        for slots in open_slots:
            if len(slots) >= len(indices) and slots[0] < indices[0]:
                move_to = slots
                break

        if move_to is None:
            continue

        open_slots.remove(move_to)
        swap_len = len(indices)
        files[i] = move_to[:swap_len]

        still_open = move_to[swap_len:]
        if len(still_open) > 0:
            open_slots.append(still_open)
            open_slots.sort(key= lambda a: a[0])


    total = 0
    for k,v in files.items():
        total += sum(k * i for i in v)
    return total


print(p1())
print(p2())



