# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:53:09 2022

@author: mjenks
"""

def parse(puzzle_input): #input is square
    data = []
    for line in puzzle_input:
        row = list(line[:-1])
        data.append(row)
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day19.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)