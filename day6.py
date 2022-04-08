# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 16:52:40 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = [int(x) for x in puzzle_input.strip().split()]
    return data
    
def solve(puzzle_data):
    states = set()
    cycles = 0
    state = puzzle_data[:]
    while tuple(state) not in states:
        states.add(tuple(state))
        cycles += 1
        most = max(state)
        for i in range(len(state)):
            if state[i] == most:
                state[i] = 0
                #add the blocks that evenly divide
                state = [x + most//len(state) for x in state]
                #add the remaining blocks starting after the chosen bank
                for j in range(1,most%len(state)+1):
                    state[(i+j)%len(state)] += 1
                break
    
    return cycles, 0

puzzle_path = "input_day6.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)