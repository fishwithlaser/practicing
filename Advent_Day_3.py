#Input is one string. Each input is a row, and the entries in rows are separated a line break
#
# e.g., 
#    R75,D30,R83,U83,L12,D49,R71,U7,L72
#    U62,R66,U55,R34,D71,R55,D58,R83
#
#  unsolved.

import numpy

def find_gridsize(row):
    """Finds minimum dimensions for a grid"""
    y = 0
    min_y = 0
    max_y = 0
    x = 0
    min_x = 0
    max_x = 0

    for item in row:
        if item[0] == 'D':
            y -= int(item[1:])
            if y < min_y: min_y = y
        elif item[0] == 'U':
            y += int(item[1:])
            if y > max_y: max_y = y
        elif item[0] == 'L':
            x -= int(item[1:])
            if x < min_x: min_x = x
        elif item[0] == 'R':
            x += int(item[1:])
            if x > max_x: max_x = x
        else: print('ERROR - should never reach this')
    return min_y, max_y, min_x, max_x

def build_matrix(row_1, row_2):
    """builds minimum-sized mxn matrix"""
    min_y0, max_y0, min_x0, max_x0 = find_gridsize(row_1)
    min_y1, max_y1, min_x1, max_x1 = find_gridsize(row_2)

    min_y = min([min_y0, min_y1])
    max_y = max([max_y0, max_y1])
    y_dim = max_y - min_y

    min_x = min([min_x0, min_x1])
    max_x = max([max_x0, max_x1])
    x_dim = max_x - min_x

    print(f'min dimensions y=({min_y})-{max_y}, x=({min_x})-{max_x}')

    matrix = []
    for x in range(x_dim):
       matrix.append([0]*y_dim)
    return matrix, -min_x, -min_y

def draw_matrix(row, matrix, a, b, index_x, index_y):
    """draws the path of the matrix"""

    for command in row:
        #e.g., R75
        if command[0] == 'R':
            movement = int(command[1:])
            for i in range(movement):
                index_x += 1
                matrix[index_y][index_x] = 3 if matrix[index_y][index_x] == b else a
        if command[0] == 'L':
            movement = int(command[1:])
            for i in range(movement):
                index_x -= 1
                matrix[index_y][index_x] = 3 if matrix[index_y][index_x] == b else a
        #e.g., R75
        if command[0] == 'U':
            movement = int(command[1:])
            for i in range(movement):
                index_y += 1
                matrix[index_y][index_x] = 3 if matrix[index_y][index_x] == b else a
        if command[0] == 'D':
            movement = int(command[1:])
            for i in range(movement):
                index_y -= 1
                matrix[index_y][index_x] = 3 if matrix[index_y][index_x] == b else a
   return matrix

if __name__ == "__main__":
    print('insert tuples instructions')
    _tuple = input()
    _tuples = _tuple.split(' ')
    row_1 = _tuples[0].split(',')
    row_2 = _tuples[1].split(',')

    matrix, central_x, central_y = build_matrix(row_1, row_2)
    matrix[central_x][central_y] = 'X'
    matrix = draw_matrix(row_1, matrix, 1, 2, central_x, central_y)
    matrix = draw_matrix(row_2, matrix, 2, 1, central_x, central_y)
    
    import seaborn
    seaborn.heatmap(data=matrix)
