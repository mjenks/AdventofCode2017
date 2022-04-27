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
    return 0, 0

puzzle_path = "input_day22.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)