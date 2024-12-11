from collections import Counter
file = "data.txt"

def evolve(stones: Counter) -> Counter:
    new_stones = Counter()

    for stone_val, stone_count in stones.items():
        if stone_val == 0:
            new_stones[1] += stone_count
        elif len(str(stone_val)) % 2 == 0:
            stone = str(stone_val)
            left = int(stone[:len(stone)//2])
            right = int(stone[len(stone)//2:])
            new_stones[left] += stone_count
            new_stones[right] += stone_count
        else:
            new_stones[stone_val * 2024] += stone_count

    return new_stones

def p1():
    with open(file, "r") as f:
        stones = Counter(int(i) for i in f.readlines()[0].strip().split())

    for i in range(25):
        stones = evolve(stones)
    return sum(stones.values())

def p2():
    with open(file, "r") as f:
        stones = Counter(int(i) for i in f.readlines()[0].strip().split())

    for i in range(75):
        stones = evolve(stones)
    return sum(stones.values())

print(p1())
print(p2())



