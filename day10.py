# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:59:23 2022

@author: mjenks
"""

def parse(puzzle_input):
    line = puzzle_input.strip().split(',')
    data = [int(x) for x in line]
    return data
    
def solve(puzzle_data, size):
    current_list = range(size)
    skip_size = 0
    position = 0
    for length in puzzle_data:
        new_list = current_list[:]
        for i in range(length):
            new_list[(position + i)%size] = current_list[(position + (length - 1) - i)%size]
        position = (position + length + skip_size)%size
        skip_size += 1
        current_list = new_list[:]
        
    return current_list[0]*current_list[1], 0

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
example_data = [3,4,1,5]
example = solve(example_data, 5)
print(example)    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data, 256)

print(solution1)
print(solution2)