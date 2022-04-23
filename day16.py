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
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day16.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)