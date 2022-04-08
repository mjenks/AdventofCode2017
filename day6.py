# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 16:52:40 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = [int(x) for x in puzzle_input.strip().split()]
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day6.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)