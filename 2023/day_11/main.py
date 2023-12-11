from itertools import combinations

input = open(0).read().strip().splitlines()

def distance_between_two_galaxies(g1: tuple[int, int], g2: tuple[int, int]) -> int:
    return abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

def solve(part=1):
    space = input[:]
    galaxies = set()
    empty_rows = []
    empty_cols = []

    # List of empty rows
    for i, line in enumerate(input):
        if line.count('#') == 0:
            empty_rows.append(i)
            
    # List of empty columns
    for i in range(len(input[0])):
        empty_col = True
        for j in range(len(input)):
            if input[j][i] == '#':
                empty_col = False
                break
        if empty_col:
            empty_cols.append(i)
     
          
    def expand_position(i, j) -> tuple[int, int]:
        factor = 1 if part == 1 else 999999
                
        num_empty_cols_left = len([ii for ii in empty_cols if ii < j])
        num_empty_rows_up = len([empty_row for empty_row in empty_rows if empty_row < i])
             
        return i + num_empty_rows_up * factor, j + num_empty_cols_left * factor
    
            
    for i in range(len(space)):
        for j in range(len(space[i])):
            if space[i][j] == '#':
                galaxies.add(expand_position(i, j))
                
    return sum(distance_between_two_galaxies(g1, g2) for g1, g2 in combinations(galaxies, 2))
        
print(f'Part 1: {solve(1)}')
print(f'Part 2: {solve(2)}')