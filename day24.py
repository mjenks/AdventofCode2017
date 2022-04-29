# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:32:09 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split('/')
        data.append([int(x) for x in line])
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day24.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)