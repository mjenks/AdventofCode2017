# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:26:40 2022

@author: mjenks

# - infected
. - clean
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = list(line.strip())
        data.append(line)
    return data
    
def solve(puzzle_data):
    burst = 0
    inf = 0
    x = 12
    y = 12
    facing = 0 #compass = ['n', 'e', 's', 'w']
    while burst < 10000:
        current = puzzle_data[x][y]
        if current == '#':
            facing = (facing+1)%4
            puzzle_data[x][y] = '.'
        else:
            facing = (facing-1)%4
            puzzle_data[x][y] = '#'
            inf += 1
        #move
        if facing == 0:
            if x == 0:
                puzzle_data.insert(0, ['.' for a in puzzle_data[0]])
            else:
                x -= 1
        elif facing == 1:
            if y == len(puzzle_data[0]) - 1:
                for a in puzzle_data:
                    a.append('.')
            y += 1
        elif facing == 2:
            if x == len(puzzle_data) - 1:
                puzzle_data.append(['.' for a in puzzle_data[0]])
            x += 1
        else:
            if y == 0:
                for a in puzzle_data:
                    a.insert(0,'.')
            else:
                y -= 1
        burst += 1
    for line in puzzle_data:
        print ''.join(line)
    return inf, 0

puzzle_path = "input_day22.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)