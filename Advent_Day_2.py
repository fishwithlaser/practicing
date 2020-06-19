# Advent of coding day 2
# https://adventofcode.com/2019/day/2

    Intcode = list(Intcode)
    index = 0
    while True:
        try:
            #opcode
            opcode = Intcode[index]
            assert opcode in [1, 2, 99]
            if opcode == 99:
                print('exit 99 - No error')
                break

            read_1 = Intcode[index + 1]
            read_2 = Intcode[index + 2]
            output = Intcode[index + 3]

            # opcode says to add intcodes
            if opcode == 1:
                Intcode[output] = Intcode[read_1] + Intcode[read_2]

            # opcode says to multiply incodes
            if opcode == 2:
                Intcode[output] = Intcode[read_1] * Intcode[read_2]
            index += 4
        except AssertionError:
            print(f'1202 program alarm.\nopcode:\n: {Intcode}')
            return False
    return tuple(Intcode)


try:
    print('    INITIATING TESTS CASES    ')
    program_1202_tests = [(1,0,0,3,99),
            (1,9,10,3, 2,3,11,0, 99, 30,40,50)]
    for Intcode in program_1202_tests:
        output = program_1202(Intcode)
        assert output is not False
    print(f'    PASSED (n={len(program_1202_tests)})    \n')
except AssertionError:
    print(f'\033[101m    TEST FAILED - error with opcode {Intcode} \033[m')

def restore_gravity(opcode):
    """replace position 1 with the value 12 and replace position 2 with the value 2."""
    opcode_temp = list(opcode)
    opcode_temp[1] = 12
    opcode_temp[2] = 2
    return tuple(opcode_temp)

if __name__ == "__main__":
    print('part 1 - paste input:')
    Intcode = input()
    Intcode = [int(i) for i in Intcode.split(',')]
    Intcode = restore_gravity(Intcode)
    output = program_1202(Intcode)

    print(f'What value is left at position 0? Ans: {output[0]}')

