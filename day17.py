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
        
    
    return buf[pos+1], 0

    
puzzle_data = 354
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)