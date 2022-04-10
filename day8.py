# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:40:33 2022

@author: mjenks
"""

registers = {}

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        target_reg = line[0]
        registers[target_reg] = 0
        if line[1] == 'inc':
            action = 1
        else:
            action = -1
        val = int(line[2])
        comp_reg = line[4]
        comp = line[5]
        comp_val = int(line[6])
        data.append([target_reg, action, val, (comp_reg, comp, comp_val)])
    return data
    
def check(reg, comp, val):
    if comp == '==':
        return registers[reg] == val
    elif comp == '!=':
        return registers[reg] != val
    elif comp == '<':
        return registers[reg] < val
    elif comp == '<=':
        return registers[reg] <= val
    elif comp == '>':
        return registers[reg] > val
    elif comp == '>=':
        return registers[reg] >= val
    else:
        print comp, ' unknown'
    return False
    
def solve(puzzle_data):
    
    return max(registers), 0

puzzle_path = "input_day8.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)