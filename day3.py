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
            
    #difference between the center value and the number is steps needed to center on the side of the ring
    #ring is the steps need to get to center
    steps = abs(puzzle_data - center_val) + ring
        
    return steps
    
def check_table(puzzle_data):
    sequence_path = "square_spiral_sums.txt"
    with open(sequence_path) as f:
        sequence_file = f.readlines()
    sequence = []
    for line in sequence_file[2:-1]:
        line = line.strip().split()
        sequence.append(int(line[-1]))
    for value in sequence:
        if value > puzzle_data:
            return value
    return "not found", value
    
puzzle_data =  368078
solution1 = solve(puzzle_data)
solution2 = check_table(puzzle_data)

print(solution1)
print(solution2)