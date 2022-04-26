# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 20:53:09 2022

@author: mjenks
"""

def parse(puzzle_input): #input is square
    data = []
    for line in puzzle_input:
        row = list(line[:-1])
        data.append(row)
    return data
    
def solve(puzzle_data):
    letters = []
    i = 0
    j = puzzle_data[i].index('|')
    direction = 'd'
    end = False
    while not end:
        symb = puzzle_data[i][j]
        if symb == ' ':
            end = True
        elif symb == '|':
            if direction == 'd':
                s = symb
                while s != ' ':
                    i += 1
                    s = puzzle_data[i][j]
                    if s.isalpha():
                        letters.append(s)  
                i -= 1
            else:
                s = symb
                while s != ' ':
                    i -= 1
                    s = puzzle_data[i][j]
                    if s.isalpha():
                        letters.append(s) 
                i += 1
        elif symb == '-':
            if direction == 'r':
                s = symb
                while s != ' ':
                    j += 1
                    s = puzzle_data[i][j]
                    if s.isalpha():
                        letters.append(s) 
                j -= 1
            else:
                s = symb
                while s != ' ':
                    j -= 1
                    s = puzzle_data[i][j]
                    if s.isalpha():
                        letters.append(s)
                j += 1
        elif symb == '+':
            if direction == 'd' or direction == 'u':
                if puzzle_data[i][j+1] != ' ':
                    j += 1
                    direction = 'r'
                else:
                    j -= 1
                    direction = 'l'
            else:
                if puzzle_data[i+1][j] != ' ':
                    i += 1
                    direction = 'd'
                else:
                    i -= 1
                    direction = 'u'
        else: #will happen at the end
            if direction == 'd':
                i += 1
            elif direction == 'u':
                i -= 1
            elif direction == 'r':
                j += 1
            else:
                j -= 1
    return ''.join(letters), 0

puzzle_path = "input_day19.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)