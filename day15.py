# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 16:06:13 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        data.append(int(line[-1]))
    return data
    
def genA(prior):
    return (prior*16807)%2147483647    
    
def genB(prior):
    return (prior*48271)%2147483647   

def solve(puzzle_data):
    a = puzzle_data[0]
    b = puzzle_data[1]
    count = 0
    i = 0
    while i < 5000000:
        a = genA(a)
        while a%4 != 0:
            a = genA(a)
        b = genB(b)
        while b%8 != 0:
            b = genB(b)
        if str(bin(a))[-16:] == str(bin(b))[-16:]:
            count += 1
        i += 1
    return count

puzzle_path = "input_day15.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution = solve(puzzle_data)

print(solution)
