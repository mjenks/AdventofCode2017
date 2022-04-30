# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 12:11:40 2022

@author: mjenks
"""

states = {}

def parse(puzzle_input):
    i = 0
    line = puzzle_input[i].strip().split()
    start = line[3][0]
    i += 1
    line = puzzle_input[i].strip().split()
    check = int(line[5])
    i += 2
    while i < len(puzzle_input):
        line = puzzle_input[i].strip().split()
        state = line[2][0]
        i += 1
        for j in range(2):
            i += 1
            line = puzzle_input[i].strip().split()
            write = int(line[4][0])
            i += 1
            line = puzzle_input[i].strip().split()
            move = line[6][0]
            i += 1
            line = puzzle_input[i].strip().split()
            cont = line[4][0]
            i+= 1
            if j == 0:
                states[state] = [[write, move, cont]]
            else:
                states[state].append([write, move, cont])
        i += 1
            
    data = start, check
    return data
    
def solve(puzzle_data):
    return 0

puzzle_path = "input_day25.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data)

print(solution)