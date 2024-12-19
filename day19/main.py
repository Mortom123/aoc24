from functools import cache

file = "data.txt"
def p1():
    patterns = set()
    tasks = []
    is_pattern = True

    with open(file) as f:
        for l in f:
            l = l.strip()
            if l == "":
                is_pattern = False
                continue
            if is_pattern:
                patterns.update([i.strip() for i in l.split(",")])
            else:
                tasks.append(l)

    @cache
    def solve(task):
        if task == "":
            return True
        return any(solve(task[len(p):]) for p in patterns if task.startswith(p))

    solvable = [solve(i) for i in tasks]
    return sum(solvable)

def p2():
    patterns = set()
    tasks = []
    is_pattern = True

    with open(file) as f:
        for l in f:
            l = l.strip()
            if l == "":
                is_pattern = False
                continue
            if is_pattern:
                patterns.update([i.strip() for i in l.split(",")])
            else:
                tasks.append(l)

    @cache
    def solve(task):
        if task == "":
            return 1
        return sum(solve(task[len(p):]) for p in patterns if task.startswith(p))

    return sum(solve(t) for t in tasks)

print(p1())
print(p2())