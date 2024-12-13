import numpy as np
import re

from numpy.array_api import int64, float64

file = "data.txt"

number_match = re.compile(r"(\d+)")

def p1():
    with open(file) as f:
        eqs = []
        current_eq = []
        for l in f:
            l = l.strip()
            if l == "":
                eqs.append(current_eq)
                current_eq = []
                continue
            current_eq.append(number_match.findall(l))
        eqs.append(current_eq)

    # Ax = C
    # x = C * A^-1
    total = np.asarray([0, 0])
    for eq in eqs:
        A = np.asarray(eq[:2]).T.astype(float)
        C = np.asarray(eq[2]).astype(float)
        sol = np.round(np.linalg.solve(A, C), 0)
        if np.all(A @ sol == C):
            total += sol.astype(int)

    return total[0] * 3 + total[1]

def p2():
    with open(file) as f:
        eqs = []
        current_eq = []
        for l in f:
            l = l.strip()
            if l == "":
                eqs.append(current_eq)
                current_eq = []
                continue
            current_eq.append(number_match.findall(l))
        eqs.append(current_eq)

    total = np.asarray([0, 0], dtype=float64)
    for i, eq in enumerate(eqs):
        A = np.asarray(eq[:2]).T.astype(int64)
        C = np.asarray(eq[2]).astype(int64) + 10000000000000
        sol = np.round(np.linalg.solve(A, C), 0)
        if np.all(A @ sol == C):
            total += sol

    return total[0] * 3 + total[1]

print(p1())
print(p2())