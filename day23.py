# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 13:47:03 2022

@author: mjenks
"""

reg = {
       'a': 1,
       'b': 0,
       'c': 0,
       'd': 0,
       'e': 0,
       'f': 0,
       'g': 0,
       'h': 0}

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        data.append(line)
    return data
    
def doStep(inst):
    i = 0
    if inst[0] == 'set':
        try:
            y = int(inst[2])
        except:
            y = reg[inst[2]]
        reg[inst[1]] = y
        i += 1
    elif inst[0] == 'mul':
        try:
            y = int(inst[2])
        except:
            y = reg[inst[2]]
        reg[inst[1]] = reg[inst[1]]*y
        i += 1
    elif inst[0] == 'sub':
        try:
            y = int(inst[2])
        except:
            y = reg[inst[2]]
        reg[inst[1]] = reg[inst[1]]-y
        i += 1
    elif inst[0] == 'jnz':
        try:
            x = int(inst[1])
        except:
            x = reg[inst[1]]
        try:
            y = int(inst[2])
        except:
            y = reg[inst[2]]
        if x != 0:
            i += y
        else:
            i += 1
    return i 
    
def solve(puzzle_data):
    i = 0
    while i >= 0 and i < len(puzzle_data):
        if i == 19:
            if reg['b']%reg['d'] == 0:
                reg['f'] = 0
            reg['e'] -= reg['g']
            reg['g'] = 0
        if i == 23:
            if reg['f'] == 0:
                reg['d'] -= reg['g']
                reg['g'] = 0
        i += doStep(puzzle_data[i])
    return reg['h']

puzzle_path = "input_day23.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data)

print(solution)