# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 10:10:35 2022

@author: mjenks
"""

class Prog:
    def __init__(self, name, weight, holding):
        self.name = name
        self.weight = weight
        self.holding = holding
        self.depth = -1

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        name = line[0]
        weight = int(line[1][1:-1])
        if len(line) > 2:
            holding = []
            for item in line[3:]:
                holding.append(item.split(',')[0])
        else:
            holding = []
        program = Prog(name, weight, holding)
        data.append(program)
    return data
    
def solve(puzzle_data):
    #build the tree in reverse to find bottom
    i = 0
    placed = set()
    while len(placed) != len(puzzle_data):
        if i == 0:    
            for p in puzzle_data:
                if len(p.holding) == 0:
                    p.depth = i
                    placed.add(p.name)
        else:
            level = []
            for p in puzzle_data:
                if len(p.holding) == 0:
                    continue
                place = True
                for q in p.holding:
                    if q not in placed:
                        place = False
                if place and p.name not in placed:
                    level.append(p.name)
                    p.depth = i
            for name in level:
                placed.add(name)
            
        i += 1
    
    return level[0], 0

puzzle_path = "input_day7.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)