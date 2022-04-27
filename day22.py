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
    while burst < 10000000:
        current = puzzle_data[x][y]
        if current == '#':
            facing = (facing+1)%4
            puzzle_data[x][y] = 'F'
        elif current == 'F':
            facing = (facing+2)%4
            puzzle_data[x][y] = '.'
        elif current == '.':
            facing = (facing-1)%4
            puzzle_data[x][y] = 'W'
        else:
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
    return inf

puzzle_path = "input_day22.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data)

print(solution)