# -*- coding: utf-8 -*-
"""
Created on Wed Apr 06 12:08:39 2022

@author: rikku
"""

def parse(puzzle_input):
    data = []
    for line in puzzle_input:
        line = line.strip().split()
        row = []
        for value in line:
            row.append(int(value))
        data.append(row)
    return data
    
def solve(puzzle_data):
    checksum = 0
    goal = 0
    for row in puzzle_data:
        row.sort()
        checksum += row[-1] - row[0]
        division = 0
        i = 0
        while division == 0:
            value = row[i]
            remainders = [x%value for x in row]
            j = 0
            for j in range(len(remainders)):
                if remainders[j] == 0 and i != j:
                    division = row[j]/value
            i += 1
        goal += division
    return checksum, goal

puzzle_path = "input_day2.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)