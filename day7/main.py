from typing import Tuple, List, Dict
import itertools
from multiprocessing import Pool

file = "data.txt"

def solve(eq: Tuple[int, List[int]], operators: Dict):
    target, operands = eq

    for i in itertools.product(operators.keys(), repeat=len(operands) - 1):
        total = operands[0]
        for j in range(len(operands) - 1):
            operation = operators[i[j]]
            total = operation(total, operands[j + 1])

        if total == target:
            return True
    return False

def add(x, y):
    return x + y
def mul(x, y):
    return x * y
def cat(x, y):
    return int(str(x) + str(y))

def p1():
    with open(file, "r") as f:
        eqs = []
        for line in f:
            target, operands = line.strip().split(":")
            operands = operands.split()
            eq = (
                int(target), [int(i) for i in operands]
            )
            eqs.append(eq)
    operators = {
        "add": add,
        "mul": mul,
    }
    items = [(eq, operators) for eq in eqs]
    with Pool() as p:
        result = p.starmap(solve, items)
        # result = list(map(lambda i: solve(*i), items))

    total = 0
    for eq, r in zip(eqs, result):
        if r:
            total += eq[0]

    return total

def p2():
    with open(file, "r") as f:
        eqs = []
        for line in f:
            target, operands = line.strip().split(":")
            operands = operands.split()
            eq = (
                int(target), [int(i) for i in operands]
            )
            eqs.append(eq)
    operators = {
        "add": add,
        "mul": mul,
        "cat": cat
    }
    items = [(eq, operators) for eq in eqs]
    with Pool() as p:
        result = p.starmap(solve, items)
        # result = list(map(lambda i: solve(*i), items))

    total = 0
    for eq, r in zip(eqs, result):
        if r:
            total += eq[0]

    return total

if __name__ == "__main__":
    print(p1())
    print(p2())



