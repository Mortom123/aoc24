def p1():
    left, right = [], []
    with open("data.txt") as f:
        for l in f:
            a,b = l.strip().split()
            left.append(int(a))
            right.append(int(b))
    left.sort()
    right.sort()

    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])
    return sum

def p2():
    left, counts = [], {}
    with open("data.txt") as f:
        for l in f:
            a,b = l.strip().split()
            left.append(int(a))
            counts[int(b)] = counts.get(int(b), 0) + 1

    sum = 0
    for i in range(len(left)):
        sum += (left[i] * counts.get(left[i], 0))
    return sum

print(p1())
print(p2())