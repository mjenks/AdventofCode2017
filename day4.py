# -*- coding: utf-8 -*-
"""
Created on Thu Apr 07 10:29:10 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        data.append(line.strip().split())
    return data

def solve(puzzle_data):
    count = 0
    for passphrase in puzzle_data:
        if len(set(passphrase)) == len(passphrase):
            count += 1
    return count, 0

puzzle_path = "input_day4.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)