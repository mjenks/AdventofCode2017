# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 10:51:11 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = list(puzzle_input.strip())
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)