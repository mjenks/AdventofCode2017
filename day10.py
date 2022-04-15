# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:59:23 2022

@author: mjenks

rewrote entire code to solve for part 2 (go to earlier submit for part 1 code)

suffix is 17, 31, 73, 47, 23
"""

def parse(puzzle_input):
    line = puzzle_input.strip()
    data = [ord(x) for x in line]
    data.append(17)
    data.append(31)
    data.append(73)
    data.append(47)
    data.append(23)
    return data
    
def solve(puzzle_data, size):
    current_list = range(size)
    skip_size = 0
    position = 0
    rounds = 0
    while rounds < 64:
        for length in puzzle_data:
            new_list = current_list[:]
            for i in range(length):
                new_list[(position + i)%size] = current_list[(position + (length - 1) - i)%size]
            position = (position + length + skip_size)%size
            skip_size += 1
            current_list = new_list[:]
        rounds += 1
        
    dense_hash = []
    i = 0
    while i < 16:
        val = 0
        for j in range(16):
            val = val^current_list[16*i+j]
        dense_hash.append(hex(val)[2:])
        i += 1
        
    knot_hash = []
    for s in dense_hash:
        if len(s) == 2:
            knot_hash.append(s)
        else:
            knot_hash.append('0')
            knot_hash.append(s)
        
    return ''.join(knot_hash)

puzzle_path = "input_day10.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
       
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data, 256)

print(solution)