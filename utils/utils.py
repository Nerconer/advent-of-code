import subprocess
import re
import os
import sys
from collections import Counter, deque

def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def aoc(data, part=1):
    print(f'Part {part}: {data}')
    subprocess.run("pbcopy", text=True, input=str(data))
    
def print_grid(grid , col_spaces: int = 1, row_spaces: int = 0):
    """Prints a grid with spaces between each character.

    Args:
        grid (_type_): _description_. Can be a list of strings, a list of lists of strings, a list of ints, or a list of lists of ints.
        col_spaces (int, optional): _description_. Defaults to 1.
        row_spaces (int, optional): _description_. Defaults to 0.
    """
    
    if isinstance(grid[0], list):
        if isinstance(grid[0][0], int):
            grid = [''.join(map(str, line)) for line in grid]
        elif type(grid[0][0]) == str:
            grid = [''.join(line) for line in grid]
    elif isinstance(grid[0], int):
        grid = [''.join(map(str, grid))]
        
    for line in grid:
        print((" " * col_spaces).join(line))
        [print() for _ in range(row_spaces)]