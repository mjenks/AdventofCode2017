# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:43:16 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(' => ')
        data.append([x.split('/') for x in line])
    return data
    
def solve(puzzle_data):
    image = ['.#.', '..#','###']
    return 0, 0

puzzle_path = "input_day21.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)