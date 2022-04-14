# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:59:23 2022

@author: mjenks
"""

def parse(puzzle_input):
    line = puzzle_input.strip().split(',')
    data = [int(x) for x in line]
    return data
    
def solve(puzzle_data):
    current_list = range(256)
    return 0, 0

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)