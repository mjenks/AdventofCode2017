# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:43:16 2022

@author: mjenks
"""

def parse(puzzle_input):
    s = []
    ex = []
    for line in puzzle_input:
        line = line.strip().split(' => ')
        rule = [x.split('/') for x in line]
        s.append(rule[0])
        ex.append(rule[1])
    return s, ex
    
def enhance(sqr): 
    global puzzle_data
    s, ex = puzzle_data
    if sqr in s:
        return ex[s.index(sqr)]
    else:
        flip = [x[::-1] for x in sqr]
        if flip in s:
            return ex[s.index(flip)]
        flop = sqr[::-1]
        if flop in s:
            return ex[s.index(flop)]
        ff = [x[::-1] for x in flop]
        if ff in s:
            return ex[s.index(ff)]
        rotr = [''.join([x[i] for x in sqr][::-1]) for i in range(len(sqr))]
        if rotr in s:
            return ex[s.index(rotr)]
        rotl = [''.join([x[-(i+1)] for x in sqr]) for i in range(len(sqr))]
        if rotl in s:
            return ex[s.index(rotl)]
        rf = [x[::-1] for x in rotr]
        if rf in s:
            return ex[s.index(rf)]
        lf = [x[::-1] for x in rotl]
        if lf in s:
            return ex[s.index(lf)]
        print "No match found"
        return sqr
    
def join(squares, num):
    num_rows = len(squares[0])*num
    rows = []
    j = 0
    for i in range(num_rows):
        row = []
        for sqr in squares[num*j:num*j+num]:
            row.append(sqr[i%len(sqr)])
        rows.append(''.join(row))
        if i != 0 and i%len(squares[0]) == 0:
            j += 1
    return rows
    
def solve():
    image = ['.#.', '..#','###']
    iterations = 0
    while iterations < 5:
        if len(image[0])%2 == 0:
            num = len(image[0])//2
            squares = []
            for i in range(num):
                for j in range(num):
                    squares.append([pix[2*j:2*j+2] for pix in image[2*i:2*i+2]]) 
        else:
            num = len(image[0])//3
            squares = []
            for i in range(num):
                for j in range(num):
                    squares.append([pix[3*j:3*j+3] for pix in image[3*i:3*i+3]])
        new = [enhance(x) for x in squares]
        iterations += 1
        image = join(new, num)
    pixels_on = sum([x.count('#') for x in image])
    return pixels_on, 0

puzzle_path = "input_day21.txt"
#puzzle_path = "day21_example.txt"
with open(puzzle_path) as f:
    puzzle_input = f.readlines()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve()

print(solution1)
print(solution2)