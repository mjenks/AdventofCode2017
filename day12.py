# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:15:55 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split('<-> ')
        connected = line[1].split(', ')
        data.append([int(x) for x in connected])
    return data
    
def solve(puzzle_data):
    group = {0}
    new = [0]
    while len(new) > 0:
        add = []
        for prog in new:
            for connect in puzzle_data[prog]:
                if connect not in group:
                    add.append(connect)
                    group.add(connect)
        new = add[:]
            
        
    return len(group), 0

puzzle_path = "input_day12.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)