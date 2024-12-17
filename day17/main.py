import multiprocessing as mp

file = "data.txt"

def run_program(registers, program):
    A, B, C = registers
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1]

        if opcode == 0:  # adv
            if operand <= 3:
                denominator = 2 ** operand
            elif operand == 4:
                denominator = 2 ** A
            elif operand == 5:
                denominator = 2 ** B
            elif operand == 6:
                denominator = 2 ** C
            else:
                raise ValueError(opcode)
            A = A // denominator

        elif opcode == 1:  # bxl
            B = B ^ operand

        elif opcode == 2:  # bst
            if operand <= 3:
                B = operand % 8
            elif operand == 4:
                B = A % 8
            elif operand == 5:
                B = B % 8
            elif operand == 6:
                B = C % 8

        elif opcode == 3:  # jnz
            if A != 0:
                instruction_pointer = operand
                continue

        elif opcode == 4:  # bxc
            B = B ^ C

        elif opcode == 5:  # out
            if operand <= 3:
                value = operand % 8
            elif operand == 4:
                value = A % 8
            elif operand == 5:
                value = B % 8
            elif operand == 6:
                value = C % 8
            else:
                raise ValueError(opcode)
            output.append(value)

        elif opcode == 6:  # bdv
            if operand <= 3:
                denominator = 2 ** operand
            elif operand == 4:
                denominator = 2 ** A
            elif operand == 5:
                denominator = 2 ** B
            elif operand == 6:
                denominator = 2 ** C
            else:
                raise ValueError(opcode)
            B = A // denominator

        elif opcode == 7:  # cdv
            if operand <= 3:
                denominator = 2 ** operand
            elif operand == 4:
                denominator = 2 ** A
            elif operand == 5:
                denominator = 2 ** B
            elif operand == 6:
                denominator = 2 ** C
            else:
                raise ValueError(opcode)
            C = A // denominator

        instruction_pointer += 2

    return output

def p1():
    with open(file) as f:
        l = f.readlines()

        reg_a = int(l[0].strip().split(":")[1])
        reg_b = int(l[1].strip().split(":")[1])
        reg_c = int(l[2].strip().split(":")[1])
        program = [int(i) for i in l[-1].strip().split(":")[1].split(",")]
    return ",".join(map(str, run_program([reg_a, reg_b, reg_c], program)))

def run(args):
    initial_A, reg_b, reg_c, program = args
    registers = [initial_A, reg_b, reg_c]
    output = run_program(registers, program)
    is_same = (output == program)

    if initial_A % 10000 == 0:
        print(initial_A)

    return is_same, initial_A, output

def infinite_loop():
    i = 0
    while True:
        yield i
        i += 1

def p2(): # copied from https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2gliho/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    with open(file) as f:
        l = f.readlines()
        reg_a = int(l[0].strip().split(":")[1])
        reg_b = int(l[1].strip().split(":")[1])
        reg_c = int(l[2].strip().split(":")[1])
        program = [int(i) for i in l[-1].strip().split(":")[1].split(",")]

    todo = [(1, 0)]
    for i, a in todo:
        for a in range(a, a+8):
            _, _, output = run([a, 0, 0, program])
            if output == program[-i:]:
                print(output, program)
                todo += [(i+1, a*8)]
                if i == len(program): return a

if __name__ == "__main__":
    print(p1())
    print(p2())