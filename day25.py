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
            direction = line[6][0]
            if direction == 'r':
                move = 1
            elif direction == 'l':
                move = -1
            else:
                print "unknown move"
                move = 0
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
    start, check = puzzle_data
    tape = [0]
    pos = 0
    i = 0
    state = start
    while i < check:
        value = tape[pos]
        action = states[state][value]
        tape[pos] = action[0]
        pos += action[1]
        if pos < 0:
            tape.insert(0,0)
            pos += 1
        if pos == len(tape):
            tape.append(0)
        state = action[2]
        i += 1
    
    return sum(tape)

puzzle_path = "input_day25.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data)

print(solution)