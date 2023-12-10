
from collections import deque

grid = open(0).read().strip().splitlines()

matrix = []
for line in grid:
    matrix.append(list(line))
    
def find_start_point(matrix: list[list[str]]) -> tuple[int, int]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return i, j
    else:
        raise ValueError('No starting point found')

def find_longest_path(matrix: list[list[str]], start_point: tuple[int, int]): 
    valid_up_pipes = 'F|7'
    valid_down_pipes = 'L|J'
    valid_right_pipes = 'J-7'
    valid_left_pipes = 'L-F'
    
    visited = {start_point}
    queue = deque([start_point])
            
    while(queue):
        i, j = queue.popleft()
        ch = matrix[i][j]
        
        visited.add((i, j))
        
        # Check up
        if i > 0 and ch in "S|JL" and matrix[i - 1][j] in valid_up_pipes and (i - 1, j) not in visited:
            queue.append((i - 1, j))
        
        # Check down
        if i < len(matrix) - 1 and ch in "S|7F" and matrix[i + 1][j] in valid_down_pipes and (i + 1, j) not in visited:
            queue.append((i + 1, j))
        
        # Check left
        if j > 0 and ch in "S-J7" and matrix[i][j - 1] in valid_left_pipes and (i, j - 1) not in visited:
            queue.append((i, j - 1))
        
        # Check right
        if j < len(matrix[i]) - 1 and ch in "S-LF" and matrix[i][j + 1] in valid_right_pipes and (i, j + 1) not in visited:
            queue.append((i, j + 1))
         
    return visited
        
    
def part_one(matrix: list[list[str]], starting_point: tuple[int, int]) -> int:
    return len(find_longest_path(matrix, starting_point)) // 2

def part_two(matrix: list[list[str]], starting_point: tuple[int, int]):
    visited = find_longest_path(matrix, starting_point)
        
    # Clean map replacing junk pipes with dots
    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i, j) not in visited:
                    matrix[i][j] = '.'
    

    # Even/Odd check
    inside_tiles = 0
    for i, row in enumerate(matrix):
        for j, character in enumerate(row):
            if character == '.':
                # Cast a ray to the left                    
                xx, c = j - 1, 0
                while xx >= 0:
                    if (
                        matrix[i][xx] == '|' 
                        or matrix[i][xx] == 'F'
                        or matrix[i][xx] == '7'
                        or matrix[i][xx] == 'S'
                    ):
                        c += 1
                    xx -= 1
                inside_tiles += 1 if c % 2 == 1 else 0
    return inside_tiles
    

starting_point = find_start_point(matrix)

print(f'Part 1: {part_one(matrix, starting_point)}')
print(f'Part 2: {part_two(matrix, starting_point)}')