# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 09:57:56 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(int(line.strip()))
    return data
        
def solve(puzzle_data):
    loc = 0
    steps = 0
    while loc < len(puzzle_data):
        i = loc
        loc += puzzle_data[i]
        puzzle_data[i] += 1
        steps += 1
    return steps, 0

puzzle_path = "input_day5.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)