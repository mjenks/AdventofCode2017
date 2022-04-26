# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:42:17 2022

@author: mjenks
"""

class Particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        
    def move(self):
        self.v = [self.v[i] + self.a[i] for i in range(3)]
        self.p = [self.p[i] + self.v[i] for i in range(3)]
        
    def dist(self):
        return sum([abs(x) for x in self.p])

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split('<')
        pos = line[1].split(',')[:-1]
        pos[2] = pos[2][:-1]
        pos = [int(x) for x in pos]
        vel = line[2].split(',')[:-1]
        vel[2] = vel[2][:-1]
        vel = [int(x) for x in vel]
        acc = line[3].split(',')
        acc[2] = acc[2][:-1]
        acc = [int(x) for x in acc]
        data.append(Particle(pos,vel,acc))
    return data
    
def solve(puzzle_data):
    closest = 0
    for i in range(10000):
        dist = []
        for part in puzzle_data:
            part.move()
            dist.append(part.dist())
        closest = dist.index(min(dist))
            
    return closest, 0

puzzle_path = "input_day20.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)