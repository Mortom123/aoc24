import re

file = "data.txt"

def p1():
    with open(file) as f:
        s = "".join([l.strip() for l in f])

    regex = re.compile("mul\((\d+,\d+)\)")
    muls = [i.split(",") for i in regex.findall(s)]
    return sum(int(i[0]) * int(i[1]) for i in muls)

def p2():
    with open(file) as f:
        s = "".join([l.strip() for l in f])

    rdos = re.compile("do\(\)")
    rdonts = re.compile("don't\(\)")
    rmuls = re.compile("mul\((\d+,\d+)\)")

    modifiers = []
    modifiers += [(i.start(),True) for i in rdos.finditer(s)]
    modifiers += [(i.start(), False) for i in rdonts.finditer(s)]
    modifiers.sort(key=lambda a: a[0])

    active = True
    sum = 0
    for i in rmuls.finditer(s):
        while len(modifiers) > 0 and modifiers[0][0] < i.start():
            mod = modifiers.pop(0)
            active = mod[1]

        if not active:
            continue
        m = i.group(1).split(",")
        sum +=  int(m[0]) * int(m[1])
    return sum

print(p1())
print(p2())



