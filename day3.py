# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 21:45:07 2022

@author: mjenks
"""
    
def solve(puzzle_data):
    #each ring contains number up to (inclusive) the next odd square
    #first find which ring the number is on
    i = 1
    while i*i < puzzle_data:
        i += 2
    ring = i // 2
    #find where on the ring the value is
    inner = 2*ring-1
    pos = puzzle_data - inner*inner
    if pos - 2*ring <= 0: #on right side
        center_val = 1
        for j in range(ring):
            center_val += 2*(4*j) + 1
    elif pos - 4*ring <= 0: # top
        center_val = 1
        for j in range(ring):
            center_val += 2*(4*j + 1) + 1
    elif pos - 6*ring <= 0: #left
        center_val = 1
        for j in range(ring):
            center_val += 2*(4*j + 2) + 1
    else: #bottom
        center_val = 1
        for j in range(ring):
            center_val += 2*(4*j + 3) + 1
            
    #difference between the center value and the number is steps need right or left
    #ring is the steps need to get to center
    steps = abs(puzzle_data - center_val) + ring
        
    return steps, 0

    
puzzle_data =  368078
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)