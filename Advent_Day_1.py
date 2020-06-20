# Advent of Coding
# https://adventofcode.com/2019/day/1

#### PART ONE
def module_fuel(mass) -> int:
    """To find the fuel required for a module, take its mass, divide by three, round down, and subtract 2."""
    mass = mass // 3 - 2
    return 0 if mass < 0 else mass

# Tests fuel module calculation
try:
    assert module_fuel(12) == 2
    assert module_fuel(14) == 2
    assert module_fuel(1969) == 654
    assert module_fuel(100756) == 33583
    assert module_fuel(1) == 0
except AssertionError:
    print('incorrect module_fuel calculation')



### PART TWO

def module_fuel_fuel(mass) -> int:
    """Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on."""
    added_fuel = 0
    while mass // 3 > 2:
        mass = mass // 3 - 2 
        added_fuel += mass 
    return added_fuel

# Tests fuel module calculation
try:
    assert module_fuel_fuel(14) == 2
    assert module_fuel_fuel(1969) == 966 
    assert module_fuel_fuel(100756) == 50346
    assert module_fuel_fuel(1) == 0
except AssertionError:
    print('error in fuel_fuel')

if __name__ == "__main__":

    # Answer to Part 1 of 2 
    print('part 1 of 2 - paste input:')
    mass_list = input()
    mass_list = mass_list.split(' ')
    mass_list = [int(mass.strip()) for mass in mass_list]
    mass_sum = 0
    for mass in mass_list:
        mass_sum += module_fuel(mass)
        
    print(f'you MASSt {mass_sum} units of fuel')
    
    # Answer to part 2 of 2
    print('part 2 of 2 - paste input:')
    mass_list = input()
    mass_list = mass_list.split(' ')
    mass_list = [int(mass.strip()) for mass in mass_list]
    mass_sum = 0
    for mass in mass_list:
        fuel_mass = module_fuel(mass)
        mass_sum += fuel_mass
        mass_sum += module_fuel_fuel(fuel_mass)

    print(f'you MASSt {mass_sum} units of fuel.')
