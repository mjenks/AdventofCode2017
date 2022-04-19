# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 12:51:03 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split(': ')
        data.append((int(line[0]),int(line[1])))
    return data
    
def scanner_pos(ran, time):
    pattern = 2*ran -2
    step = time%pattern
    last = ran - 1
    if step < ran:
        loc = step
    else:
        loc = 2*last - step        
    return loc    
    
def solve(puzzle_data):
    severity = 0
    for layer in puzzle_data:
        depth, ran = layer
        if scanner_pos(ran, depth) == 0:
            severity += depth*ran
    caught = True
    delay = 1
    while caught:
        safe = True
        for layer in puzzle_data:
            depth, ran = layer
            if scanner_pos(ran, depth+delay) == 0:
                safe = False
                break
        if safe:
            caught = False
            safe_delay = delay
        delay += 1
                
    return severity, safe_delay

puzzle_path = "input_day13.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)