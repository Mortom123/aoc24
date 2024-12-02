file = "data.txt"

def p1():
    safe = 0
    with open(file) as f:
        for l in f:
            nums = [int(i) for i in l.strip().split()]
            try:
                diff = (nums[1] - nums[0]) / (abs(nums[1] - nums[0]))
            except ZeroDivisionError:
                continue

            is_safe = all(0 < (num2 - num1) * diff < 4 for num1, num2 in zip(nums[:-1], nums[1:]))
            if is_safe:
                safe += 1
    return safe

def p2():
    safe = 0
    with open(file) as f:
        for l in f:
            nums = [int(i) for i in l.strip().split()]
            is_safe = False
            for index in range(len(nums)):
                num_without = nums[:index] + nums[index + 1:]
                try:
                    diff = (num_without[1] - num_without[0]) / (abs(num_without[1] - num_without[0]))
                except ZeroDivisionError:
                    continue

                is_safe = all(0 < (num2 - num1) * diff < 4 for num1, num2 in zip(num_without[:-1], num_without[1:]))
                if is_safe:
                    break

            if is_safe:
                safe += 1

    return safe

print(p1())
print(p2())



