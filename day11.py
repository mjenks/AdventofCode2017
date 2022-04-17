# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:41:51 2022

@author: mjenks
"""

def parse(puzzle_input):
    data = puzzle_input.strip().split(',')
    return data
    
def solve(puzzle_data):
    #count the number of steps taken in each direction
    n = puzzle_data.count('n')
    ne = puzzle_data.count('ne')
    se = puzzle_data.count('se')
    s = puzzle_data.count('s')
    sw = puzzle_data.count('sw')
    nw = puzzle_data.count('nw')

    #combine ne/nw to n and se/sw to s
    rem_n = abs(ne-nw)
    if ne >= nw:
        n += nw
        nw = 0
        ne = rem_n
    else:
        n += ne
        ne = 0
        nw = rem_n
    rem_s = abs(se-sw)
    if se >= sw:
        s += sw
        sw = 0
        se = rem_s
    else:
        s += se
        se = 0
        sw = rem_s       

    #move sw+n = nw (or e dep on rem) (or nw+s = sw if s > n)
    if n > s:
        rem_n += rem_s
        n -= rem_s
        rem_s = 0
        e_w = rem_n
    else:
        rem_s += rem_n
        s -= rem_n
        rem_n = 0
        e_w = rem_s
        
    #use n+s = 0 to remove retraced steps
    n_s = abs(n-s)
    
    steps = e_w + n_s
        
    
    return steps, 0

puzzle_path = "input_day11.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)