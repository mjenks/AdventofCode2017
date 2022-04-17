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
        
    #if these rem are not on the same side cancel some
    if se !=0 and nw != 0:
        if se > nw:
            se -= nw
            nw = 0
        else:
            nw -= se
            se = 0
    if ne != 0 and sw != 0:
        if ne > sw:
            ne -= sw
            sw = 0
        else:
            sw -= ne
            ne = 0

    #move all e/w to either north or south and reduce
    if n > s:
        if se != 0:
            n -= se
            ne += se
            se = 0
        if sw != 0:
            n -= sw
            nw += sw
            sw = 0
        if nw != 0 and ne != 0: #ne+nw = n
            if nw > ne:
                nw -= ne
                n += ne
                ne = 0
            else:
                ne -= nw
                n += nw
                nw = 0
    else:
        if ne != 0:
            s -= ne
            se += ne
            ne = 0
        if nw != 0:
            s -= nw
            sw += nw
            nw = 0
        if sw != 0 and se != 0: #se+sw = s
            if sw > se:
                sw -= se
                s += se
                se = 0
            else:
                se -= sw
                s += sw
                sw = 0
                
    #reduce n/s steps
    if n > s:
        n -= s
        s = 0
    else:
        s -= n
        n = 0
        
    #make sure that the two remaining values are both either north or south
    if n != 0:
        if se != 0: #se+n = ne
            if se <= n:
                ne += se
                n -= se
                se = 0
            else:
                ne += n
                se -= n
                n = 0                    
        if sw != 0:
            if sw <= n:
                nw += sw
                n -= sw
                sw = 0
            else:
                nw += n
                sw -= n
                n = 0
    if s != 0:
        if ne != 0: #se+n = ne
            if ne <= s:
                se += ne
                s -= ne
                ne = 0
            else:
                se += s
                ne -= s
                s = 0
        if nw != 0:
            if nw <= s:
                sw += nw
                s -= nw
                nw = 0
            else:
                sw += s
                nw -= s
                s = 0
                
    steps = nw + n + ne + sw + s + se
    
    return steps
    
def part2(puzzle_data):
    furthest = 0
    for i in range(1,len(puzzle_data)+1):
        dist = solve(puzzle_data[:i])
        furthest = max(furthest, dist)
    return furthest

puzzle_path = "input_day11.txt"
with open(puzzle_path) as f:
    puzzle_input = f.read()
    
puzzle_data = parse(puzzle_input)
solution1 = solve(puzzle_data)
solution2 = part2(puzzle_data)

print(solution1)
print(solution2)