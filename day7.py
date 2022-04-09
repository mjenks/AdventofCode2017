# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 10:10:35 2022

@author: mjenks
"""

class Prog:
    def __init__(self, name, weight, holding):
        self.name = name
        self.weight = weight
        self.holding = holding

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        name = line[0]
        weight = int(line[1][1:-1])
        if len(line) > 2:
            holding = line[3:]
        else:
            holding = []
        program = Prog(name, weight, holding)
        data.append(program)
    return data
    
def solve(puzzle_data):
    return 0, 0

puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)