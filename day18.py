# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:46:03 2022

@author: mjenks
"""

reg = {
       'a': 0,
       'b': 0,
       'f': 0,
       'i': 0,
       'p': 0}

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        data.append(line)
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)