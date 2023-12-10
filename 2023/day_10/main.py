
from collections import deque

grid = open(0).read().strip().splitlines()

matrix = []
for line in grid:
    matrix.append(list(line))
    
def find_start_point(matrix: list[list[str]]) -> tuple[int, int, int]:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'S':
                return i, j, 0
    else:
        raise ValueError('No starting point found')

def find_longest_path(matrix: list[list[str]], start_point: tuple[int, int, int]):
    def bfs(matrix: list[list[str]], start_point: tuple[int, int, int]):
        valid_up_pipes = ['F', '|', '7']
        valid_down_pipes = ['L', '|', 'J']
        valid_right_pipes = ['J', '-', '7']
        valid_left_pipes = ['L', '-', 'F']
        
        
        visited = set([(start_point[0], start_point[1])])
        queue = deque([start_point])
        
        max_depth = 0
        
        while(queue):
            curr_p = queue.popleft()
            depth = curr_p[2]
                        
            #visited.add((current_point[0], current_point[1]))
            
            if matrix[curr_p[0]][curr_p[1]] == 'S' and depth > 2:
                print(f'Found S at {curr_p} with depth {depth}')
                
            
            left_position = (curr_p[0], curr_p[1] - 1)
            right_position = (curr_p[0], curr_p[1] + 1)
            up_position = (curr_p[0] - 1, curr_p[1])
            down_position = (curr_p[0] + 1, curr_p[1])
            
            # Check left
            if curr_p[1] - 1 >= 0 and matrix[curr_p[0]][curr_p[1] - 1] in valid_left_pipes and left_position not in visited:
                queue.append(left_position + (depth + 1,))
                max_depth = max(max_depth, depth + 1)
                visited.add(left_position)
             
            # Check right
            if curr_p[1] + 1 < len(matrix[curr_p[0]]) and matrix[curr_p[0]][curr_p[1] + 1] in valid_right_pipes and right_position not in visited:
                queue.append(right_position + (depth + 1,))
                max_depth = max(max_depth, depth + 1)
                visited.add(right_position)
                
            # Check up
            if curr_p[0] - 1 >= 0 and matrix[curr_p[0] - 1][curr_p[1]] in valid_up_pipes and up_position not in visited:
                queue.append(up_position + (depth + 1,))
                max_depth = max(max_depth, depth + 1)
                visited.add(up_position)
            
            # Check down
            if curr_p[0] + 1 < len(matrix) and matrix[curr_p[0] + 1][curr_p[1]] in valid_down_pipes and down_position not in visited:
                queue.append(down_position + (depth + 1,))
                max_depth = max(max_depth, depth + 1)
                visited.add(down_position)
                
        return max_depth, visited
            
  
    depth, visited = bfs(matrix, start_point)
    return depth, visited
        
    
def part_one(matrix: list[list[str]], starting_point: tuple[int, int, int]) -> int:
    return find_longest_path(matrix, starting_point)[0]

def part_two(grid, starting_point: tuple[int, int, int]):
    grid = [row.replace("S", "|") for row in grid]
    
    *_, visited = find_longest_path(matrix, starting_point)
    
    # Clean map replacing junk pipes with dots
    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i, j) not in visited:
                    matrix[i][j] = '.'
                        
    for row in grid:
        within = False
        riding = False
        for ch in row:
            pass
    """   
    *_, visited = find_longest_path(matrix, starting_point)
        
    # Clean map replacing junk pipes with dots
    for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i, j) not in visited:
                    matrix[i][j] = '.'
    
    
    for i, row in enumerate(matrix):
        s = ''
        for j, character in enumerate(row):
            pos = (i, j)
            if pos in visited:
                s+=f'\033[1m{character}\033[0m'
            else:
                s+=character
        print(s)    
    
    # Even/Odd check
    inside_tiles = 0
    for i, row in enumerate(matrix):
        for j, character in enumerate(row):
            if character == '.':
                temp_count = 0
                # Cast a ray to the right
                #for k in range(j + 1, len(row)):
                    
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
                if c % 2 == 1:
                    #print(f'Inside: {i}, {j}')
                    inside_tiles += 1
                #inside_tiles += 1 if temp_count % 2 == 1 else 0
    return inside_tiles
    """

starting_point = find_start_point(matrix)

print(f'Part 1: {part_one(matrix, starting_point)}')
print(f'Part 2: {part_two(grid, starting_point)}')