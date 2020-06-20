# Day 2 - Advent of code
# https://adventofcode.com/2019/day/2

def program_1202(Intcode) -> tuple:
    # record_operations identifies operations that use nouns and verbs
    Intcode = list(Intcode)
    index = 0 
    while True:
        try:
            #opcode
            opcode = Intcode[index]
            assert opcode in [1, 2, 99] 
            if opcode == 99: 
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
    
def restore_gravity(Intcode, noun=12, verb=2):
    """replace position 1 with the value 12 and replace position 2 with the value 2."""    Intcode_temp = list(Intcode)
    Intcode_temp[1] = noun
    Intcode_temp[2] = verb
    return tuple(Intcode_temp)

if __name__ == "__main__":
    print('part 1 - paste input:')
    Intcode = input()
    Intcode = [int(i) for i in Intcode.split(',')]
    Intcode_0 = Intcode
    for noun in range(100):
        for verb in range(100):
            restored_gravity = restore_gravity(Intcode_0, noun, verb)
            try:
                output = program_1202(restored_gravity)
            except IndexError:
                pass
            if output[0] == 19690720:
                print(f'noun={noun}, verb={verb}')
                break
    print(f'What is 100 * noun + verb? Ans: {noun}{verb}')
