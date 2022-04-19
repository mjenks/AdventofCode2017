# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:51:03 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(': ')
        data.append((int(line[0]),int(line[1])))
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day13.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)