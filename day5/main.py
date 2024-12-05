from functools import cmp_to_key

file = "data.txt"

def p1_p2():
    orders = {}
    inputs = []
    with open(file) as f:
        is_orders = True
        for line in f:
            line = line.strip()
            if line == "":
                is_orders = False
                continue

            if is_orders:
                before, after = line.split("|")
                orders.setdefault(int(before), set()).add(int(after))
            else:
               inputs.append([int(i) for i in line.split(",")])

    def compare(a, b):
        sa = orders.get(a, None)
        sb = orders.get(b, None)
        b_in_a = False if sa is None else b in sa
        a_in_b = False if sb is None else a in sb

        if a_in_b:
            return 1
        elif b_in_a:
            return -1
        else:
            return 0

    result_1 = 0
    result_2 = 0
    for line in inputs:
        line_before = line.copy()
        line.sort(key=cmp_to_key(compare))

        if line_before == line:
            result_1 += line[len(line) // 2]
        else:
            result_2 += line[len(line) // 2]
    return result_1, result_2



print(p1_p2())



