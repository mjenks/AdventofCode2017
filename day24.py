# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 14:32:09 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split('/')
        data.append([int(x) for x in line])
    return data
    
def solve(puzzle_data):
    wall = 0
    comp_sort = [[] for x in range(51)]
    for i in range(len(puzzle_data)):
        for pin in puzzle_data[i]:
            comp_sort[pin].append(i)
    options = [[[(x, wall)] for x in comp_sort[wall]]]
    length = 1
    strength = []
    while length < len(puzzle_data):
        new = []
        for bridge in options[length-1]:
            comp, used_pin = bridge[-1]
            comp_used = [x[0] for x in bridge]
            strength.append(sum([sum(puzzle_data[x]) for x in comp_used]))
            if puzzle_data[comp][0] != puzzle_data[comp][1]:
                pin = (set(puzzle_data[comp]) - {used_pin}).pop()
            else:
                pin = puzzle_data[comp][0]
            for new_comp in comp_sort[pin]:
                if new_comp not in comp_used:
                    current = bridge[:]
                    current.append((new_comp, pin))
                    new.append(current)
        options.append(new)
        length += 1
    return max(strength), 0

puzzle_path = "input_day24.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)