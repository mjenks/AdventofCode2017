# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:53:53 2022

@author: mjenks
"""
    
def solve(puzzle_data):
    buf = [0]
    pos = 0
    i = 1
    while i < 2018:
        cycle = (pos + puzzle_data)%len(buf)
        buf.insert(cycle+1, i)
        pos = cycle+1
        i += 1
    part1 = buf[pos+1]
    length = len(buf)
    val = buf[1]
    while i < 50000001:
        cycle = (pos + puzzle_data)%length
        length += 1
        pos = cycle+1
        if pos == 1:
            val = i
        i += 1
    return part1, val

    
puzzle_data = 354
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)