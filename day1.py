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
    captcha2 = 0
    i = 0
    for digit in puzzle_data:
        test = puzzle_data[(i+1)%len(puzzle_data)]
        if digit == test:
            captcha += digit
        step = len(puzzle_data)/2
        test2 = puzzle_data[(i + step)%len(puzzle_data)]
        if digit == test2:
            captcha2 += digit
        i += 1
    return captcha, captcha2

puzzle_path = "input_day1.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)