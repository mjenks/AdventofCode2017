# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 18:15:52 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = list(puzzle_input)
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day9.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)