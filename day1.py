# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 10:51:11 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for char in puzzle_input.strip():
        data.append(int(char))
    return data
    
def solve(puzzle_data):
    captcha = 0
    i = 0
    for digit in puzzle_data:
        if i == len(puzzle_data)-1:
            test = puzzle_data[-1]
        else:
            test = puzzle_data[i+1]
        if digit == test:
            captcha += digit
        i += 1
    return captcha, 0

puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)