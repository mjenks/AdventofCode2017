# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:07:30 2022

@author: mjenks
"""

def knotHash(string):
    data = [ord(x) for x in string]
    size = 256
    current_list = range(size)
    skip_size = 0
    position = 0
    rounds = 0
    while rounds < 64:
        for length in data:
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
    
def solve(puzzle_data):
    return 0, 0

    
puzzle_data = 'nbysizxe'
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)