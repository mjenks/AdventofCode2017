# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 12:46:03 2022

@author: mjenks
"""

prog0 = {
       'a': 0,
       'b': 0,
       'f': 0,
       'i': 0,
       'p': 0,
       'snt': [],
       'rcv': 0}
       
prog1 = {
       'a': 0,
       'b': 0,
       'f': 0,
       'i': 0,
       'p': 1,
       'snt': [],
       'rcv': 0}
       

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        data.append(line)
    return data
    
def doStep(reg, inst, snt):
    i = 0
    s = False
    if inst[0] == 'snd':
        try:
            reg['snt'].append(int(inst[1]))
        except:
            reg['snt'].append(reg[inst[1]])
        s = True
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
        if reg['rcv'] < len(snt):
            reg[inst[1]] = snt[reg['rcv']]
            reg['rcv'] += 1
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
    return i, s

def solve(puzzle_data):
    i0 = 0
    i1 = 0
    run0 = True
    run1 = True
    wait0 = False
    wait1 = False
    while run0 or run1:
        if run0:
            i, s0 = doStep(prog0, puzzle_data[i0], prog1['snt'])
            if i == 0:
                run0 = False
                wait0 = True
            i0 += i
            if i0 < 0 or i0 > len(puzzle_data):
                run0 = False
            if s0 and wait1:
                run1 = True
                wait1 = False
        if run1:
            j, s1 = doStep(prog1, puzzle_data[i1], prog0['snt'])
            if j == 0:
                run1 = False
                wait1 = True
            i1 += j
            if i1 < 0 or i1 > len(puzzle_data):
                run1 = False
            if s1 and wait0:
                run0 = True
                wait0 = False
               
                
    return len(prog1['snt'])

puzzle_path = "input_day18.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data)

print(solution)
