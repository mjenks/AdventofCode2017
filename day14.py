# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:07:30 2022

@author: mjenks
"""

def knotHash(string):
    data = [ord(x) for x in string]
    data.append(17)
    data.append(31)
    data.append(73)
    data.append(47)
    data.append(23)
    size = 256
    current_list = range(size)
    skip_size = 0
    position = 0
    rounds = 0
    while rounds < 64:
        for length in data:
            new_list = current_list[:]
            for i in range(length):
                new_list[(position + i)%size] = current_list[(position + (length - 1) - i)%size]
            position = (position + length + skip_size)%size
            skip_size += 1
            current_list = new_list[:]
        rounds += 1
        
    dense_hash = []
    i = 0
    while i < 16:
        val = 0
        for j in range(16):
            val = val^current_list[16*i+j]
        dense_hash.append(hex(val)[2:])
        i += 1
        
    knot_hash = []
    for s in dense_hash:
        if len(s) == 2:
            knot_hash.append(s)
        else:
            knot_hash.append('0')
            knot_hash.append(s)
        
    return ''.join(knot_hash)
    
def solve(puzzle_data):
    hash_out = []
    for i in range(128):
        hash_in = puzzle_data + '-' + str(i)
        hash_out.append(knotHash(hash_in))
        
    mem_grid = []
    for row in hash_out:
        mem_row = []
        for digit in row:
            block = str(bin(int(digit, 16)))[2:].zfill(4)
            for val in block:
                mem_row.append(int(val))
        mem_grid.append(mem_row)
        
    used = sum(sum(x) for x in mem_grid)
    
    regions = []
    for i in range(128):
        row = mem_grid[i]
        for j in range(128):
            square = row[j]
            if square == 1:
                new_region = True
                for region in regions:
                    if ((i-1,j) in region) or ((i,j-1) in region):
                        region.add((i,j))
                        new_region = False
                if new_region:
                    regions.append({(i,j)})
        
    duplicates = True
    while duplicates:
        real_regions = []
        for region in regions:
            new_region = True
            for reg in real_regions:
                if not region.isdisjoint(reg):
                    reg.update(region)
                    new_region = False
            if new_region:
                real_regions.append(region)
        if len(regions) == len(real_regions):
            duplicates = False
        regions = real_regions[:]
            
    
    return used, len(regions)

    
puzzle_data = 'nbysizxe'
solution1, solution2 = solve(puzzle_data)

print(solution1)
print(solution2)