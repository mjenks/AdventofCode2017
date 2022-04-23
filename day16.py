# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:56:34 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for step in puzzle_input.strip().split(','):
        typ = step[0]
        if typ == 's':
            data.append((typ, int(step[1:])))
        elif typ == 'x':
            ab = step[1:].split('/')
            data.append((typ, [int(x) for x in ab]))
        elif typ == 'p':
            ab = step[1:].split('/')
            data.append((typ, ab))
    return data
    
def spin(line, num):
    return line[(-1*num):] + line[:(-1*num)]
    
def exchange(line, a, b):
    new = list(line)
    new[a] = line[b]
    new[b] = line[a]
    return ''.join(new)
    
def partner(line, a, b):
    new = list(line)
    new[line.index(a)] = b
    new[line.index(b)] = a
    return ''.join(new)
    
def solve(puzzle_data):
    start = 'abcdefghijklmnop'
    line = start[:]
    pattern = [start]
    for step in puzzle_data:
        typ = step[0]
        if typ == 's':
            line = spin(line, step[1])
        elif typ == 'x':
            line = exchange(line, step[1][0], step[1][1])
        elif typ == 'p':
            line = partner(line, step[1][0], step[1][1])
    pattern.append(line[:])
    i = 1
    while line != start:
        for step in puzzle_data:
            typ = step[0]
            if typ == 's':
                line = spin(line, step[1])
            elif typ == 'x':
                line = exchange(line, step[1][0], step[1][1])
            elif typ == 'p':
                line = partner(line, step[1][0], step[1][1])
        pattern.append(line[:])
        i += 1
    return pattern[1], pattern[1000000000%i]

puzzle_path = "input_day16.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)