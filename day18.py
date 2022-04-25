# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:46:03 2022

@author: mjenks
"""

reg = {
       'a': 0,
       'b': 0,
       'f': 0,
       'i': 0,
       'p': 0}

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        data.append(line)
    return data
    
def solve(puzzle_data):
    played = 0
    first = 0
    i = 0
    while i >= 0 and i < len(puzzle_data):
        inst = puzzle_data[i]
        if inst[0] == 'snd':
            try:
                played = int(inst[1])
            except:
                played = reg[inst[1]]
            i += 1
        elif inst[0] == 'set':
            try:
                y = int(inst[2])
            except:
                y = reg[inst[2]]
            reg[inst[1]] = y
            i += 1
        elif inst[0] == 'add':
            try:
                y = int(inst[2])
            except:
                y = reg[inst[2]]
            reg[inst[1]] += y
            i += 1
        elif inst[0] == 'mul':
            try:
                y = int(inst[2])
            except:
                y = reg[inst[2]]
            reg[inst[1]] = reg[inst[1]]*y
            i += 1
        elif inst[0] == 'mod':
            try:
                y = int(inst[2])
            except:
                y = reg[inst[2]]
            reg[inst[1]] = reg[inst[1]]%y
            i += 1
        elif inst[0] == 'rcv':
            if reg[inst[1]] != 0:
                first = played
                break
            else:
                i += 1
        elif inst[0] == 'jgz':
            try:
                x = int(inst[1])
            except:
                x = reg[inst[1]]
            try:
                y = int(inst[2])
            except:
                y = reg[inst[2]]
            if x > 0:
                i += y
            else:
                i += 1
                
    return first, 0

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)